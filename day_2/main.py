# still incorrect?

with open("input.txt") as fp:
	h = fp.read().strip().split("\n")
h = [x.split() for x in h]

import enum
import aenum

class PointSelection(enum.IntEnum):
	rock = 1
	paper = 2
	scissor = 3
	
class Outcome(enum.IntEnum):
	lost = 0
	draw = 3
	win = 6

class Selection(aenum.MultiValueEnum):
	rock = "X","A"
	paper = "Y","B"
	scissor = "Z","C"
	
total = 0

def is_win(elf: Selection, you: Selection) -> Outcome:
	if elf == you: # tie
		return Outcome.draw
	if elf == Selection.rock:
		if you == Selection.paper:
			return Outcome.win
		else:
			return Outcome.lost
	elif elf == Selection.paper:
		if you == Selection.rock:
			return Outcome.win
		else:
			return Outcome.lost
	elif elf == Selection.scissor:
		if you == Selection.rock:
			return Outcome.win
		else:
			return Outcome.lost

def reward_selection(you: Selection) -> PointSelection:
	return PointSelection[you._name_]

for selection in h:
	elf,you = selection
	elf = Selection(elf)
	you = Selection(you)
	total += is_win(elf,you)
	total += reward_selection(you)

print(f"You won {total} points")
