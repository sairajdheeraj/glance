document.getElementById("summarizeBtn").addEventListener("click", () => processText("summarize"));
document.getElementById("explainBtn").addEventListener("click", () => processText("explain"));

function processText(action) {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            function: () => window.getSelection().toString()
        }, (results) => {
            if (results && results[0] && results[0].result) {
                const selectedText = results[0].result;
                chrome.runtime.sendMessage({ action, text: selectedText }, (response) => {
                    document.getElementById("result").innerText = response.result.summary || response.result.explanation || response.error || "No response.";
                });
            } else {
                document.getElementById("result").innerText = "No text selected!";
            }
        });
    });
}
