document.getElementById("start-btn").addEventListener("click", function() {
    if (window.Telegram && Telegram.WebApp) {
        Telegram.WebApp.sendData(JSON.stringify({ action: "start" })); // Botga "start" signali yuboriladi
    } else {
        alert("Telegram WebApp ishlamayapti. Iltimos, Telegram orqali oching.");
    }
});