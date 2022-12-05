with open('./day_5/input.txt') as fp:
	con = fp.read().split("\n\n")
	stacks = [h for h in con[0].split("\n")]
	moves = con[1].split("\n")

n = [[stack[i:i+3] for i in range(0, len(stack), 4)] for stack in stacks]

class Instruction:
	def __init__(self, amount: int, source: int, target: int):
		self.amount = int(amount)
		self.source = int(source)
		self.target = int(target)

	@staticmethod
	def from_text(i: str):
		return Instruction(*list(i.replace("move ","").replace("from","").replace("to","").strip().split()))

	def __str__(self):
		return f"<Instruction move {self.amount} crate(s) from {self.source} to the target {self.target}>"

	def __repr__(self):
		return self.__str__()

moves = [Instruction.from_text(move) for move in moves]

conversion_technology = {}
n.reverse()

for m in n:
	for j in range(len(m)):
		if m[j].strip() and not m[j].strip().isdigit():
			try:
				conversion_technology[j].append(m[j].strip().replace("[","").replace("]",""))
			except KeyError:
				conversion_technology[j] = [m[j]]

print(conversion_technology)

for move in moves:
	conversion_technology[move.target-1] = [x for x in reversed(conversion_technology[move.source-1][:move.amount])] + conversion_technology[move.target-1]
	conversion_technology[move.source-1] = conversion_technology[move.source-1][move.amount:]

result = []

for x in conversion_technology.values():
	if len(x[0]) > 0: 
		result.append(x[0])

print(f"P1: Crates that are on top of the stacks are {''.join(result)} ")