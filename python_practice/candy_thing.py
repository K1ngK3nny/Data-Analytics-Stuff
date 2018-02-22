candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit",
             "Sweedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

allowance = 5

candyCart = []

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "] " + candy)

for x in range(allowance):
    selected = input("Which candy would you like to bring home? ")
    candyCart.append(candyList[int(selected)])
    print("I brought home with me...", selected)

for candy in candyCart:
    print(candy)
