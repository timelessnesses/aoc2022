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
	
you_total = 0
elf_total = 0

def is_win(elf: Selection, you: Selection) -> Outcome:
	p = 0
	if elf == you:
		p += Outcome.draw

	elif elf == Selection.rock:
		if you == Selection.scissor:
			p += Outcome.lost
		elif you == Selection.paper:
			p += Outcome.win
		else:
			raise ValueError(f"lol what {you=} {elf=}")
	elif elf == Selection.paper:
		if you == Selection.rock:
			p += Outcome.lost
		elif you == Selection.scissor:
			p += Outcome.win
		else:
			raise ValueError("kekw")
	elif elf == Selection.scissor:
		if you == Selection.paper:
			p += Outcome.lost
		elif you == Selection.rock:
			p += Outcome.win
		else:
			raise ValueError("skill issue")
	
	return p + PointSelection[you._name_]

for selection in h:
	elf,you = selection
	elf = Selection(elf)
	you = Selection(you)
	you_total += is_win(elf,you)
	elf_total += is_win(you,elf)

print(f"P1: You won {you_total} points and elf won {elf_total}")


class Selection(enum.Enum):
	rock = "A"
	paper = "B"
	scissor = "C"

class Strategy(enum.Enum):
	win = "Z"
	draw = "Y"
	lose = "X"

def round_ender(opponent_selection: Selection, end_state: Strategy) -> Selection:
	if end_state == Strategy.draw:
		return opponent_selection
	if opponent_selection == Selection.rock:
		if end_state == Strategy.win:
			return Selection.paper
		elif end_state == Strategy.lose:
			return Selection.scissor
		else:
			raise ValueError(f"what the fuck {elf=} {end_state=}")
	elif opponent_selection == Selection.paper:
		if end_state == Strategy.win:
			return Selection.scissor
		elif end_state == Strategy.lose:
			return Selection.rock
		else:
			raise ValueError("what the fuck")
	elif opponent_selection == Selection.scissor:
		if end_state == Strategy.win:
			return Selection.rock
		elif end_state == Strategy.lose:
			return Selection.paper
		else:
			raise ValueError("what the fuck")		
	else:
		raise ValueError("what the fuck")

# change for a bit here so we need to pick our own selection 

you_total = 0
elf_total = 0

for selection in h:
	elf,you = selection
	elf = Selection(elf)
	you = round_ender(elf,Strategy(you))
	you_total += is_win(elf,you)
	elf_total += is_win(you,elf)

print(f"P2: You won {you_total} points and elf won {elf_total}")