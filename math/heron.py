n = int(input("Enter your Number: "))
x = n

while n - (x*x) > 0.01:
    x = (0.5)*((n/x)+x)

print("Die Wurzel von " + str(n) + " lautet: " + str(x))