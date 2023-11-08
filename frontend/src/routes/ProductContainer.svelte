<script>
  import Product from "../components/Product.svelte"
  import { getProducts, getProductMatches } from "../api/index.js"
  import { onMount } from 'svelte';
  
  let products = []

  onMount(async () => {
    products = await getProducts(10); // Load 10 products on component mount, for example
  });

  const fetchProductMatches = async() => {
    products = await getProductMatches(10, products)
  }
  
</script>

<div>
  <div class="grid md:grid-cols-2 gap-4">
  {#each products as product (product.url)}
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
  <button 
    on:click={fetchProductMatches} 
    class="bg-blue-500 text-white hover:bg-blue-700 py-2 w-full font-bold my-8">
    Find Matches
  </button>
</div>
