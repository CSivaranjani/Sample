import collections
array = [int(x) for x in raw_input().split()]
for siva, count in collections.Counter(array).items():
    if count == 1:
        print siva
