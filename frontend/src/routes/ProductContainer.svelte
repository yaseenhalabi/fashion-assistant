<script>
  import Product from "../components/Product.svelte"
  import { getProducts, getProductMatches } from "../api/index.js"
  import { onMount } from 'svelte';
  
  let products = []
  let selectedProducts = []
  let preferences = {
  }

  const updatePreference = (key, value) => {
    preferences = { ...preferences, [key]: value };
  };

  onMount(async () => {
    products = await getProducts(10); // Load 10 products on component mount, for example
  });

  const fetchProductMatches = async() => {
    products = await getProductMatches(preferences, products)
  }

  const addSelectedProduct = (product) => {
    selectedProducts.push(product)
    console.log(selectedProducts)
  }

  const removeSelectedProduct = (product) => {
    selectedProducts = selectedProducts.filter(item => item.url !== product.url);
    console.log(selectedProducts)
  }


</script>

<div>

  <div class="flex flex-col md:flex-row md:flex-wrap md:justify-between">
    <input 
      type="number" 
      placeholder="Number of Items" 
      class="p-2 border rounded m-2 flex-1"
      min="1"
      on:input={e => updatePreference('num_of_items', e.target.value)} 
    />
    <input 
      type="text" 
      placeholder="Top Size" 
      class="p-2 border rounded m-2 flex-1"
      on:input={e => updatePreference('top_size', e.target.value)} 
    />
    <input 
      type="text" 
      placeholder="Bottom Size" 
      class="p-2 border rounded m-2 flex-1"
      on:input={e => updatePreference('bot_size', e.target.value)} 
    />
    <input 
      type="text" 
      placeholder="Color" 
      class="p-2 border rounded m-2 flex-1"
      on:input={e => updatePreference('color', e.target.value)} 
    />
    <input 
      type="number" 
      placeholder="Min Price" 
      class="p-2 border rounded m-2 flex-1"
      min="0"
      on:input={e => updatePreference('min_price', e.target.value)} 
    />
    <input 
      type="number" 
      placeholder="Max Price" 
      class="p-2 border rounded m-2 flex-1"
      min="0"
      on:input={e => updatePreference('max_price', e.target.value)} 
    />
  </div>
  <button 
    on:click={fetchProductMatches} 
    class="bg-blue-500 text-white hover:bg-blue-700 py-2 w-full font-bold my-2">
    Find Matches
  </button>
  <div class="grid md:grid-cols-2 gap-4">
  {#each products as product (product.url)}
    <Product
      addSelectedProduct={() => addSelectedProduct(product)}
      removeSelectedProduct={() => removeSelectedProduct(product)}
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
</div>
