import copy
# Helper function for solving 3 partition problem
# It return True if there exists three subsets with given sum
def subsetSum1(S, n,T,totals,bools):
	# return True if subset is found
	if (sum(totals)==0):
		return True
	# base case: no items left
	if (n < 0):
		n=len(S)
	#print(S)
	#print(totals)
	#print(bools)
	for i in range(len(totals)):
		mid = True
		for j in range(i):
			if (bools[j]==False):
				mid =True
			else:
				mid=False
		if((mid) and totals[i]-S[n]>=0):
			totals[i] = totals[i]-S[n]
			bools[i]=subsetSum1(S, n - 1, T, copy.deepcopy(totals),copy.deepcopy(bools))
			totals[i] = totals[i]+S[n]
	# Case 1. current item becomes part of first subset
	ren = False
	for i in range(len(bools)):
		ren = ren or bools[i]
	return ren


# Function for solving 3-partition problem. It return True if given
# set S[0..n-1] can be divided into three subsets with equal sum
def partition(S, n,T):
	if (n < 3):
		return False

	# get sum of all elements in the set
	total = sum(S)
	if (total!=(n/3)*T):
		return False
	totals=[]
	bools=[]
	for i in range(int(n/3)):
		totals.append(T)
		bools.append(False)
	# return True if sum is divisible by 3 and the set S can
	# be divided into three subsets with equal sum
	return ((total % 3)==0) and subsetSum1(S, n - 1,T, totals,bools)

# main function for 3-partition problem
def main():
	# Input: set of integers
	S = [23,40,27,35,24,31]
	T=90
	# number of items in S
	n = len(S)

	if (partition(S, n,T)):
		print("Yes")
	else:
		print("No")

	return 0

if __name__ == '__main__':
    main()
