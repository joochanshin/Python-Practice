# Python-Practice, the The Mandelbrot Set

A small project to print out X and _ in relation to the Mandelbrot set.

## A small explanation

The Mandelbrot set starts with a recursively defined formula. In this formula,
c, is a **Complex Number**.

<p align="center">
  <img width="400" height="100" src="https://github.com/joochanshin/Python-Practice/blob/master/SC/SS5.png">
</p>

The Mandelbrot set is the set of numbers c such that for every n we know
that

<p align="center">
  <img width="200" height="100" src="https://github.com/joochanshin/Python-Practice/blob/master/SC/SS6.png">
</p>

Because it would not be very possible to check every possible number, the program checks through numbers from 0 to 10.

When we insert *1* as the value for c, we get a very large number which is obviously not less than or equal to 2; however when we insert the number *-1* we get the value 0. So below is a table for a few number combinations:

<p align="center">
  <img width="600" height="200" src="https://github.com/joochanshin/Python-Practice/blob/master/SC/SS1.png">
</p>

Knowing this, I came up with a recursive function 

```
def z(n, c):
    if n == 0:
        return Complex(0, 0)
    else:
        tmp = z(n - 1, c)
        return tmp * tmp + c
```
not knowing if __pow__ will work. 

## Some problems

Originally I had
```
 if n == 0:
        return 0
```
to break the resursive function; however, the program was written in a way that it is expected a Complex object to be returned, rather than an integer. 

Other problems were small typos in the operator overloads like in the __add__ method for example would have
```
return Complex((a + x) + (b + y))
```
instead of the now working line of code
```
return Complex((a + x), (b + y))
```
The difference being that the first line of code would give the constructor only one argument, as opposed to two. 

The other strange error that I ran into was in the __abs__ method. Some of these numbers become very large so I was getting the TypeError stating that this long int is too large to convert into a float... So then I added a Decimal wrap

```
return sqrt((Decimal(x) ** 2) + (Decimal(y) ** 2))
```
and was working for a bit; however, I then had to change the **X** and **Y** inputs to floats to account for the step iterator, and then had to wrap the values into str before the Decimal leading to this line of code:
```
return sqrt((Decimal(str(x)) ** 2) + (Decimal(str(y)) ** 2))
```

Last error I was getting was actually getting the forloop to work. This was quite an easy fix. 

```
str_ = ""
        xx = np.arange(float(startX), float(stopX) + con, s)
        yy = np.arange(float(stopY),  float(startY) - con, s * -1)
        for y in yy:
            '''print y'''
            for x in xx:
                '''print x'''
                if accept_c(Complex(x, y)):
                    str_ += "X"
                else:
                    str_ += "_"
            str_ += "\n"
        print str_
```
The forloop would keep running inbetween 2 and 3, so I made an if statement earlier giving the lines of code:
```
if s == 1:
    con = 1
```
The forloop would only print out the numbers 2 through 3 if it is 1, which should include the last bit for a test I ran.

## Finished Project

This is the finished project:
<p align="center">
  <img width="600" height="800" src="https://github.com/joochanshin/Python-Practice/blob/master/SC/SS4.png">
</p>
The numbers you see were to debug the earlier forloop problem.

<p align="center">
  <img width="600" height="700" src="https://github.com/joochanshin/Python-Practice/blob/master/SC/SS3.png">
</p>


This is what the finished project looks like.
