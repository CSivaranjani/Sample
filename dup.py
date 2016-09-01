import collections
a = raw_input().split()
print [int(siva) for siva, count in collections.Counter(a).items() if count > 1]
