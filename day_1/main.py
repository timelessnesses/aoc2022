s = open("input.txt")
g = s.read().split("\n\n")
s.close()

nice = []

for x in g:
	h = x.strip().split("\n")
	nice.append([int(x) for x in h])
	
all = []
for b in nice:
	value = 0
	for x in b:
		value += x
		
	all.append(value)
print(f"Most calrories is {sorted(all,reverse=True)[0]}")
print(f"Top 3 calories is {sorted(all,reverse=True)[0] + sorted(all,reverse=True)[1] + sorted(all,reverse=True)[2] }")
