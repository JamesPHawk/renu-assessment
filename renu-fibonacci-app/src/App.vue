<script setup lang="ts">
import FibInput from './components/FibInput.vue';
import FibRecent from './components/FibRecent.vue';
</script>

<template>
  <div class="container">
    <h1>Fibonacci Calculator</h1>
    <div class="input">
      <FibInput />
    </div>
    <div>
      <FibRecent />
    </div>
  </div>
  
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
