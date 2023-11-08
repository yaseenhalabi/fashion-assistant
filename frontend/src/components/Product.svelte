<!-- Product.svelte -->
<script>
  export let imageAddress;
  export let url;
  export let tags;
  export let price;
  export let size;
  export let color;
  export let condition;
  export let description;
</script>

<style>
  .product-card {
    border: 1px solid #e2e8f0; /* Light grey border */
    border-radius: 8px; /* Rounded corners */
    overflow: hidden; /* Ensures no content leaks outside the border */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* subtle shadow for depth */
    display: flex;
    flex-direction: column; /* Stack image on top of details */
  }

  .product-image {
    display: block;
    width: 100%; /* Full width of the container */
    object-fit: cover; /* Cover ensures that the aspect ratio is maintained without stretching the image */
    object-position: center; /* Align the image centrally */
  }

  .product-details {
    width: max-width;
    padding: 16px;
  }

  .product-tag {
    color: #5a67d8; /* A shade of indigo */
    font-weight: bold;
    text-decoration: none; /* Remove underline from tags */
    margin-bottom: 8px; /* Space between tag and price */
  }

  .product-price {
    font-size: 1.25rem; /* Larger font size for price */
    font-weight: bold;
    margin-bottom: 16px; /* Space between price and attributes */
  }

  .product-attribute {
    margin-bottom: 8px; /* Consistent margin for attributes */
  }

  .product-description {
    max-height: 100px; /* Limit height of description */
    overflow-y: auto; /* Scroll for overflow */
    border-top: 1px solid #e2e8f0; /* Separator */
    padding-top: 8px; /* Space between border and text */
  }

  /* Responsive adjustments */
  @media (min-width: 768px) {
    .product-card {
      flex-direction: row; /* Image and details side by side on larger screens */
    }

    .product-image {
      max-width: 50%;
    }

    .product-details {
      max-width: 50%;
    }
  }
</style>

<div class="product-card lg:h-80 md:h-auto w-full">
  <img class="product-image" src={imageAddress} alt="Product image" />
  <div class="product-details">
    <a href={url} class="product-tag">{tags}</a>
    <p class="product-price">Price: {price}</p>
    <p class="product-attribute">Size: {size}</p>
    <p class="product-attribute">Color: {color}</p>
    <p class="product-attribute">Condition: {condition}</p>
    <div class="product-description">
      Description: {description}
    </div>
  </div>
</div>
