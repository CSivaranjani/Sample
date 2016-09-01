import collections
a = [int(x) for x in raw_input().split()]
print [siva for siva, count in collections.Counter(a).items() if count > 1]
