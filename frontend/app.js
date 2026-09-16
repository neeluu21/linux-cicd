async function checkBackend() {
    try {
        const response = await fetch("http://localhost:5000/api/health");
        const data = await response.json();

        document.getElementById("result").innerText = data.message;
    } catch (error) {
        document.getElementById("result").innerText =
            "Backend is not running";
    }
}
