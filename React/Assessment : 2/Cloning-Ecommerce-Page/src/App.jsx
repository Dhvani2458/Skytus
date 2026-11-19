
import { useState } from "react";
import "./App.css";

const products = [
  {
    id: 1,
    name: "Wireless Bluetooth Headphones",
    price: 1499,
    oldPrice: 2499,
    rating: 4.5,
    category: "Electronics",
    image: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500",
    discount: "40% off",
  },
  {
    id: 2,
    name: "Smart Watch for Everyday Use",
    price: 1999,
    oldPrice: 3499,
    rating: 4.3,
    category: "Electronics",
    image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
    discount: "43% off",
  },
  {
    id: 3,
    name: "Casual Running Sneakers",
    price: 1299,
    oldPrice: 2199,
    rating: 4.4,
    category: "Fashion",
    image: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500",
    discount: "41% off",
  },
  {
    id: 4,
    name: "Everyday Travel Backpack",
    price: 999,
    oldPrice: 1599,
    rating: 4.2,
    category: "Fashion",
    image: "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500",
    discount: "38% off",
  },
  {
    id: 5,
    name: "Classic UV Protection Sunglasses",
    price: 699,
    oldPrice: 1199,
    rating: 4.1,
    category: "Fashion",
    image: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=500",
    discount: "42% off",
  },
  {
    id: 6,
    name: "Modern Home Table Lamp",
    price: 899,
    oldPrice: 1499,
    rating: 4.4,
    category: "Home",
    image: "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=500",
    discount: "40% off",
  },
  {
    id: 7,
    name: "Premium Casual Wristwatch",
    price: 1599,
    oldPrice: 2599,
    rating: 4.5,
    category: "Accessories",
    image: "https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=500",
    discount: "38% off",
  },
  {
    id: 8,
    name: "Reusable Coffee Mug",
    price: 399,
    oldPrice: 699,
    rating: 4.0,
    category: "Home",
    image: "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=500",
    discount: "43% off",
  },
];

const categories = ["All", "Electronics", "Fashion", "Home", "Accessories"];

function ProductCard({ product, onAdd }) {
  return (
    <article className="product-card">
      <span className="discount-label">{product.discount}</span>
      <div className="product-image">
        <img src={product.image} alt={product.name} loading="lazy" />
      </div>
      <div className="product-details">
        <p className="product-category">{product.category}</p>
        <h3>{product.name}</h3>
        <p className="product-rating">
          <span>★</span> {product.rating} <span className="rating-count">| Customer rating</span>
        </p>
        <div className="price-row">
          <strong>₹{product.price.toLocaleString("en-IN")}</strong>
          <del>₹{product.oldPrice.toLocaleString("en-IN")}</del>
        </div>
        <p className="delivery-text">FREE delivery on eligible orders</p>
        <button className="add-cart-button" onClick={() => onAdd(product)}>
          Add to Cart
        </button>
      </div>
    </article>
  );
}

function App() {
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");
  const [cartCount, setCartCount] = useState(0);
  const [notice, setNotice] = useState("");

  const filteredProducts = products.filter((product) => {
    const matchesSearch = product.name.toLowerCase().includes(search.toLowerCase());
    const matchesCategory = category === "All" || product.category === category;
    return matchesSearch && matchesCategory;
  });

  function handleAdd(product) {
    setCartCount((count) => count + 1);
    setNotice(`${product.name} added to your demo cart.`);
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

        <form className="search-bar" onSubmit={(event) => event.preventDefault()}>
          <select
            aria-label="Choose category"
            value={category}
            onChange={(event) => setCategory(event.target.value)}
          >
            {categories.map((item) => (
              <option key={item} value={item}>{item}</option>
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
        <a href="#products">Best Sellers</a>
        <a href="#products">Electronics</a>
        <a href="#products">Fashion</a>
        <a href="#products">Home & Kitchen</a>
        <a href="#footer">Customer Service</a>
      </nav>

      <main>
        <section className="hero-banner" id="deals">
          <div className="hero-copy">
            <p className="hero-kicker">THE EVERYDAY SHOPPING FEST</p>
            <h1>Great finds.<br />Better prices.</h1>
            <p>Discover electronics, fashion, home essentials and more.</p>
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

        <section className="quick-categories">
          <h2>Shop by category</h2>
          <div className="quick-category-list">
            {[
              { name: "Electronics", icon: "🎧" },
              { name: "Fashion", icon: "👟" },
              { name: "Home", icon: "🏠" },
              { name: "Accessories", icon: "⌚" },
            ].map((item) => (
              <button
                key={item.name}
                className="quick-category"
                onClick={() => {
                  setCategory(item.name);
                  document.getElementById("products")?.scrollIntoView({ behavior: "smooth" });
                }}
              >
                <span>{item.icon}</span>
                <strong>{item.name}</strong>
              </button>
            ))}
          </div>
        </section>

        <section className="products-section" id="products">
          <div className="products-heading">
            <div>
              <p className="section-kicker">HANDPICKED FOR YOU</p>
              <h2>Today's top picks</h2>
              <p className="section-description">Explore popular products at great prices.</p>
            </div>
            <span className="result-count">{filteredProducts.length} products</span>
          </div>

          <div className="filter-list">
            {categories.map((item) => (
              <button
                key={item}
                className={category === item ? "filter-button selected" : "filter-button"}
                onClick={() => setCategory(item)}
              >
                {item}
              </button>
            ))}
          </div>

          {notice && (
            <div className="cart-notice" role="status">
              <span>✓ {notice}</span>
              <button onClick={() => setNotice("")} aria-label="Dismiss message">×</button>
            </div>
          )}

          {filteredProducts.length > 0 ? (
            <div className="product-grid">
              {filteredProducts.map((product) => (
                <ProductCard key={product.id} product={product} onAdd={handleAdd} />
              ))}
            </div>
          ) : (
            <div className="no-results">
              <h3>No products found</h3>
              <p>Try a different search term or category.</p>
              <button onClick={() => { setSearch(""); setCategory("All"); }}>
                Clear filters
              </button>
            </div>
          )}
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
          <p>© {new Date().getFullYear()} ShopZone. Educational UI clone built with React.</p>
          <p>No real orders or payments are processed on this website.</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
