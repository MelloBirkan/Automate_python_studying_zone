def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        return 'Error: You tried to divide by zero.'

def how_many_cats():
    print('How many cats do you have?')
    numCats = input()
    try:
        if int(numCats) > 0:
            print('Meow ' * int(numCats))
        else:
            print("You don't have cats")
    except ValueError:
        print("You didn't enter a number.")

how_many_cats()
print(div42by(2))
print(div42by(12))
print(div42by(0))
