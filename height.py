a=[int(x) for x in raw_input().split()]
a.sort(reverse=True)
k=int(raw_input())
print a[k-1]
