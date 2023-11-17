<script>
  let isOpen = true
  const toggleOpen = () => {
    isOpen = !isOpen
  }
</script>

<style>
</style>

<div>
  <button class="flex items-center cursor-pointer select-none" on:click={toggleOpen}>
    <span class="underline mr-2">How to Use</span>
  </button>
  <div class={`bg-gray-100 transition-height duration-300 ${isOpen ? 'max-h-40 ' : 'max-h-0'} overflow-hidden`}>
    <ol class="list-decimal px-8 m-2">
      <li>Select preferred size, color, pricing, etc in the preferences below</li>
      <li>Scroll through clothes. Click on the image of clothing types you like.</li>
    </ol>
  </div>
</div>
