power = True
expresso = 20
latte = 30
cappuccino = 40
water = 200
milk = 200
coffee = 200


def report(money):
    print(f"water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: {money} RS")


def tran(ctype):
    global water, milk, coffee
    if ctype == 'espresso':
        csum = 10 * int(input("Number of Ten Rupee coins : "))
        csum += 5 * int(input("Number of Five Rupee coins : "))
        if csum >= expresso:
            if water >= 50 and coffee >= 18:
                water = water - 50
                coffee = coffee - 18
                print("processed successfully")
            else:
                report(csum)
                print("Insufficient ingredients")
            if csum > expresso:
                print(f"Amount refunded after payment {(csum - expresso)}")
        else:
            print(f"Cost of an expresso is {expresso}RS")
            print("Insufficient Payment, Amount Refunded")
    elif ctype == 'latte':
        csum = 10 * int(input("Number of Ten Rupee coins : "))
        csum += 5 * int(input("Number of Five Rupee coins : "))
        if csum >= latte:
            if water >= 200 and coffee >= 24 and milk >= 150:
                water = water - 200
                coffee = coffee - 24
                milk = milk - 150
                print("processed successfully")
            else:
                report(csum)
                print("Insufficient ingredients")
            if csum > latte:
                print(f"Amount refunded after payment {(csum - expresso)}")
        else:
            print(f"Cost of a latte is {latte}RS")
            print("Insufficient Payment, Amount Refunded")
    elif ctype == 'cappuccino':
        csum = 10 * int(input("Number of Ten Rupee coins : "))
        csum += 5 * int(input("Number of Five Rupee coins : "))
        print(csum)
        if csum >= cappuccino:
            if water >= 200 and coffee >= 18 and milk >= 100:
                water = water - 250
                coffee = coffee - 24
                milk = milk - 100
                print("processed successfully")
            else:
                report(csum)
                print("Insufficient ingredients")
            if csum > cappuccino:
                print(f"Amount refunded after payment {(csum - expresso)}")
        else:
            print(f"Cost of a cappuccino is {cappuccino}RS")
            print("Insufficient Payment, Amount Refunded")


while power:
    print("What would you like? (espresso/latte/cappuccino):")
    tran(str(input()))
    if int(input("To turn off press 0 or Press any number to continue: ")) == 0:
        break
    else:
        continue
