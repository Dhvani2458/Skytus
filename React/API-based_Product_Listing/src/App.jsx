
import { useState } from "react";
import ProductList from "./components/ProductList";
import "./App.css";

const categories = [
  "All",
  "beauty",
  "fragrances",
  "furniture",
  "groceries",
  "home-decoration",
  "kitchen-accessories",
  "laptops",
  "mens-shirts",
  "mens-shoes",
  "mens-watches",
  "mobile-accessories",
  "motorcycle",
  "skin-care",
  "smartphones",
  "sports-accessories",
  "sunglasses",
  "tablets",
  "tops",
  "vehicle",
  "womens-bags",
  "womens-dresses",
  "womens-jewellery",
  "womens-shoes",
  "womens-watches",
];

function App() {
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");
  const [cart, setCart] = useState([]);
  const [notice, setNotice] = useState("");

  const cartCount = cart.reduce((total, item) => total + item.quantity, 0);

  function handleAdd(product) {
    setCart((previousCart) => {
      const existing = previousCart.find(
        (item) => item.id === product.id
      );

      if (existing) {
        return previousCart.map((item) =>
          item.id === product.id
            ? { ...item, quantity: item.quantity + 1 }
            : item
        );
      }

      return [...previousCart, { ...product, quantity: 1 }];
    });

    setNotice(`${product.title} added to cart!`);
  }

  function chooseCategory(value) {
    setCategory(value);
    document
      .getElementById("products")
      ?.scrollIntoView({ behavior: "smooth" });
  }

  return (
    <div className="amazon-page" id="top">
      <header className="main-header">
        <a href="#top" className="amazon-logo" aria-label="ShopZone home">
          shop<span>zone</span><small>.in</small>
        </a>

        <div className="delivery-location">
          <span className="location-icon">⌖</span>
          <span>
            <small>Deliver to</small>
            <strong>India</strong>
          </span>
        </div>

        <form
          className="search-bar"
          onSubmit={(event) => {
            event.preventDefault();
            document
              .getElementById("products")
              ?.scrollIntoView({ behavior: "smooth" });
          }}
        >
          <select
            aria-label="Choose category"
            value={category}
            onChange={(event) => setCategory(event.target.value)}
          >
            {categories.map((item) => (
              <option key={item} value={item}>
                {item === "All"
                  ? "All Categories"
                  : item.replaceAll("-", " ")}
              </option>
            ))}
          </select>

          <input
            type="search"
            placeholder="Search ShopZone.in"
            value={search}
            onChange={(event) => setSearch(event.target.value)}
            aria-label="Search products"
          />

          <button type="submit" aria-label="Search">⌕</button>
        </form>

        <div className="header-account">
          <small>Welcome</small>
          <strong>Guest</strong>
        </div>

        <a href="#products" className="orders-link">
          <small>Explore</small>
          <strong>Products</strong>
        </a>

        <a href="#products" className="header-cart">
          <span className="cart-emoji">🛒</span>
          <span className="cart-count">{cartCount}</span>
          <strong>Cart</strong>
        </a>
      </header>

      <nav className="category-nav" aria-label="Main navigation">
        <a href="#products" className="all-category">☰ All</a>
        <a href="#deals">Today's Deals</a>
        <a href="#products" onClick={() => setCategory("All")}>
          Best Sellers
        </a>
        <a href="#products" onClick={() => chooseCategory("smartphones")}>
          Electronics
        </a>
        <a href="#products" onClick={() => chooseCategory("womens-dresses")}>
          Fashion
        </a>
        <a href="#products" onClick={() => chooseCategory("furniture")}>
          Home & Kitchen
        </a>
        <a href="#footer">Customer Service</a>
      </nav>

      <main>
        <section className="hero-banner" id="deals">
          <div className="hero-copy">
            <p className="hero-kicker">THE EVERYDAY SHOPPING FEST</p>
            <h1>Great finds.<br />Better prices.</h1>
            <p>
              Discover electronics, fashion, home essentials and more.
            </p>
            <a href="#products" className="hero-button">Shop deals →</a>
          </div>

          <div className="hero-art" aria-hidden="true">
            <span className="hero-star">✦</span>
            <div className="hero-circle">
              <span>BIG</span>
              <strong>DEALS</strong>
              <small>EVERY DAY</small>
            </div>
          </div>
        </section>


        <section className="products-section" id="products">
          <div className="products-heading">
            <div>
              <p className="section-kicker">HANDPICKED FOR YOU</p>
              <h2>Today's top picks</h2>
              <p className="section-description">
                Explore popular products loaded from a public API.
              </p>
            </div>

            <span className="result-count">
              {category === "All"
                ? "All categories"
                : category.replaceAll("-", " ")}
            </span>
          </div>

          <div className="filter-list">
            {categories.map((item) => (
              <button
                key={item}
                className={
                  category === item
                    ? "filter-button selected"
                    : "filter-button"
                }
                onClick={() => setCategory(item)}
              >
                {item === "All" ? "All" : item.replaceAll("-", " ")}
              </button>
            ))}
          </div>

          {notice && (
            <div className="cart-notice" role="status">
              <span>✓ {notice}</span>
              <button
                onClick={() => setNotice("")}
                aria-label="Dismiss message"
              >
                ×
              </button>
            </div>
          )}

          <ProductList
            search={search}
            category={category}
            onAdd={handleAdd}
          />
        </section>
      </main>

      <a className="back-to-top" href="#top">Back to top ↑</a>

      <footer className="footer" id="footer">
        <div className="footer-main">
          <div>
            <a href="#top" className="amazon-logo footer-logo">
              shop<span>zone</span><small>.in</small>
            </a>
            <p>Your everyday destination for great finds.</p>
          </div>

          <div>
            <h3>Get to Know Us</h3>
            <a href="#top">About Us</a>
            <a href="#products">Our Products</a>
          </div>

          <div>
            <h3>Help & Support</h3>
            <a href="#footer">Contact</a>
            <a href="#products">Shopping Guide</a>
          </div>
        </div>

        <div className="footer-bottom">
          <p>
            © {new Date().getFullYear()} ShopZone. Educational UI project built with React.
          </p>
          <p>No real orders or payments are processed on this website.</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
