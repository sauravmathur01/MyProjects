async function getWeather() {
    const location = document.getElementById('location').value;
    const resultDiv = document.getElementById('result');

    if (!location) {
        resultDiv.innerHTML = '<p class="error">Please enter a location.</p>';
        return;
    }

    const apiKey = '870c615c02ad43cf963100752222412';
    const apiUrl = `http://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${location}&aqi=yes`;

    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error('Location not found. Please try again.');
        }

        const data = await response.json();

        resultDiv.innerHTML = `
            <h2>${data.location.name}, ${data.location.country}</h2>
            <p>Temperature: ${data.current.temp_c}°C</p>
            <p>Condition: ${data.current.condition.text}</p>
            <img src="${data.current.condition.icon}" alt="Weather Icon">
        `;
    } catch (error) {
        resultDiv.innerHTML = `<p class="error">${error.message}</p>`;
    }
}