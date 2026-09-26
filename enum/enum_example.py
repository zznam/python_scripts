from enum import Enum


class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3
for item in Shake:
    print(item)


