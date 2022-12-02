# still incorrect?

with open("./day_2/input.txt") as fp:
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

count = 1

for selection in h:
	elf,you = selection
	elf = Selection(elf)
	you = Selection(you)
	total += is_win(elf,you)
	total += reward_selection(you)

	print(
        f"""
        Round {count}
        You ended up {is_win(elf,you)._name_}
        You rewarded with {is_win(elf,you) + reward_selection(you)} points
        Game Result: {elf._name_} vs {you._name_}
        """
    )
	count += 1

print(f"You won {total} points")
