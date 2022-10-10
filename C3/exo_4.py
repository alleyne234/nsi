from math import cos, sin, pi

class Angle:
    def __init__(self, angle):
        self.angle = angle % 360 # permet de ramener l'angle antre 0 et 360
        
    def __str__(self):
        # return str(self.angle) + ' degrés'
        return '{} degrés'.format(self.angle)
    
    def ajoute(self, other):
        return Angle((self.angle + other.angle) % 360)
    
    # attention angle dans le module math (cos, sin) en radian !
    def cos(self):
        return cos(self.angle * pi / 180)
    
    def sin(self):
        return sin(self.angle * pi / 180)
        
angle1 = Angle(60)
print(angle1.cos())
print(angle1.sin())
angle2 = Angle(45)
print(angle1.ajoute(angle2))
