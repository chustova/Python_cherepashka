import turtle as tu
import numpy
a = 3
tu.penup()
tu.forward(10)
tu.pendown()
for a in range (3,11):
    tu.left(180-(180*(a-2)/(2*a)))
    tu.forward(a*10)
    k = a
    while k > 1:
        tu.left(180-(180*(a-2)/a))
        tu.forward(a*10)
        k = k - 1
    tu.right(180*(a-2)/(2*a))
    tu.penup()
    tu.forward(((10 / (2 * numpy.sin((360 / (2 * a))/57.3)))))
    tu.pendown()
    a = a + 1

