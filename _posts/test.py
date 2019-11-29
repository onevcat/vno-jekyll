class TOASCII(int):
    def __new__(cls, INPUT = ''):
        if isinstance(INPUT, str):
            total = 0
            for each in INPUT:
                total += ord(each)
                INPUT = total
        return int.__new__(cls, INPUT)

print(TOASCII('A'))

