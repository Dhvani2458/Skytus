
import { useCallback, useEffect, useState } from "react";
import { fetchProducts } from "../services/productApi";
import ProductCard from "./ProductCard";

function ProductList({ search, category, onAdd }) {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadProducts = useCallback(async () => {
    setLoading(true);
    setError("");

    try {
      const data = await fetchProducts();
      setProducts(data);
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadProducts();
  }, [loadProducts]);

  const filteredProducts = products.filter((product) => {
    const matchesCategory =
      category === "All" || product.category === category;

    const searchText = search.trim().toLowerCase();

    const matchesSearch =
      product.title.toLowerCase().includes(searchText) ||
      product.description.toLowerCase().includes(searchText) ||
      product.category.toLowerCase().includes(searchText);

    return matchesCategory && matchesSearch;
  });

  if (loading) {
    return (
      <div className="loading-state" role="status">
        <div className="loading-spinner"></div>
        <p>Loading products from the API...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-state" role="alert">
        <h3>Unable to load products</h3>
        <p>{error}</p>
        <button className="retry-button" onClick={loadProducts}>
          Try Again
        </button>
      </div>
    );
  }

  if (filteredProducts.length === 0) {
    return (
      <div className="no-results">
        <h3>No products found</h3>
        <p>Try a different search term or category.</p>
      </div>
    );
  }

  return (
    <div className="product-grid">
      {filteredProducts.map((product) => (
        <ProductCard
          key={product.id}
          product={product}
          onAdd={onAdd}
        />
      ))}
    </div>
  );
}

export default ProductList;
