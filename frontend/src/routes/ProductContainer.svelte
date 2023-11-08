<script>
  import Product from "../components/Product.svelte"
  import { getProducts, getProductMatches } from "../api/index.js"
  import { onMount } from 'svelte';
  
  let products = []

  onMount(async () => {
    products = await getProducts(10); // Load 10 products on component mount, for example
  });


</script>

<div class="">
  <div class="grid md:grid-cols-2 gap-4">
  {#each products as product (product.url)} <!-- Assuming each product has a unique 'id' -->
    <Product 
      imageAddress={product.image} 
      url={product.url} 
      tags={product.tags} 
      price={product.price}
      size={product.size}
      color={product.color}
      condition={product.condition}
      description={product.description}
    />
  {/each}
  </div>
  <button>hello</button>
</div>
