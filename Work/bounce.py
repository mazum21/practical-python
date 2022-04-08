# bounce.py
#
# Exercise 1.5
height = 100
bounce = 1

while bounce <= 10:
    bounce += 1
    height = height / 5 * 3
    print(round(height, 4))