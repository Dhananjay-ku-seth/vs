document.addEventListener("DOMContentLoaded", () => {
    const apiKey = "35b0fb73a81844704a0d174148242602"; // Replace with your actual API key
    const city = "New Delhi"; // Replace with the city you want to fetch weather for
    const apiUrl = `http://api.weatherapi.com/v1/current.json?key=5b0fb73a81844704a0d174148242602&q=New-Delhi&aqi=yes`;

    fetch(apiUrl)
         .then(response => response.json())
         .then(data => {
             console.log(data); // Output the entire JSON response
              // Extract and use specific weather data from the response as needed
          })
         .catch(error => {
             console.error("Error fetching weather data:", error);
             document.getElementById("weather").innerText = "Failed to fetch weather data.";
         });
});
