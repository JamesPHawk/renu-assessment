<script setup lang="ts">

import { computed } from "vue"
import { submissionStore, type Submission } from "../submissionStore";

const columns = computed<(Submission | null)[]>(() => {
  const arr = submissionStore.submissions.slice(0, 5)
  const padCount = 5 - arr.length
  return [...arr, ...Array.from({ length: padCount }, () => null)]
})

</script>

<template>
  <div>
    <h2>Last 5 Submissions</h2>
    <table border="1" cellspacing="0" cellpadding="8">
      <tbody>
        <tr>
          <td><strong>n</strong></td>
          <td v-for="(c, i) in columns" :key="'n-' + i">
            {{ c ? c.n : "-" }}
          </td>
        </tr>
        <tr>
          <td><strong>value</strong></td>
          <td v-for="(c, i) in columns" :key="'val-' + i">
            {{ c ? c.fibonacci : "-" }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>