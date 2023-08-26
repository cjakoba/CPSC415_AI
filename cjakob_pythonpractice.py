HAL: int = 9000
BB: str = "8"
R2: list[str] = ["D", "2"]
L: list[int] = [3]
K = {"2SO"}
C = ["3PO"]
WALL = [["E"]]

Galactica = {"Karl": "Helo",
             "Kara": "Starbuck",
             "Lee": "Apollo"}
Galactica["Sharon"] = "Boomer"
Galactica["Marge"] = "Racetrack"
Galactica["Louanne"] = "Kat"

Germanna_levels = ["Freshman", "Sophomore"]
UMW_levels = ["Freshman", "Sophomore", "Junior", "Senior"]
MaryWash_levels = UMW_levels
CNU_levels = UMW_levels[:] # likely incorrect

class CjakobPythonPractice:
    def plus2(self, x):
        return x + 2

    def gimme_dat_set(self):
        return {"Pris", "Leon", "Roy"}


def middlest(x, y, z):
    easy_sort = sorted([x, y, z])
    return easy_sort[1]

