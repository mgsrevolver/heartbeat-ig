/**
 * Fires the Heartbeat IG routine when Clay replies in an "IG draft:" thread.
 *
 * One-time setup (Clay, signed in as clay@heartbeat.chat):
 * 1. claude.ai/code/routines -> the IG routine -> add an API trigger. Copy its
 *    fire URL and token into FIRE_URL and TOKEN below. Also REMOVE the 10:00
 *    and 11:00 cron times so only `0 9 * * *` (draft) remains.
 * 2. script.google.com -> New project -> paste this file.
 * 3. Triggers (clock icon) -> Add trigger -> checkForReplies, time-driven,
 *    every 1 minute. This is plain Apps Script, no LLM calls, no cost.
 *
 * It only looks at threads whose subject contains "IG draft:", and only fires
 * when the newest message is NOT from the routine (body doesn't start with
 * "[cortex-ig]"). Each message id fires at most once.
 */
const FIRE_URL = 'PASTE_ROUTINE_API_TRIGGER_URL';
const TOKEN = 'PASTE_ROUTINE_API_TRIGGER_TOKEN';

function checkForReplies() {
  const props = PropertiesService.getScriptProperties();
  const threads = GmailApp.search('subject:"IG draft:" newer_than:2d', 0, 10);
  threads.forEach(function (t) {
    const msgs = t.getMessages();
    const last = msgs[msgs.length - 1];
    const id = last.getId();
    if (props.getProperty('fired:' + id)) return;
    const body = last.getPlainBody().trim();
    if (body.indexOf('[cortex-ig]') === 0) return; // routine's own mail
    if (msgs.length < 2) return;                   // nothing to reply to yet
    props.setProperty('fired:' + id, '1');
    UrlFetchApp.fetch(FIRE_URL, {
      method: 'post',
      contentType: 'application/json',
      headers: { Authorization: 'Bearer ' + TOKEN },
      payload: JSON.stringify({
        text: 'REPLY RECEIVED threadId=' + t.getId() + ' messageId=' + id +
              ' (new message from Clay in an IG draft thread; follow ROUTINE.md step 1 for this thread only)'
      }),
      muteHttpExceptions: true
    });
  });
}
