<script setup lang="ts">
import { ref } from "vue"

const intValue = ref<string>("")

function setInput(event: Event) {
  const target = event.target as HTMLInputElement
  // Remove anything that's not a digit
  target.value = target.value.replace(/\D/g, "")
  intValue.value = target.value
}

</script>

<template>
  <div class="card">
    <label class="input-text" for="integerInput">Index</label>
    <input
      id="integerInput"
      :value="intValue"
      @input="setInput"
      inputmode="numeric"
      pattern="\d*"
      class="input-field"
      placeholder="Enter an integer"
    />

    <p class="input-text">Current value: {{ intValue }}</p>
  </div>

</template>

<style scoped>
.input-field {
  border-radius: .375rem;
  background-color: #fff;
  padding: 1.25rem;
  color: rgba(47,60,69,.75)
}

.input-text {
  color: #F8F8FF;
}
</style>
