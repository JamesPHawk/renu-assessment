<script setup lang="ts">
import { ref } from "vue"

const intValue = ref<string>("")
const message = ref<string>("")

const emit = defineEmits<{
  (e: "submitted", payload: { n: number; fibonacci: number }): void
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

  try {
    const response = await fetch("http://localhost:5000/renu-fibonacci", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ value: num }),
    })

    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.error || "API request failed")
    }

    const result = await response.json()
    console.log("API response:", result)

    emit("submitted", { n: result.submitted, fibonacci: result.fibonacci })
    message.value = `F(${result.submitted}) = ${result.fibonacci}`
    intValue.value = "" // clear input
  } catch (err: unknown) {
    if (err instanceof Error) {
      message.value = `API call failed: ${err.message}`
    } else {
      message.value = "API call failed: Unknown error"
    }
  }
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
