from math import *

# Vector2 Class
class Vector2:
    '''A Class For Representing A 2D Vector'''

    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y



    # Setters:
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if (not isinstance(value, (int, float)) or isinstance(value, bool)):
            raise TypeError("Cannot Set X To That Type! Only Int Or Float.")
        
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if (not isinstance(value, (int, float)) or isinstance(value, bool)):
            raise TypeError("Cannot Set Y To That Type! Only Int Or Float.")
        
        self._y = value




    @property
    def magnitude(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y)

    @property
    def Normalized(self) -> "Vector2":
        if (self.magnitude <= 1e-6):
            return Vector2.zero()
        return self / self.magnitude

    # Regular Instance Methods:
    def Normalize(self) -> "Vector2":
        if (self.magnitude <= 1e-6):
            return Vector2.zero()
        self /= self.magnitude

    # Static Methods
    @staticmethod
    def Dot(a : "Vector2", b : "Vector2") -> float:
        if not isinstance(a, Vector2) or not isinstance(b, Vector2):
            raise TypeError("Both Arguments Must Be Of Type Vector2.")

        return a.x * b.x + a.y * b.y
    
    @staticmethod
    def Rotate(vec, angle):
        theta = radians(angle)

        cs = cos(theta)
        sn = sin(theta)
        x = vec.x * cs - vec.y * sn
        y = vec.x * sn + vec.y * cs

        return Vector2(x, y)

    @staticmethod
    def Distance(a : "Vector2", b : "Vector2") -> float:
        if not isinstance(a, Vector2) or not isinstance(b, Vector2):
            raise TypeError("Both Arguments Must Be Of Type Vector2.")

        return (a - b).magnitude()

    @staticmethod
    def Max(a : "Vector2", b : "Vector2"):
        if not isinstance(a, Vector2) or not isinstance(b, Vector2):
            raise TypeError("Both Arguments Must Be Of Type Vector2.")

        return Vector2(max(a.x, b.x), max(a.y, b.y))

    @staticmethod
    def Min(a : "Vector2", b : "Vector2"):
        if not isinstance(a, Vector2) or not isinstance(b, Vector2):
            raise TypeError("Both Arguments Must Be Of Type Vector2.")

        return Vector2(min(a.x, b.x), min(a.y, b.y))
    
    @staticmethod
    def Angle(a : "Vector2", b : "Vector2") -> float:
        if not isinstance(a, Vector2) or not isinstance(b, Vector2):
            raise TypeError("Both Arguments Must Be Of Type Vector2.")
            
        dot_product = Vector2.Dot(a, b)
        magnitude_product = a.magnitude() * b.magnitude()

        if magnitude_product == 0: return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(cos_theta)

    @staticmethod
    def zero(): return Vector2(0, 0)
    @staticmethod
    def one(): return Vector2(1, 1)
    @staticmethod
    def right(): return Vector2(1, 0)
    @staticmethod
    def left(): return Vector2(-1, 0)
    @staticmethod
    def up(): return Vector2(0, 1)
    @staticmethod
    def down(): return Vector2(0, -1)



    # Operators
    def __add__(self, o : "Vector2"):
        if not isinstance(o, Vector2):
            raise TypeError("Can Only Add With Type Vector2.")

        return Vector2(self.x + o.x, self.y + o.y)

    def __sub__(self, o : "Vector2"):
        if not isinstance(o, Vector2):
            raise TypeError("Can Only Subtruct With Type Vector2.")

        return Vector2(self.x - o.x, self.y - o.y)

    def __mul__(self, o : float):
        return Vector2(self.x * o, self.y * o)

    def __truediv__(self, o : float):
        return Vector2(self.x / o, self.y / o)

    def __floordiv__(self, o : float):
        return Vector2(self.x // o, self.y // o)

    def __iadd__(self, o : "Vector2"):
        if not isinstance(o, Vector2):
            raise TypeError("Can Only Add With Type Vector2.")

        self.x += o.x
        self.y += o.y
        return self

    def __isub__(self, o : "Vector2"):
        if not isinstance(o, Vector2):
            raise TypeError("Can Only Subtruct With Type Vector2.")

        self.x -= o.x
        self.y -= o.y
        return self

    def __imul__(self, o : float):
        self.x *= o
        self.y *= o
        return self

    def __itruediv__(self, o : float):
        self.x /= o
        self.y /= o
        return self
    
    def __ifloordiv__(self, o : float):
        self.x //= o
        self.y //= o
        return self

    def __eq__(self, o : "Vector2"):
        if not isinstance(o, Vector2):
            raise TypeError("Can Only Compare With Type Vector2.")

        return self.x == o.x and self.y == o.y
    
    def __ne__(self, o : "Vector2"):
        if not isinstance(o, Vector2):
            raise TypeError("Can Only Compare With Type Vector2.")

        return (self.x != o.x) or (self.y != o.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y})"

# Vector3 Class
class Vector3:
    '''A Class For Representing A 3D Vector'''
    

    def __init__(self, x : float, y : float, z : float):       
        self.x = x
        self.y = y
        self.z = z



    
    # Setters:
    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value):
        if (not isinstance(value, (int, float)) or isinstance(value, bool)):
            raise TypeError("Cannot Set X To That Type! Only Int Or Float.")
        
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value):
        if (not isinstance(value, (int, float)) or isinstance(value, bool)):
            raise TypeError("Cannot Set Y To That Type! Only Int Or Float.")
        
        self._y = value

    @property
    def z(self) -> int:
        return self._z

    @z.setter
    def z(self, value):
        if (not isinstance(value, (int, float)) or isinstance(value, bool)):
            raise TypeError("Cannot Set Y To That Type! Only Int Or Float.")
        
        self._z = value





    @property
    def magnitude(self) -> float:
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

    @property
    def Normalized(self) -> "Vector3":
        mag = self.magnitude
        return Vector3(self.x / mag, self.y / mag, self.z / mag)

    def Normalize(self):
        self.x /= self.magnitude


    # Static Methods
    @staticmethod
    def Dot(a : "Vector3", b : "Vector3") -> float:
        if not isinstance(a, Vector3) or not isinstance(b, Vector3):
            raise TypeError("Both Arguments Must Be Of Type Vector3.")

        return a.x * b.x + a.y * b.y + a.z * b.z

    @staticmethod
    def Distance(a : "Vector3", b : "Vector3") -> float:
        if not isinstance(a, Vector3) or not isinstance(b, Vector3):
            raise TypeError("Both Arguments Must Be Of Type Vector3.")

        return (a - b).magnitude

    @staticmethod
    def Max(a : "Vector3", b : "Vector3"):
        if not isinstance(a, Vector3) or not isinstance(b, Vector3):
            raise TypeError("Both Arguments Must Be Of Type Vector3.")

        return Vector3(min(a.x, b.x), min(a.y, b.y), min(a.z, b.z))

    @staticmethod
    def Min(a : "Vector3", b : "Vector3"):
        if not isinstance(a, Vector3) or not isinstance(b, Vector3):
            raise TypeError("Both Arguments Must Be Of Type Vector3.")
        
        return Vector3(max(a.x, b.x), max(a.y, b.y), max(a.z, b.z))
    
    @staticmethod
    def Angle(a : "Vector3", b : "Vector3") -> float:
        if not isinstance(a, Vector3) or not isinstance(b, Vector3):
            raise TypeError("Both Arguments Must Be Of Type Vector3.")

        dot_product = Vector3.Dot(a, b)
        magnitude_product = a.magnitude * b.magnitude
        
        if magnitude_product == 0: return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(cos_theta)



    @staticmethod
    def zero(): return Vector3(0, 0, 0)
    @staticmethod
    def one(): return Vector3(1, 1, 1)
    @staticmethod
    def right(): return Vector3(1, 0, 0)
    @staticmethod
    def left(): return Vector3(-1, 0, 0)
    @staticmethod
    def up(): return Vector3(0, 1, 0)
    @staticmethod
    def down(): return Vector3(0, -1, 0)
    @staticmethod
    def back(): return Vector3(0, 0, -1)
    @staticmethod
    def forward(): return Vector3(0, 0, 1)



    # Operators
    def __add__(self, o : "Vector3"):
        if not isinstance(o, Vector3):
            raise TypeError("Can Only Add With Type Vector3.")

        return Vector3(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o : "Vector3"):
        if not isinstance(o, Vector3):
            raise TypeError("Can Only Subtruct With Type Vector3.")

        return Vector3(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, o):
        return Vector3(self.x * o, self.y * o, self.z * o)

    def __truediv__(self, o):
        return Vector3(self.x / o, self.y / o, self.z / o)
    
    def __floordiv__(self, o : float):
        return Vector3(self.x // o, self.y // o, self.z // o)

    def __iadd__(self, o : "Vector3"):
        if not isinstance(o, Vector3):
            raise TypeError("Can Only Add With Type Vector3.")
            
        self.x += o.x
        self.y += o.y
        self.z += o.z
        return self

    def __isub__(self, o : "Vector3"):
        if not isinstance(o, Vector3):
            raise TypeError("Can Only Subtruct With Type Vector3.")

        self.x -= o.x
        self.y -= o.y
        self.z -= o.z
        return self

    def __imul__(self, o):
        self.x *= o
        self.y *= o
        self.z *= o
        return self

    def __itruediv__(self, o):
        self.x /= o
        self.y /= o
        self.z /= o
        return self

    def __ifloordiv__(self, o : float):
        self.x //= o
        self.y //= o
        self.z //= o
        return self

    def __eq__(self, o : "Vector3"):
        if not isinstance(o, Vector3):
            raise TypeError("Can Only Compare With Type Vector3.")

        return self.x == o.x and self.y == o.y and self.z == o.z
    
    def __ne__(self, o : "Vector3"):
        if not isinstance(o, Vector3):
            raise TypeError("Can Only Compare With Type Vector3.")

        return self.x != o.x or self.y != o.y or self.z != o.z

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector3(x={self.x}, y={self.y}, z={self.z})"
