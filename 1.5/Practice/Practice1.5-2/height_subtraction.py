class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f"{self.feet} feet, {self.inches} inches"

    def __sub__(self, other):
        height_a = self.feet * 12 + self.inches
        height_b = other.feet * 12 + other.inches

        result_inches = height_a - height_b

        result_feet = result_inches // 12
        remaining_inches = result_inches % 12

        return Height(result_feet, remaining_inches)



h1 = Height(5, 10)
h2 = Height(3, 9)

result = h1 - h2

print("Result of subtraction:")
print(result)
