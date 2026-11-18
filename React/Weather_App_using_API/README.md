# Weatherly – Weather Dashboard

A responsive weather application that allows users to search for any city and view its current weather conditions using real-time data from a public weather API.

## 🌐 Live Demo

[**View Weatherly Live**](https://weatherapp-blush-nine.vercel.app/)

## ✨ Features

- **City Search:** Search for weather information by entering a city name.
- **Real-Time Weather:** Displays current temperature and weather conditions.
- **Weather Highlights:** Shows humidity, wind speed, precipitation, and feels-like temperature.
- **Weather Icons:** Displays visual icons based on weather conditions.
- **Recent Searches:** Quickly access previously searched cities.
- **Loading State:** Displays a loading indicator while fetching weather data.
- **Error Handling:** Shows user-friendly messages for invalid city names and API errors.
- **Responsive Design:** Works on desktop and mobile devices.
- **Modern UI:** Features a lavender and purple-blue theme with a dashboard layout.

## 🛠️ Technologies Used

- React.js
- JavaScript (ES6+)
- CSS3
- Vite
- Fetch API
- Async/Await
- Public Weather API
- Vercel (Deployment)

## 📚 Concepts Covered

### 1. Asynchronous JavaScript
- Used Promises to handle asynchronous operations.
- Implemented `async/await` for fetching weather information.

### 2. Fetch API
- Retrieved weather data from a public weather API.
- Processed API responses using JavaScript.

### 3. DOM Manipulation
- Updated weather information dynamically based on API responses.
- Displayed temperature, weather conditions, and other details.

### 4. Error Handling
- Handled invalid city names.
- Managed API and network errors.
- Displayed appropriate error messages.

## 🚀 Installation and Setup

Follow these steps to run the project locally.

**1. Clone the repository**

```bash
git clone <your-github-repository-url>
```

**2. Navigate to the project folder**

```bash
cd weather-app
```

**3. Install dependencies**

```bash
npm install
```

**4. Start the development server**

```bash
npm run dev
```

**5. Open in browser**

```text
http://localhost:5173
```

## 📁 Project Structure

```text
weather-app/
│
├── public/
├── src/
│   ├── components/
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
│
├── index.html
├── package.json
├── package-lock.json
└── README.md
```

*Note: The component folder structure may vary depending on the final project files.*

## 💻 How to Use

1. Open the Weatherly application.
2. Enter a city name in the search bar.
3. Click the **Search City** button.
4. View the current weather information.
5. Select a recent search to view that city's weather again.

## 🚀 Deployment

The application is deployed using Vercel.

**Live URL:** https://weatherapp-blush-nine.vercel.app/

## 👩‍💻 Author

**Dhvani Tandel**

Developed as part of an internship practical assignment to understand asynchronous JavaScript, API integration, dynamic UI updates, and error handling.
