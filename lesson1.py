# Носов С.Е. 29.11.2020

# Exesize 1400

i = 1
f = 2.7
str = "abc"
b = True
print(i)
print(f)
print(str)
print(b)
print(type(i))
print("Insert number: ")
a = int(input())
print("Insert another number: ")
b = int(input())
print(f"a + b = {a+b}")
print("a + b = {}".format(a+b))

# Exesize 2

print("Insert time (sec): ")
a = int(input())
hour = a // 3600
min = (a - 3600 * hour) // 60
sec = a % 60
print(f"You time equals = {hour:02} : {min:02} : {sec:02}")

# Exesize 3

print("Insert time number n not start at '0': ")
n = input();
nn = f"{n}{n}"
nnn = f"{n}{n}{n}"
num = int(n) + int(nn) + int(nnn)
print(f"Number n + nn + nnn equals = {num}")

# Exesize 4

print("Insert time number n: ")
n = int(input())
maxDigit = 0
while n != 0:
    localD = n % 10
    n = (n - localD) / 10
    if maxDigit < localD:
        maxDigit = localD
print(int(maxDigit))

# Exesize 5

print("Insert your profit: ")
profit = int(input())
print("Insert your loss: ")
loss = int(input())
blc = profit - loss
if blc > 0:
    print(f"You balance = {blc:9.2f} your profitability = {profit/loss: 6.3f}")
    print("How many employees do you have in your company:")
    empNum = int(input())
    print(f"Average profit per employee = {blc/empNum: 6.2f}")
elif blc == 0:
    print("Sorry, your balans equals zero")
else:
    print(f"Sorry, your balans equals {blc:9.2f}")

# Exesize 6

a = 0
b = 0
percentOfDis = 10
while b <= a:
    print("Insert you distanсe before training: ")
    a = int(input())
    if a < 0:
        print("Distanсe before training must be > 0")
    print("Insert you distanсe after training: ")
    b = int(input())
    if b < a:
        print("Distanсe after training must be ge than before. Try again.")
trainingDis = a
numDay = 1
cr = True
while cr:
    print(f"At day {numDay} you running {trainingDis: 6.2f} km")
    trainingDis = trainingDis * (1 + percentOfDis / 100)
    numDay += 1
    if trainingDis > b:
        print(f"At day {numDay} you running {trainingDis: 6.2f} km")
        print(f"On {numDay}-th day you running > {b} km.")
        cr = False