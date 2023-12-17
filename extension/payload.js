const cont = document.getElementsByTagName('html')[0].innerHTML;

const breakpoint = /<([a-z]+)(?![^>]*\/>)[^>]*>/

const splitted = cont.split(breakpoint)

const listStrings = splitted.filter(item => item);

const listStringsCleaned = listStrings.filter(function(x) {
    return x.length > 5;
});

fetch("http://127.0.0.1:8000/predict/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
   "text_list": listStringsCleaned,
    "threshold": 0.9
  })
})
.then((response) => response.json())
    .then((response) => {
        // send the page title as a chrome message
        chrome.runtime.sendMessage({message: response});
    })



