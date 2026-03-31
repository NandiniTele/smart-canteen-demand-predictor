async function predictDemand() {
    const btnText = document.getElementById("btn-text");
    const btnLoader = document.getElementById("btn-loader");
    const resultContainer = document.getElementById("result-container");
    
    // Show loading state
    btnText.classList.add("hidden");
    btnLoader.classList.remove("hidden");
    
    // Reset result container while loading
    resultContainer.innerHTML = `
        <div class="loader" style="border-top-color: var(--accent); width: 32px; height: 32px;"></div>
        <p class="result-hint" style="margin-top: 16px;">Analyzing patterns...</p>
    `;

    const data = {
        day: document.getElementById("day").value,
        meal: document.getElementById("meal").value,
        item: document.getElementById("item").value,
        weather: document.getElementById("weather").value,
        event: document.getElementById("event").value
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.error) {
            resultContainer.innerHTML = `<div class="error-text">Error: ${result.error}</div>`;
        } else {
            // Success state - render the stylized output
            resultContainer.innerHTML = `
                <div class="result-value">${result.predicted_demand}</div>
                <div class="result-label">Estimated Plates Required</div>
            `;
        }
    } catch (error) {
        resultContainer.innerHTML = `<div class="error-text">Failed to connect to server.</div>`;
    } finally {
        // Hide loading state
        btnText.classList.remove("hidden");
        btnLoader.classList.add("hidden");
    }
}