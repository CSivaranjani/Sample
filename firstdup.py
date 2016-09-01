a = [int(x) for x in raw_input().split()]

import collections
for item, count in collections.Counter(a).items():
    if count > 1:
        print item
        break

