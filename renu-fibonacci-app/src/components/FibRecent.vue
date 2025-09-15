<script setup lang="ts">
defineProps<{
  items: number[]
}>()
</script>

<template>
  <div>
    <h2>Last 5 Submissions</h2>
    <table border="1" cellspacing="0" cellpadding="8">
      <tbody>
        <tr>
          <!-- Row label -->
          <td><strong>n</strong></td>
          <!-- Submitted values -->
          <td v-for="i in 5" :key="'n-' + i">
            {{ items[i - 1] ?? '-' }}
          </td>
        </tr>
        <tr>
          <!-- Row label -->
          <td><strong>value</strong></td>
          <!-- Stubbed values for now -->
          <td v-for="i in 5" :key="'v-' + i">
            {{ items[i - 1] ?? '-' }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>

</style>
