for x in range(-2, 3):
    for y in range(-2, 3):
        print "x, ", x, "y, ", y
        c1 = Complex(x, y)
        if c1.getImaginary() < 0:
            c1 = Complex(c1.getReal(), c1.getImaginary() * -1)
        c2 = c1.getReal() + c1.getImaginary()
        print accept_c(c2)
        print abs(z(10, c2))
    print "\n"

run = True
print "Welcome to the Mandelbrot Set \nEnter exit at anytime to quit."


while run:
    goFunct = True
    startX = raw_input("Enter start X point (or exit):")
    if startX == "exit":
        break
    stopX = raw_input("Enter stop X point (or exit):")
    if stopX == "exit":
        break
    startY = raw_input("Enter start Y point (or exit):")
    if startY == "exit":
        break
    stopY = raw_input("Enter stop Y point (or exit):")
    if stopY == "exit":
        break
    step = raw_input("Enter step size (or exit):")
    if step == "exit":
        break
    if startX > stopX or \
        startY > stopY or \
        step <= 0:
        goFunct = False
        print "Bad inputs. Could not render."
    if goFunct:
        str = ""
        for x in range(int(startX), int(stopX)+1):
            for y in range(int(stopY), int(startY) -1):
                c4 = Complex(x, y)
                if accept_c(c4) == True:
                    str += "X"
                else:
                    str += "_"
            str += "\n"
        print str

