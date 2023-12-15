const cont = document.getElementsByTagName('html')[0].innerHTML;

const breakpoint = "<([a-z]+)(?![^>]*\/>)[^>]*>"

const splitted = cont.split(breakpoint)

const listStrings = splitted.filter(item => item);

// send the page title as a chrome message
chrome.runtime.sendMessage(listStrings[1]);

