/**
 * Fires the Heartbeat IG routine when Clay replies in an "IG draft:" thread.
 *
 * One-time setup (Clay, signed in as clay@heartbeat.chat):
 * 1. claude.ai/code/routines -> the IG routine -> Edit -> Select a trigger ->
 *    Add another trigger -> API. Copy the URL, click Generate token, copy the
 *    token (shown once). Save the routine. Leave the schedule at 0 9 * * * ET.
 * 2. script.google.com -> New project -> replace Code.gs with this file and
 *    paste the URL and token into FIRE_URL and TOKEN below. Save.
 * 3. Run testFire once (approve the Gmail + external request permissions).
 *    The log should say "HTTP 200". It fires on the newest IG draft thread,
 *    which is normally already closed, so the run just stops.
 * 4. Triggers (clock icon) -> Add trigger -> checkForReplies, Time-driven,
 *    Minutes timer, Every minute. Plain Apps Script: no LLM calls, no cost.
 *
 * It only looks at threads whose subject contains "IG draft:", and only fires
 * when the newest message is NOT from the routine (body doesn't start with
 * "[cortex-ig]"). Each message id fires at most once; a failed fire is
 * retried on the next minute.
 */
const FIRE_URL = 'PASTE_ROUTINE_API_TRIGGER_URL';
const TOKEN = 'PASTE_ROUTINE_API_TRIGGER_TOKEN';

function fire_(text) {
  const res = UrlFetchApp.fetch(FIRE_URL, {
    method: 'post',
    contentType: 'application/json',
    headers: {
      Authorization: 'Bearer ' + TOKEN,
      'anthropic-beta': 'experimental-cc-routine-2026-04-01',
      'anthropic-version': '2023-06-01'
    },
    payload: JSON.stringify({ text: text }),
    muteHttpExceptions: true
  });
  const code = res.getResponseCode();
  Logger.log('HTTP ' + code + ' ' + res.getContentText().slice(0, 300));
  return code >= 200 && code < 300;
}

function checkForReplies() {
  const props = PropertiesService.getScriptProperties();
  const threads = GmailApp.search('subject:"IG draft:" newer_than:2d', 0, 10);
  threads.forEach(function (t) {
    const msgs = t.getMessages();
    if (msgs.length < 2) return;                   // nothing to reply to yet
    const last = msgs[msgs.length - 1];
    const id = last.getId();
    if (props.getProperty('fired:' + id)) return;
    const body = last.getPlainBody().trim();
    if (body.indexOf('[cortex-ig]') === 0) return; // routine's own mail
    const ok = fire_('REPLY RECEIVED threadId=' + t.getId() + ' messageId=' + id +
      ' (new message from Clay in an IG draft thread; follow ROUTINE.md step 1 for this thread only)');
    if (ok) props.setProperty('fired:' + id, '1');
  });
}

function testFire() {
  const t = GmailApp.search('subject:"IG draft:"', 0, 1)[0];
  if (!t) { Logger.log('No IG draft thread found'); return; }
  fire_('REPLY RECEIVED threadId=' + t.getId() + ' messageId=' + t.getMessages().pop().getId() +
    ' (setup test from the Apps Script; follow ROUTINE.md step 1 for this thread only)');
}
