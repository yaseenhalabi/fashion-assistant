<!-- Product.svelte -->
<!-- Displays an individual product card-->
<script>
  export let imageAddress, url, tags, price, size, color, condition, description, addSelectedProduct, removeSelectedProduct;

  let liked = false

  const toggleLike = () => {
    if (!liked){
      addSelectedProduct()
    }
    else {
      removeSelectedProduct()
    }
    liked = !liked
  }

</script>

<style>
  .product-card {
    border: 1px solid #e2e8f0; 
    border-radius: 8px;    
    overflow: hidden; 
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
  }
  .liked {
    border: #5a67d8 4px solid;
  }
  .product-image {
    -webkit-user-drag: none;
    user-select: none;
    display: block;
    width: 100%; 
    object-fit: cover; 
    object-position: center; 
  }
  .product-details {
    width: max-width;
    padding: 16px;
  }
  .product-tag {
    color: #5a67d8; 
    font-weight: bold;
    text-decoration: none; 
    margin-bottom: 8px; 
  }
  .product-price {
    font-size: 1.25rem; 
    font-weight: bold;
    margin-bottom: 16px; 
  }
  .product-attribute {
    margin-bottom: 8px; 
  }
  .product-description {
    max-height: 100px; 
    overflow-y: auto; 
    border-top: 1px solid #e2e8f0; 
    padding-top: 8px; 
  }
  
  @media (min-width: 768px) {
    .product-card {
      flex-direction: row; 
    }
    .product-image {
      max-width: 50%;
    }
    .product-details {
      max-width: 50%;
    }
  }
</style>

<div class={`product-card lg:h-80 md:h-auto w-full ${liked? 'liked': ''}`} >
  <button class="product-image" on:click={toggleLike}>
    <img draggable="false" src={imageAddress} alt={tags}/>
  </button>
  <div class="product-details">
    <a href={url} class="product-tag">{tags}</a>
    <p class="product-price">Price: ${price}</p>
    <p class="product-attribute">Size: {size == "none"? (size[0].toUpperCase() + size.slice(1)):size.toUpperCase()}</p>
    <p class="product-attribute">Color: {color[0].toUpperCase() + color.slice(1)}</p>
    <p class="product-attribute">Condition: {condition[0].toUpperCase() + condition.slice(1)}</p>
    <div class="product-description">
      Description: {description}
    </div>
  </div>
</div>

