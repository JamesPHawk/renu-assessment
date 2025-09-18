<script setup lang="ts">
import { ref } from "vue"
import { submissionStore } from "../submissionStore"

const intValue = ref<string>("")
const message = ref<string>("")

function setInput(event: Event) {
  const target = event.target as HTMLInputElement
  let value = target.value

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

    submissionStore.addSubmission({
      n: result.index,
      fibonacci: result.value,
    })
    message.value = `F(${result.index}) = ${result.value}`
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
    <label class="input-text" for="integerInput">Index (n)</label>
    <input
      id="integerInput"
      :value="intValue"
      @input="setInput"
      inputmode="numeric"
      pattern="-?\d*"
      class="input-field"
      placeholder="Enter an integer"
    />
    <div class="btn-container">
      <button @click="handleSubmit" class="submit-btn">Submit</button>
    </div>
    <p style="text-align: center;">{{ message }}</p>
    <p style="text-align: center;">This calculator will find the Fibonacci value at <br>n for -604<span>&#8804;</span>n<span>&#8804;</span>1476.</p>

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

.btn-container {
  display: flex;
  justify-content: flex-end;
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
