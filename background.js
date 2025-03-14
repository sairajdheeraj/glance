chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "summarize" || request.action === "explain") {
        const apiUrl = `http://127.0.0.1:5000/${request.action}`;
        
        fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: request.text })
        })
        .then(response => response.json())
        .then(data => sendResponse({ result: data }))
        .catch(error => sendResponse({ error: error.message }));

        return true; // Keeps the connection open for async response
    }
});
