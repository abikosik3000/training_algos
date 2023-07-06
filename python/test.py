import enum


class CommonItem:
    pass

class ReceiptItem:
    pass

class SpecialItem:
    pass

class Status(enum.Enum):
    special = "a"
    receipt = "b"
    common = "c"

print(Status("d")) 