
import React from "react";

function ProductCard({ product, onAdd }) {
  return (
    <article className="product-card">
      <div className="product-image">
        <img
          src={product.thumbnail}
          alt={product.title}
          loading="lazy"
          onError={(event) => {
            event.currentTarget.style.visibility = "hidden";
          }}
        />
        {product.discountPercentage > 10 && (
          <span className="discount-badge">
            -{Math.round(product.discountPercentage)}%
          </span>
        )}
      </div>

      <div className="product-details">
        <span className="product-category">
          {product.category.replaceAll("-", " ")}
        </span>

        <h3 title={product.title}>{product.title}</h3>

        <p className="product-description">
          {product.description}
        </p>

        <div className="product-rating">
          <span>★</span> {product.rating?.toFixed(1) || "N/A"}
          <span className="rating-label"> / 5</span>
        </div>

        <div className="product-price">
          <strong>${product.price?.toFixed(2)}</strong>
          {product.discountPercentage > 0 && (
            <span className="old-price">
              $
              {(
                product.price /
                (1 - product.discountPercentage / 100)
              ).toFixed(2)}
            </span>
          )}
        </div>

        <p
          className={
            product.stock > 0 ? "stock-status" : "out-of-stock"
          }
        >
          {product.stock > 0
            ? `${product.stock} available`
            : "Out of stock"}
        </p>

        <button
          className="add-cart-button"
          onClick={() => onAdd(product)}
          disabled={product.stock <= 0}
        >
          {product.stock > 0 ? "Add to Cart" : "Unavailable"}
        </button>
      </div>
    </article>
  );
}

export default ProductCard;
