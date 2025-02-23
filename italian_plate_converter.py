import re


class InvalidPlateFormat(Exception):
    def __init__(self, plate_number):
        self.plate_number = plate_number
        super().__init__(f"Invalid plate format: {plate_number}\nPlate must be in the format: 'AA000AA'")


class Plate:
    def __init__(self, number):
        if self.check_format(number):
            self.number = number.upper()
        else:
            raise InvalidPlateFormat(number)

    def __str__(self):
        return f"Plate number: {self.number}"

    def __eq__(self, other):
        return self.number == other.number

    def __lt__(self, other):
        return self.convert_to_number() < other.convert_to_number()

    def __gt__(self, other):
        return self.convert_to_number() > other.convert_to_number()

    def calculate_diff(self, other):
        return abs(
            self.convert_to_number() - other.convert_to_number()
        )

    @staticmethod
    def check_format(number):
        pattern = re.compile(r"[A-Za-z]{2}\d{3}[A-Za-z]{2}")
        return pattern.fullmatch(number) is not None

    def convert_to_number(self):
        return (
            int(self.number[2:5]) +
            (ord(self.number[-1]) - ord("A")) * 1000 +
            (ord(self.number[1]) - ord("A")) * (26 ** 2) * 1000 +
            (ord(self.number[0]) - ord("A")) * (26 ** 3) * 1000
        )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("-" * 40)
    print("Welcome to italian plate converter!")
    print("-" * 40)
    print()
    print(
        "* Italian plate converter is a highly intelligent program that recognizes every car plate!\n"
        "Ok, ok...only the italian ones.\n"
        "And, yes...only the ones that follow the format 'AA000AA'.\n"
        "But it's still cool!\n\n"
    )
    p1 = input("Enter a plate number: ")
    p1 = Plate(p1)
    print(f"You entered -> {p1}")
    print(f"The plate is the number: {p1.convert_to_number():,}")

    p2 = input("Enter another plate number: ")
    p2 = Plate(p2)
    print(f"You entered -> {p2}")
    print(f"The plate is the number: {p2.convert_to_number():,}")

    print(f"The difference between the plates is: {p1.calculate_diff(p2):,}")
