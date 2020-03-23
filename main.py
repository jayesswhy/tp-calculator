# this program calculates the amount of toilet paper required during quarantine

# usage
poops = int(input("How many poops per day?: ")) # poops per day
wipes = int(input("How many wipes per poop?: ")) # wipes per poop
sheets = int(input("How many sheets per wipe?: ")) # sheets per wipe
poops_total = poops * (wipes * sheets)

# pees
pees = int(input("How many times do you pee per day?: ")) # pees per day
sheets1 = int(input("How many sheets per pee?: ")) # sheets per pee
pees_total = pees * sheets1

# how many people in household
people = int(input("How many people in your household?: "))
sheets_total = people * (pees_total + poops_total)

# sheets per roll of toilet paper
roll = int(input("How many sheets per roll of toilet paper?: "))

# quarantine period
quarantine = int(input("How many days quarantine?: "))

# how many rolls should you buy for quarantine
total = int((sheets_total * quarantine) / roll)
print ("You should buy", total, "rolls of toilet paper")
