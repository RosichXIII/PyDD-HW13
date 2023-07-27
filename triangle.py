class TriangleLengthException(Exception):
    
    def __init__(self, param, value):
        self.param = param
        self.value = value
    
    def __str__(self):

        if self.param < self.value:
            return f'Сторона треугольника не может быть отрицательной.\n' \
            f'Заданное число {self.param} < {self.value}'
        elif self.param == self.value:
            return f'Сторона треугольника не может быть равна нулю.\n' \
            f'Заданное число {self.param} = {self.value}'
            
class TriangleError(TriangleLengthException):
    
    def __init__(self, value1: int, value2: int, value3: int):
        self.a = value1
        self.b = value2
        self.c = value3
    
    def __str__(self):
        print(f"Tреугольника со сторонами {self.a}, {self.b}, {self.c} не существует.")

class Triangle:
    
    def __init__(self, a: int, b: int, c: int) -> None:
        if a > 0:
            self.a = a
        else:
            raise TriangleLengthException(a, 0)
        if b > 0:
            self.b = b
        else:
            raise TriangleLengthException(b, 0)
        if c > 0:
            self.c = c
        else:
            raise TriangleLengthException(c, 0)
    
    def triangle_check(self):
        a = self.a
        b = self.b
        c = self.c
        if a < b + c and b < a + c and c < a + b:
            print("Такой треугольник существует", end=" ")
            if a==b==c:
                print("и он равносторонний.")
            elif a == b or a == c or b == c:
                print("и он равнобедренный.")
            else:
                print("и он разносторонний.")
        else:
            raise TriangleError(self.a, self.b, self.c)
            
