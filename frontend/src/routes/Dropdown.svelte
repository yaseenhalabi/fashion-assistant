<script>
  let isOpen = false
  const toggleOpen = () => {
    isOpen = !isOpen
  }
</script>

<style>
</style>

<div>
  <button class="flex items-center cursor-pointer select-none" on:click={toggleOpen}>
    <span class="mr-2">How to Use</span>
    <span class={`transform transition-transform ${isOpen ? 'rotate-90' : ''}`}>
      →
    </span>
  </button>
  <div class={`transition-height duration-300 ${isOpen ? 'max-h-40' : 'max-h-0'} overflow-hidden`}>
    <ol>
      <li>
        Enter your preferences
      </li>
      <li>
        Select which clothes you like the most
      </li>


    </ol>
  </div>
</div>
