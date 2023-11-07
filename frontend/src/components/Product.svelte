
<!-- Product.svelte -->
<script>
  // Props are exported variables in Svelte
  export let imageAddress;
  export let url;
  export let tags;
  export let price;
  export let size;
  export let color;
  export let condition;
  export let description;
</script>

<div class="max-h-auto lg:basis-6/12 sm:basis-full mx-auto">
  <div class="md:flex">
    <div class="md:flex-shrink-0">
      <img class="h-full w-full object-cover md:w-48" src={imageAddress} alt="IMAGE MISSING" />
    </div>
    <div class="p-8 pt-0">
      <div class="flex">✅</div>
      <div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">
        <a href={url} class="hover:underline">{tags}</a>
      </div>
      <p class="block mt-1 text-lg leading-tight font-medium text-black hover:underline">
        Price: <span class="font-bold">{price}</span>
      </p>
      <p class="mt-2 text-gray-500">Size: <strong>{size}</strong></p>
      <p class="text-gray-500">Color: <strong>{color}</strong></p>
      <p class="text-gray-500">Condition: <strong>{condition}</strong></p>
      <div class="h-20 overflow-y-auto text-gray-500 max-w-sm border-t mt-2 pt-2"> 
          Description: {description}
      </div>
    </div>
  </div>
</div>
