from math import sqrt

class Carre:
    def __init__(self, cote):
        self.cote = cote
    
    def perimetre(self):
        return 4 * self.cote
    
    def aire(self):
        return self.cote ** 2
    
carre_5 = Carre(5)
print("Le périmètre de l'instance carré est de", carre_5.perimetre())

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        
    def aire(self):
        p = (self.a + self.b + self.c) / 2
        return round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 3)
    
    def rect(self):
        return self.a ** 2 == self.b ** 2 + self.c ** 2 or self.b ** 2 == self.c ** 2 + self.a ** 2 or self.c ** 2 == self.a ** 2 + self.b ** 2

triangle_2_3_4 = Triangle(2, 3, 4)
print("L'aire de l'instance triangle est", triangle_2_3_4.aire())

triangle_rectangle_test = Triangle(5.4, 9, 7.2)
print("Le triangle est-il rectangle ? :", triangle_rectangle_test.rect())
