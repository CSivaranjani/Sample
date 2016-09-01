a1=set(raw_input())
a2=set(raw_input())
res=a2.issubset(a1)
if res==0:
    print "a1 is a subset of a2"
else:
    print "a1 is not subset of a2"
