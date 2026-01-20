
class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def total_inches(self):
        return self.feet * 12 + self.inches

    def __gt__(self, other):
        return self.total_inches() > other.total_inches()

    def __ge__(self, other):
        return self.total_inches() >= other.total_inches()

    def __ne__(self, other):
        return self.total_inches() != other.total_inches()



h1 = Height(4, 6)
h2 = Height(4, 5)
h3 = Height(5, 9)
h4 = Height(5, 10)

print("Height(4,6) > Height(4,5):", h1 > h2)
print("Height(4,5) >= Height(4,5):", h2 >= h2)
print("Height(5,9) != Height(5,10):", h3 != h4)
