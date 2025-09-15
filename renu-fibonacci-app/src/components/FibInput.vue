<script setup lang="ts">
import { ref } from "vue"

const intValue = ref<string>("")
const message = ref<string>("")

const emit = defineEmits<{
  (e: "submitted", value: number): void
}>()

function setInput(event: Event) {
  const target = event.target as HTMLInputElement
  let value = target.value

  // allow optional leading "-" and digits only
  value = value.replace(/(?!^-)\D/g, "")

  target.value = value
  intValue.value = value
}

async function handleSubmit() {
  if (intValue.value === "" || intValue.value === "-") {
    message.value = "Please enter a valid integer."
    return
  }

  const num = parseInt(intValue.value, 10)

  // just want to get api call in place
  try {
    await fakeApiCall(num)
    emit("submitted", num)
    message.value = `Submitted successfully: ${num}`
    intValue.value = ""
  } catch {
    message.value = "API call failed."
  }
}

function fakeApiCall(value: number): Promise<void> {
  return new Promise((resolve) => {
    console.log("Stubbed API call with:", value)
    setTimeout(() => resolve(), 1000)
  })
}
</script>

<template>
  <div class="input-area">
    <label class="input-text" for="integerInput">Index</label>
    <input
      id="integerInput"
      :value="intValue"
      @input="setInput"
      inputmode="numeric"
      pattern="-?\d*"
      class="input-field"
      placeholder="Enter an integer"
    />
    <button @click="handleSubmit" class="submit-btn">Submit</button>
    <p>{{ message }}</p>
  </div>

</template>

<style scoped>

.input-area {
  display: flex;
  flex-direction: column;
  color: #F8F8FF;
}

.input-text {
  margin-bottom: .75rem;
}

.input-field {
  border-radius: .375rem;
  background-color: #fff;
  padding: 1.25rem;
  color: rgba(47,60,69,.75);
  font-size: 20px;
}

.submit-btn {
  border-radius: .375rem;
  width: 33%;
  margin-top: .75rem;
  padding: .75rem;
  font-size: 16px;
  background-color: #fff;
  color: #243746;
  transition: 0.3s;
}

.submit-btn:hover {
  background-color: #3bbfad;
}

input::placeholder {
  font-size: 20px;
}

</style>
