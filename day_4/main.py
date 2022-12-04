import typing

with open("./day_4/input.txt") as fp:
    cleanups = fp.read().split("\n")


class Area:
    def __init__(self, start: int, end: int) -> None:
        self.__range = range(start, end + 1)

    @property
    def range(self):
        return list(self.__range)

    def is_overlap(self, area: "Area") -> bool:
        for num in self.range:
            if num in area.range:
                return True
        return False

    def how_overlap(self, area: "Area") -> typing.List[int]:
        overlaps = []
        for num in self.range:
            if num in area.range:
                overlaps.append(num)
        return overlaps

    def is_fully_overlapped(self, area: "Area") -> bool:
        area_min = area.range[0]
        area_max = area.range[-1]
        our_min = self.range[0]
        our_max = self.range[-1]

        if (our_min <= area_min and our_max >= area_max) or (
            area_min <= our_min and area_max >= our_max
        ):
            return True
        return False

    def is_in_range_overlap(self, area: "Area") -> bool:
        area_min = area.range[0]
        area_max = area.range[-1]
        our_min = self.range[0]
        our_max = self.range[-1]
        if not (our_max < area_min or area_max < our_min):
            return True
        return False

    @staticmethod
    def from_text(input_: str) -> "Area":
        if not len(input_.strip().split("-")) == 2:
            raise ValueError(f"wtf is this {input_}")
        return Area(*[int(x) for x in input_.strip().split("-")])

    def __str__(self):
        return f"<Area start={self.range[0]} end={self.range[-1]}>"

    def __repr__(self):
        return self.__str__()


areas = []

for area in cleanups:  # clean things up a bit
    if "," in area:
        areas.append(area.split(","))

fully = []

for area in areas:
    j = []
    for h in area:
        j.append(Area.from_text(h))
    fully.append(j)

results = []

for areas in fully:
    results.append(areas[0].is_fully_overlapped(areas[1]))

print(f"P1: Amount of fully overlapped space is {len([x for x in results if x])} areas")

results = []

for areas in fully:
    results.append(areas[0].is_in_range_overlap(areas[1]))

print(
    f"P2: Amount of in-range overlapped space is {len([x for x in results if x])} areas"
)
