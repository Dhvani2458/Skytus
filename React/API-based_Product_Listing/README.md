# API-Based Product Listing using React

## Project Overview

API-Based Product Listing is a responsive web application built using React. It fetches product data from a public API and displays it in an organized, user-friendly interface inspired by e-commerce websites.

The application allows users to search products, filter them by category, view product details, and add products to a demo shopping cart.

## Live Demo

**Live Website:** https://api-basedproductlisting.vercel.app/

## Features

- **API Integration:** Fetches product data from the DummyJSON Products API.
- **Product Listing:** Displays product images, names, descriptions, prices, ratings, and availability.
- **Search Functionality:** Search products by name, description, or category.
- **Category Filtering:** Filter products using category buttons and the category selector.
- **Reusable Components:** Uses separate `ProductList` and `ProductCard` components.
- **Loading State:** Displays a loading indicator while fetching data.
- **Error Handling:** Shows an error message and retry option if the API request fails.
- **Shopping Cart:** Allows users to add products and updates the cart counter.
- **Responsive Design:** Supports desktop, tablet, and mobile screen sizes.

## Technologies Used

- React.js
- JavaScript (ES6+)
- HTML5
- CSS3
- React Hooks (`useState`, `useEffect`, and `useCallback`)
- DummyJSON Products API
- Vite
- Vercel

## API Used

**DummyJSON Products API**

https://dummyjson.com/products?limit=100

The API provides sample product information, including product IDs, titles, descriptions, prices, categories, ratings, stock information, and image URLs.

## Project Structure

```text
src/
├── components/
│   ├── ProductCard.jsx
│   └── ProductList.jsx
├── services/
│   └── productApi.js
├── App.jsx
├── App.css
├── index.css
└── main.jsx
```

## Installation and Setup

### Prerequisites

- Node.js
- npm
- A code editor such as Visual Studio Code

### Steps to Run Locally

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project folder:

   ```bash
   cd YOUR_PROJECT_FOLDER
   ```

3. Install dependencies:

   ```bash
   npm install
   ```

4. Start the development server:

   ```bash
   npm run dev
   ```

5. Open the localhost URL displayed in the terminal.

## How It Works

1. The application fetches product data from the DummyJSON API.
2. React hooks manage product data, loading status, and errors.
3. The `ProductList` component displays the products and applies search and category filters.
4. The reusable `ProductCard` component displays individual product information.
5. Users can add products to the demo cart and see the cart count update.

## Limitations

- Product information is sample data provided by DummyJSON.
- The shopping cart is managed on the frontend and is not saved to a database.
- No real orders, payments, or user authentication are implemented.
- An internet connection is required to fetch product data.

## Learning Outcomes

- Understanding REST API integration in React.
- Using `useEffect` and `useState` to manage application state.
- Creating reusable React components.
- Implementing search, category filtering, and error handling.
- Designing responsive layouts with CSS.
- Deploying a React application using Vercel.

## Author

**Dhvani Tandel**

GitHub: https://github.com/Dhvani2458

---

*Developed as a React practical project to demonstrate API integration, reusable components, and responsive user interface development.*
