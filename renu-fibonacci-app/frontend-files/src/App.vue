<script setup lang="ts">
import { ref } from "vue"
import FibInput from './components/FibInput.vue';
import FibRecent from './components/FibRecent.vue';

const submissions = ref<number[]>([])
function handleSubmit(value: number) {
  // Keep only the last 5 values
  submissions.value = [value, ...submissions.value].slice(0, 5)
}
</script>

<template>
  <div class="container">
    <h1>Fibonacci Calculator</h1>
    <div class="section">
      <FibInput @submissions="handleSubmit"/>
    </div>
    <div>
      <FibRecent :items="submissions"/>
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
