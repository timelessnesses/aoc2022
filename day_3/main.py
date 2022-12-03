from collections import Counter
import string

with open("./day_3/input.txt") as fp:
	rucksacks = fp.read().split("\n")

h = []
for o in rucksacks:
	h.append([o[int(len(o)/2):],o[:int(len(o)/2)]])

for o in h:
	assert len(o[0]) == len(o[1])
class Character:
	def __init__(self, character: str, count: int) -> None:
		self.character = character
		self.count = count

class Compartment(object):
	def __init__(self,compartment: str):
		self.compartment = compartment

	def compare(self, second_compartment: "Compartment") -> Character:
		for character in self.compartment:
			if second_compartment.compartment.count(character):
				return Character(character, second_compartment.compartment.count(character))

g = []

stuffs = []

def priority_finder(character: Character) -> int:
	yay = list(string.ascii_letters)
	return yay.index(character.character) + 1

for o in h:
	first_compartment = Compartment(o[0])
	second_compartment = Compartment(o[1])
	stuffs.append(priority_finder(first_compartment.compare(second_compartment)))	

print(f"P1: {sum(stuffs)=}")

