import turtle as tu
a = 1
tu.left(90)
while 1:
    for i in range (1,361):
        tu.forward(a)
        tu.left(1)
    for n in range (1,361):
        tu.forward(a)
        tu.right(1)
    a = a + 0.15
