# This program calculates the amount of toilet paper required during quarantine

def getDigit (question):
    while True:
        answer = input(question)
        if answer.isdigit():
            return int(answer)
        else:
            print("Please enter a number")

def getPositiveDigit (question):
    while True:
        answer = getDigit(question)
        if answer <= 0:
            print("Enter a number greater than 1")
        else:
            return answer


poops = getDigit("How many poops per day?: ")
wipes = getDigit("How many wipes per poop?: ")
sheets = getDigit("How many sheets per wipe?: ")
poops_total = poops * (wipes * sheets)

pees = getDigit("How many times do you pee per day?: ")
sheets1 = getDigit("How many sheets per pee?: ")
pees_total = pees * sheets1

people = getPositiveDigit("How many people in your household?: ")
sheets_total = people * (pees_total + poops_total)

roll = getPositiveDigit("How many sheets per roll of toilet paper?: ")

quarantine = getDigit("How many days quarantine?: ")

total = int((sheets_total * quarantine) / roll)
print("You should buy", total, "rolls of toilet paper")
