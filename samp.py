s = [int(x) for x in raw_input().split()]

import collections
for a, count in collections.Counter(s).items():
    if count == 1:
        print a
        break
