import { reactive } from "vue"

export interface Submission {
  index: number
  value: number
}

interface SubmissionStore {
  submissions: Submission[]
  addSubmission(sub: Submission): void
}

export const submissionStore: SubmissionStore = reactive({
  submissions: [] as Submission[],
  addSubmission(sub: Submission) {
    // Add new submission to the start
    this.submissions.unshift(sub)
    // Keep only last 5
    if (this.submissions.length > 5) {
      this.submissions.pop()
    }
  },
})