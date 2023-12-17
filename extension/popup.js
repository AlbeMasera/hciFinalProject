// Inject the payload.js script into the current tab after the popout has loaded
window.addEventListener('load', function (evt) {
	chrome.extension.getBackgroundPage().chrome.tabs.executeScript(null, {
		file: 'payload.js'
	});;
});

// Listen to messages from the payload.js script and write to popout.html
chrome.runtime.onMessage.addListener(function ({message}) {
	const goodContent = "<img src=\"img/ok.svg\" alt=\Girl in a jacket\" width=\"300\" height=\"300\">"
	
	const badContent = "<img src=\"img/bad.svg\" alt=\Girl in a jacket\" width=\"300\" height=\"300\">"

	if (message.message== "Safe content"){
		document.getElementById('pagetitle').innerHTML = goodContent + " " +message.message;
	}else{
		document.getElementById('pagetitle').innerHTML = badContent + " " +message.message;
	}


});