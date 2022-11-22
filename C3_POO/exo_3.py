class Temps:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
    
    def affiche(self):
        print(self.h, 'h', self.m, 'm', self.s, 's')
        
    def __add__(self, other):
        h1_s = self.h * 3600 + self.m * 60 + self.s
        h2_s = other.h * 3600 + other.m * 60 + other.s
        h = ((h1_s + h2_s) // 3600) % 24 # permet de derer le depassement de 24 heures
        m = ((h1_s + h2_s) % 3600) // 60
        s = ((h1_s + h2_s) % 3600) % 60
        return Temps(h, m ,s)
        
    def __sub__(self):
        h1_s = self.h * 3600 + self.m * 60 + self.s
        h2_s = other.h * 3600 + other.m * 60 + other.s
        if h1_s - h2_s >= 0:
            diff = h2_s - h1_s
        else:
            diff = 3600 * 24 + (h1_s - h2_s)
        h = (diff // 3600) % 24 # permet de derer le depassement de 24 heures
        m = (diff % 3600) // 60
        s = (diff % 3600) % 60
        return Temps(h, m, s)
        
h1 = Temps(2, 40, 10)
h2 = Temps(3, 21, 0)
print("La différence de temps est :")
