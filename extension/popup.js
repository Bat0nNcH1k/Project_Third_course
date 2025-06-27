document.addEventListener("DOMContentLoaded", async () => {
  const resultDiv = document.getElementById("result");
  resultDiv.innerText = "Проверка...";

  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const url = tab.url;

      const response = await fetch("http://localhost:5001/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    const data = await response.json();
    resultDiv.innerText = data.result === "phishing"
      ? "⚠️ Обнаружен фишинговый сайт!"
      : "✅ Сайт безопасен.";
  } catch (e) {
    resultDiv.innerText = "Ошибка: не удалось подключиться к серверу.";
  }
});