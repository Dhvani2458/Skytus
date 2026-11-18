import { useState } from "react";
import "./App.css";

function getWeatherInfo(code) {
  const conditions = {
    0: ["Clear Sky", "☀️"],
    1: ["Mainly Clear", "🌤️"],
    2: ["Partly Cloudy", "⛅"],
    3: ["Overcast", "☁️"],
    45: ["Foggy", "🌫️"],
    48: ["Rime Fog", "🌫️"],
    51: ["Light Drizzle", "🌦️"],
    53: ["Moderate Drizzle", "🌦️"],
    55: ["Dense Drizzle", "🌧️"],
    61: ["Light Rain", "🌧️"],
    63: ["Moderate Rain", "🌧️"],
    65: ["Heavy Rain", "🌧️"],
    71: ["Light Snow", "🌨️"],
    73: ["Moderate Snow", "🌨️"],
    75: ["Heavy Snow", "❄️"],
    80: ["Rain Showers", "🌦️"],
    81: ["Moderate Showers", "🌧️"],
    82: ["Heavy Showers", "⛈️"],
    95: ["Thunderstorm", "⛈️"],
    96: ["Thunderstorm with Hail", "⛈️"],
    99: ["Heavy Thunderstorm", "⛈️"],
  };

  return conditions[code] || ["Unknown Weather", "🌡️"];
}

function App() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [recentCities, setRecentCities] = useState([]);

  const searchWeather = async (event, selectedCity) => {
    event?.preventDefault();

    const searchCity = (selectedCity || city).trim();

    if (!searchCity) {
      setError("Please enter a city name to continue.");
      setWeather(null);
      return;
    }

    setLoading(true);
    setError("");

    try {
      const geoResponse = await fetch(
        `https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(
          searchCity
        )}&count=1&language=en&format=json`
      );

      if (!geoResponse.ok) {
        throw new Error("Unable to search for this city. Try again.");
      }

      const geoData = await geoResponse.json();

      if (!geoData.results?.length) {
        throw new Error("City not found. Please check the spelling.");
      }

      const location = geoData.results[0];

      const weatherResponse = await fetch(
        `https://api.open-meteo.com/v1/forecast?latitude=${location.latitude}&longitude=${location.longitude}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,weather_code,wind_speed_10m&timezone=auto`
      );

      if (!weatherResponse.ok) {
        throw new Error("Weather data is unavailable. Please try again.");
      }

      const weatherData = await weatherResponse.json();

      if (!weatherData.current) {
        throw new Error("No current weather information was returned.");
      }

      const current = weatherData.current;
      const [condition, icon] = getWeatherInfo(current.weather_code);

      setWeather({
        city: location.name,
        country: location.country || "",
        temperature: current.temperature_2m,
        feelsLike: current.apparent_temperature,
        humidity: current.relative_humidity_2m,
        windSpeed: current.wind_speed_10m,
        precipitation: current.precipitation,
        isDay: current.is_day,
        condition,
        icon,
        time: current.time,
      });

      setRecentCities((previous) => [
        location.name,
        ...previous.filter(
          (item) => item.toLowerCase() !== location.name.toLowerCase()
        ),
      ].slice(0, 4));

      setCity(location.name);
    } catch (err) {
      setError(
        err.message || "Something went wrong. Please try again later."
      );
      setWeather(null);
    } finally {
      setLoading(false);
    }
  };

  const formattedTime = weather?.time
    ? new Date(weather.time).toLocaleString("en-IN", {
        weekday: "long",
        hour: "2-digit",
        minute: "2-digit",
      })
    : "";

  return (
    <div className="weather-app">
      <aside className="sidebar">
        <div className="side-brand">
          <span className="brand-symbol">W</span>
          <span>WEATHERY</span>
        </div>

        <div className="side-menu">
          <p className="menu-label">MENU</p>
          <div className="menu-item selected">
            <span>◉</span> Weather Dashboard
          </div>
          <div className="menu-item">
            <span>⌕</span> City Search
          </div>
        </div>

        <div className="sidebar-bottom">
          <span className="side-cloud">☁️</span>
          <p>Weather changes.</p>
          <strong>Be ready for it.</strong>
          <small>Powered by Open-Meteo</small>
        </div>
      </aside>

      <main className="dashboard">
        <header className="dashboard-header">
          <div>
            <p className="header-date">WEATHER OVERVIEW</p>
            <h1>Weather Dashboard</h1>
          </div>

          <div className="live-status">
            <span></span> Live updates
          </div>
        </header>

        <section className="search-section">
          <form
            className="search-bar"
            onSubmit={(event) => searchWeather(event)}
          >
            <span className="search-symbol">⌕</span>
            <input
              type="text"
              placeholder="Search for a city..."
              value={city}
              onChange={(event) => setCity(event.target.value)}
              aria-label="Search city"
            />
            <button type="submit" disabled={loading}>
              {loading ? "Searching..." : "Search City"}
            </button>
          </form>

          {recentCities.length > 0 && (
            <div className="recent-searches">
              <span>Recent:</span>
              {recentCities.map((item) => (
                <button
                  key={item}
                  onClick={() => {
                    setCity(item);
                    searchWeather(null, item);
                  }}
                  type="button"
                >
                  {item}
                </button>
              ))}
            </div>
          )}
        </section>

        {error && (
          <div className="error-message">
            <span>⚠</span> {error}
          </div>
        )}

        {loading && (
          <div className="loading-card">
            <div className="loader"></div>
            <p>Getting the latest weather...</p>
          </div>
        )}

        {!weather && !loading && !error && (
          <section className="empty-dashboard">
            <div className="empty-art">🌍</div>
            <h2>Explore weather around the world</h2>
            <p>
              Search for your favourite city to see its current weather,
              temperature, wind speed, and more.
            </p>
          </section>
        )}

        {weather && !loading && (
          <>
            <section className="hero-weather">
              <div className="hero-content">
                <div className="location-tag">
                  <span>📍</span> CURRENT LOCATION
                </div>

                <h2>
                  {weather.city}
                  <span>{weather.country}</span>
                </h2>

                <p className="hero-time">{formattedTime}</p>

                <div className="main-temperature">
                  {Math.round(weather.temperature)}
                  <sup>°C</sup>
                </div>

                <p className="main-condition">{weather.condition}</p>
                <p className="hero-feels">
                  Feels like {Math.round(weather.feelsLike)}°C
                </p>
              </div>

              <div className="hero-illustration">
                <div className="sun-glow"></div>
                <span>{weather.icon}</span>
                <div className="hero-cloud">☁️</div>
              </div>

              <div className="hero-bottom">
                <span>{weather.isDay ? "☀️ Daytime" : "🌙 Nighttime"}</span>
                <span>Weather data updated live</span>
              </div>
            </section>

            <section className="details-section">
              <div className="section-title">
                <div>
                  <p className="section-eyebrow">WEATHER INFORMATION</p>
                  <h2>Today's Highlights</h2>
                </div>
                <span className="detail-date">Current conditions</span>
              </div>

              <div className="details-grid">
                <div className="detail-card">
                  <div className="detail-top">
                    <span>💧</span>
                    <small>HUMIDITY</small>
                  </div>
                  <h3>{weather.humidity}<span>%</span></h3>
                  <p>Relative humidity</p>
                </div>

                <div className="detail-card">
                  <div className="detail-top">
                    <span>💨</span>
                    <small>WIND SPEED</small>
                  </div>
                  <h3>{weather.windSpeed}<span> km/h</span></h3>
                  <p>Current wind speed</p>
                </div>

                <div className="detail-card">
                  <div className="detail-top">
                    <span>🌧️</span>
                    <small>PRECIPITATION</small>
                  </div>
                  <h3>{weather.precipitation}<span> mm</span></h3>
                  <p>Current precipitation</p>
                </div>

                <div className="detail-card">
                  <div className="detail-top">
                    <span>🌡️</span>
                    <small>FEELS LIKE</small>
                  </div>
                  <h3>{Math.round(weather.feelsLike)}<span>°C</span></h3>
                  <p>Perceived temperature</p>
                </div>
              </div>
            </section>
          </>
        )}

        <footer className="dashboard-footer">
          <span>WEATHERY © 2026</span>
          <span>Made for every kind of weather ☁️</span>
        </footer>
      </main>
    </div>
  );
}

export default App;