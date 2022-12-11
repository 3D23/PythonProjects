class Vector3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '('+str(self.x) + ';' + str(self.y) + ';' + str(self.z) + ')'

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

vector_one = Vector3D(2, 3, 4)
vector_two = Vector3D(3, 4, 5)
vector_three = vector_one + vector_two
print(str(vector_three))
vector_four = vector_one - vector_two
print(str(vector_four))
print(vector_three * vector_four)
