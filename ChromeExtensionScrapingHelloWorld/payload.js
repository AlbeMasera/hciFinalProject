const cont = document.body.innerText;
// send the page title as a chrome message
chrome.runtime.sendMessage(cont);