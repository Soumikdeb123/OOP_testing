from collections import defaultdict

# Constructing dictionary d using lists
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)

# Constructing dictionary e using sets
e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['a'].add(3)
e['b'].add(4)
e['b'].add(5)

print("Using lists as the container:")
print(d)

print("\nUsing sets as the container:")
print(e)

print("d=" + str(d.items()))
print("e=" + str(e.items()))
