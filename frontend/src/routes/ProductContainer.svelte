<script>
  import Product from "../components/Product.svelte"
  import { getProducts, getProductMatches } from "../api/index.js"
  import { onMount } from 'svelte';
  
  let products = []
  let selectedProducts = []
  let preferences = {
    num_of_items: 20
  }
  let isOpen = true
  const toggleOpen = () => {
    isOpen = !isOpen
  }

  // removes the key from preferences if key.value == ''
  const updatePreference = (key, value) => {
    if (value.trim() !== '') {
      preferences = { ...preferences, [key]: value };
    } else {
      const {[key]: _, ...rest} = preferences;
      preferences = rest;
    }
  };

  onMount(async () => {
    products = await getProductMatches(preferences, products); 
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

  const handleEnterPress = (event) => {
    if (event.key === 'Enter') {
      fetchProductMatches();
    }
  };

</script>

<div>
  
  <button class="flex items-center cursor-pointer select-none" on:click={toggleOpen}>
    <span class="underline mr-2">Preferences</span>
  </button>

  <div class={`flex flex-col md:flex-row md:flex-wrap md:justify-between ${isOpen ? 'max-h-auto' : 'hidden'}`}>
    <div class="m-2 ms-0 flex-1">
      <label for="num_of_items" class="block text-sm font-medium text-gray-700">Number of Items</label>
      <input 
        placeholder="10"
        bind:value={preferences.num_of_items}
        type="number" 
        class="mt-1 p-2 border rounded w-full"
        min="1"
        on:input={e => updatePreference('num_of_items', e.target.value)} 
        on:keyup={handleEnterPress}
      />
    </div>
    <div class="m-2 flex-1">
      <label for="top_size" class="block text-sm font-medium text-gray-700">Top Size</label>
      <input 
        placeholder="any"
        type="text" 
        class="mt-1 p-2 border rounded w-full"
        on:input={e => updatePreference('top_size', e.target.value)} 
        on:keyup={handleEnterPress}
      />
    </div>
    <div class="m-2 flex-1">
      <label for="bot_size" class="block text-sm font-medium text-gray-700">Bottom Size</label>
      <input 
        placeholder="any"
        type="text" 
        class="mt-1 p-2 border rounded w-full"
        on:input={e => updatePreference('bot_size', e.target.value)} 
        on:keyup={handleEnterPress}
      />
    </div>
    <div class="m-2 flex-1">
      <label for="color" class="block text-sm font-medium text-gray-700">Color</label>
      <input 
        placeholder="any"
        type="text" 
        class="mt-1 p-2 border rounded w-full"
        on:input={e => updatePreference('color', e.target.value)} 
        on:keyup={handleEnterPress}
      />
    </div>
    <div class="m-2 flex-1">
      <label for="min_price" class="block text-sm font-medium text-gray-700">Min Price</label>
      <input 
        placeholder="any"
        type="number" 
        class="mt-1 p-2 border rounded w-full"
        min="0"
        on:input={e => updatePreference('min_price', e.target.value)} 
        on:keyup={handleEnterPress}
      />
    </div>
    <div class="m-2 me-0 flex-1">
      <label for="max_price" class="block text-sm font-medium text-gray-700">Max Price</label>
      <input 
        placeholder="any"
        type="number" 
        class="mt-1 p-2 border rounded w-full"
        min="0"
        on:input={e => updatePreference('max_price', e.target.value)} 
        on:keyup={handleEnterPress}
      />
    </div>
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
