import string

with open("./day_3/input.txt") as fp:
    rucksacks = fp.read().split("\n")

h = []
for o in rucksacks:
    h.append([o[int(len(o) / 2) :], o[: int(len(o) / 2)]])

for o in h:
    assert len(o[0]) == len(o[1])


class Character:
    def __init__(self, character: str, count: int) -> None:
        self.character = character
        self.count = count


class Compartment(object):
<<<<<<< HEAD
<<<<<<< HEAD
	def __init__(self,compartment: str) -> None:
		self.compartment = compartment
=======
=======
>>>>>>> origin/main
    def __init__(self, compartment: str):
        self.compartment = compartment

    def compare(self, second_compartment: "Compartment") -> Character:
        for character in self.compartment:
            if second_compartment.compartment.count(character):
                return Character(
                    character, second_compartment.compartment.count(character)
                )
<<<<<<< HEAD
>>>>>>> origin/main
=======
>>>>>>> origin/main


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

import math

regroupped = [
    rucksacks[3 * i : 3 * i + 3] for i in range(0, math.ceil(len(rucksacks) / 3))
]  # THIS IS SO UGLY


def p2_comparer(first: str, second: str, third: str) -> Character:
    for character in first:
        if second.count(character) and third.count(character):
            return Character(character, 0)


stuffs = []

for h in regroupped:
    stuffs.append(priority_finder(p2_comparer(*h)))

print(f"P2: {sum(stuffs)=}")
