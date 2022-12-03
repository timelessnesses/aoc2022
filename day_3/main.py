from collections import Counter

with open("./day_3/input.txt") as fp:
	rucksacks = fp.read().split("\n")

h = []
for o in rucksacks:
	h.append([o[int(len(o)/2):],o[:int(len(o)/2)]])

class Compartment(object):
	def __init__(self,compartment: str):
		self.compartment = compartment

	def compare(self, second_compartment: "Compartment") -> dict:
		l = {}
		for character in self.compartment:
			if second_compartment.compartment.count(character):
				l.update({character: second_compartment.compartment.count(character)})
		return l

g = []

stuffs = []

for o in h:
	first_compartment = Compartment(o[0])
	second_compartment = Compartment(o[1])
	print(first_compartment.compare(second_compartment))