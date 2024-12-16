import  math
class Circle:
    def __init__(self):
        self.radius = self._input_radius()
    def _input_radius(self):
        while True:
            try:
                radius = float(input("Enter radius: "))
                if radius > 0:
                    return radius
                else:
                    print("Radius must be positive.")
            except ValueError:
                print("Please enter a NUMBER.")
    def get_radius(self):
        return self.radius
    def get_square(self):
        return math.pi*(self.radius**2)
    def set_radius(self, new_radius):
        if new_radius > 0:
            self.radius = new_radius
        else:
            print("Radius must be positive.")
circle = Circle()
print("Current radius is:", circle.get_radius())
new_radius = float(input("Enter new radius: "))
circle.set_radius(new_radius)
print("New radius:", circle.get_radius())