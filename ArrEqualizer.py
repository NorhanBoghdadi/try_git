n = int(input())    # Read input from user
ar = [int(x) for x in input().split()]  # Mapped input into list of integers
ac = [(x, ar.count(x)) for x in set(ar)]    # Mapped unique elements of ar to a list of tuples containing the element and it's frequency
ac = sorted(ac, key = lambda x: -x[1])  # Sorted ac using frequency
res = 0
for i in range(1,len(ac)):  # Loop over all elements of ac
    res += ac[i][1] # add frequency of the element to the final result
print(res)  # Print the final result
 
