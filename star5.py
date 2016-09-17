import turtle as tu
def star (n):
    for i in range (1,n+1):
        tu.forward(50)
        tu.left(180-(180/n))
        tu.forward(50)
star (5)
