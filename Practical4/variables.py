a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
# d is larger than e, so population growth is decelerating in Scotland.
if d > e:
    print("d is larger than e")
elif e > d:
    print("e is larger than d")
else:
    print("d and e are equal")