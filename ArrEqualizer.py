n = int(input())
ar = [int(x) for x in input().split()]
ac = [(x, ar.count(x)) for x in set(ar)]
ac = sorted(ac, key = lambda x: -x[1])
res = 0
for i in range(1,len(ac)):
    res += ac[i][1]
print(res)
 