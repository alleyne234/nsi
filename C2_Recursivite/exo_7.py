### IMPORTS ###
import turtle as tt



### CODES ###
def koch(n, l):
    tt.speed(100000)
    if n == 0:
        tt.down()
        tt.forward(l)
        tt.up()
    else:
        koch(n - 1, l / 3) # appel recursif pour tracer un segment
        tt.left(60)
        koch(n - 1, l / 3)
        tt.right(120)
        koch(n - 1, l / 3)
        tt.left(60)
        koch(n - 1, l / 3)

def flocon_koch(n, l):
    tt.left(60)
    koch(n, l)
    tt.right(120)
    koch(n, l)
    tt.right(120)
    koch(n, l)
    tt.right(180)
