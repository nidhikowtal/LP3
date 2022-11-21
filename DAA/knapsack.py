import sys


def knapSack(maxWeight, wt, val, n):
	dp=[]
	for i in range(n):
		temp=[]
		for j in range(maxWeight+1):
			temp.append(0)
		dp.append(temp)

	for i in range(wt[0],maxWeight+1):
		dp[0][i]=val[0]

	for i in range(1,n):
		for j in range(maxWeight + 1):
			notTake=0+dp[i-1][j]
			take=-sys.maxsize-1

			if(wt[i]<=j):
				take=val[i]+dp[i-1][j-wt[i]]
			dp[i][j]=max(take, notTake)

	return dp[n-1][maxWeight]


wt=[3, 4, 6, 5]
val=[2, 3, 1, 4]
W = 8
n = len(val)
print("Maximum total value : ", knapSack(W, wt, val, n))