# Amazon-Inspired E-Commerce Landing Page

## 📌 Project Overview

This project is a responsive, UI-only e-commerce landing page developed using ReactJS as part of **Assessment 2: Clone a Landing Page (Amazon / Flipkart UI)**.

The website features an Amazon-inspired shopping interface with a navigation bar, search functionality, promotional banner, product categories, product listings, and a shopping cart counter.

This project is created for educational purposes and does not include backend services, user authentication, or payment integration.

## ✨ Features

- **Header and Navigation:** Amazon-inspired header with a custom ShopZone logo, navigation links, and cart counter.
- **Search Bar:** Search products by name.
- **Promotional Banner:** Attractive banner with a shopping call-to-action.
- **Product Categories:** Browse products by category.
- **Product Listing:** Eight sample products displayed dynamically.
- **Product Cards:** Product images, names, prices, ratings, and discount labels.
- **Add to Cart:** Update the demo cart counter using React state.
- **Responsive Design:** Layout adapts to desktop, tablet, and mobile screens.
- **Footer:** Includes informational links and project details.

## 🛠️ Technologies Used

- ReactJS
- JavaScript (ES6+)
- HTML5
- CSS3
- Vite
- Git and GitHub

## ⚛️ React Concepts Implemented

- **Functional Components:** Built using reusable React components.
- **Props:** Product information is passed to the reusable `ProductCard` component.
- **State Management:** `useState` manages search input, category selection, cart count, and notifications.
- **Dynamic Rendering:** `map()` renders product cards and category buttons.
- **Array Methods:** `filter()` implements product search and category filtering.
- **Event Handling:** Handles search input, category selection, and Add to Cart clicks.

## 📂 Project Structure

```text
ecommerce-landing-page/
├── public/
├── src/
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── assets/
├── .gitignore
├── eslint.config.js
├── index.html
├── package.json
├── package-lock.json
├── vite.config.js
└── README.md
```

*Note: The contents of the `src/` folder may vary depending on your project setup.*

## 🚀 Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Navigate to the project directory

```bash
cd ecommerce-landing-page
```

### 3. Install dependencies

```bash
npm install
```

### 4. Start the development server

```bash
npm run dev
```

Open the local URL displayed in the terminal, usually:

`http://localhost:5173/`

## 📱 Responsive Design

CSS Flexbox, CSS Grid, and media queries are used to make the website responsive across desktop, tablet, and mobile devices.

## 🛒 Project Limitations

- No backend or database integration.
- No user registration or authentication.
- No real checkout or payment processing.
- Product information, prices, ratings, and discounts are sample data.
- The cart counter is for demonstration purposes only.

## 🎯 Learning Outcomes

- Understanding React functional components and props.
- Managing UI state with `useState`.
- Rendering dynamic lists using `map()`.
- Implementing search and category filters.
- Creating reusable product cards.
- Developing responsive layouts using CSS.
- Building an e-commerce interface inspired by a real-world shopping website.

## 👩‍💻 Author

**Dhvani Tandel**

GitHub: [Dhvani2458](https://github.com/Dhvani2458)

## 📄 Disclaimer

This project is an educational e-commerce UI clone inspired by Amazon's shopping interface. It is not affiliated with or endorsed by Amazon. The logo, product information, prices, ratings, and promotional content are used for demonstration purposes.

---

**Project:** Assessment 2 — Clone a Landing Page (Amazon / Flipkart UI)  
**Built with:** ReactJS and CSS
