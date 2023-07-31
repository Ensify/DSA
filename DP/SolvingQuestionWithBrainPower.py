class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n=len(questions)
        dp=[0 for _ in range(n)]
        dp[-1] = questions[-1][0]

        for i in range(n-2,-1,-1):
            dp[i] = questions[i][0]
            k=i+questions[i][1]+1
            if k<n:
                dp[i]+=dp[k]
            dp[i] = max(dp[i+1],dp[i])

        return dp[0]