Coffee = {
    "espresso": {
        "Ingrediants": {
            "Water": 100,
            "Coffee": 75,
        },
        "Cost": 200,
    },

    "latte": {
        "Ingrediants": {
            "Milk": 100,
            "Water": 100,
            "Coffee": 80,
        },
        "Cost": 250,
    },

    "cappaccino": {
        "Ingrediants": {
            "Milk": 80,
            "Water": 120,
            "Coffee": 85,
        },
        "Cost": 300,
    },
}
Profit = 0
Storage = {
    "Water": 500,
    "Milk": 500,
    "Coffee": 500,
}
Coffee1 = 0
money10 = 0
money20 = 0
money50 = 0
money100 = 0
retrnmony = 0
moneyrecd = 0
mony_cof = 0
On = True
while On == True:
    option = int(input("Enter the (1) Coffee :"))
    if option == 0:
        On = False
    elif option == 1:
        if Storage["Water"] < 100:
            print(f'We Running out Water: {Storage["Water"]}ml')
        elif Storage["Milk"] < 100:
            print(f'We Running out Milk: {Storage["Milk"]}ml')
        elif Storage["Coffee"] < 80:
            print(f'We Running out Coffee: {Storage["Coffee"]}g')
        else:
            Coffe = input(" Pls select your coffee : espresso / latte /cappaccino / report :").lower()
            if Coffe == "latte":
                print("Pls Pay the amount ")
                money10 = int(input("No of 10 rupees :")) * 10
                money20 = int(input("No of 20 rupees :")) * 20
                money50 = int(input("No of 50 rupees :")) * 50
                money100 = int(input("No of 100 rupees :")) * 100
                moneyrecd = money10 + money20 + money50 + money100
                mony_cof = Coffee["latte"]["Cost"]
                if moneyrecd < mony_cof:
                    print(f' You paid {moneyrecd} And it is not enough to buy a {Coffe}')
                else:
                    print("Pls Take ur latte")
                    print("It Consist of")
                    print(f'Water :{Coffee["latte"]["Ingrediants"]["Water"]} ml')
                    print(f'Milk :{Coffee["latte"]["Ingrediants"]["Milk"]} ml')
                    print(f'Coffee :{Coffee["latte"]["Ingrediants"]["Coffee"]} g')
                    print(f'Price :{Coffee["latte"]["Cost"]}₹')
                    Profit += Coffee["latte"]["Cost"]
                    Storage["Coffee"] -= Coffee["latte"]["Ingrediants"]["Coffee"]
                    Storage["Milk"] -= Coffee["latte"]["Ingrediants"]["Milk"]
                    Storage["Water"] -= Coffee["latte"]["Ingrediants"]["Water"]
                    if moneyrecd > mony_cof:
                        print(
                            f'Thanks for visiting You paid {moneyrecd} And remaining {moneyrecd - mony_cof} pls collect b4 u leave.')
                    else:
                        print(f'Pls collect your {Coffe}" have a good day ')
            elif Coffe == "espresso":
                print("Pls Pay the amount ")
                money10 = int(input("No of 10 rupees :")) * 10
                money20 = int(input("No of 20 rupees :")) * 20
                money50 = int(input("No of 50 rupees :")) * 50
                money100 = int(input("No of 100 rupees :")) * 100
                moneyrecd = money10 + money20 + money50 + money100
                mony_cof = Coffee["espresso"]["Cost"]
                if moneyrecd < mony_cof:
                    print(f' You paid {moneyrecd} And it is not enough to buy a {Coffe}')
                else:
                    print("Pls Take ur espresso")
                    print("It Consist of")
                    print(f'Water :{Coffee["espresso"]["Ingrediants"]["Water"]} ml')
                    print(f'Coffee :{Coffee["espresso"]["Ingrediants"]["Coffee"]} g')
                    print(f'Price :{Coffee["espresso"]["Cost"]}₹')
                    Profit += Coffee["espresso"]["Cost"]
                    Storage["Coffee"] -= Coffee["espresso"]["Ingrediants"]["Coffee"]
                    Storage["Water"] -= Coffee["espresso"]["Ingrediants"]["Water"]
                    if moneyrecd > mony_cof:
                        print(
                            f'Thanks for visiting You paid {moneyrecd} And remaining {moneyrecd - mony_cof} pls collect b4 u leave.')
                    else:
                        print(f'Pls collect your {Coffe}" have a good day ')

            if Coffe == "cappaccino":
                print("Pls Pay the amount ")
                money10 = int(input("No of 10 rupees :")) * 10
                money20 = int(input("No of 20 rupees :")) * 20
                money50 = int(input("No of 50 rupees :")) * 50
                money100 = int(input("No of 100 rupees :")) * 100
                moneyrecd = money10 + money20 + money50 + money100
                mony_cof = Coffee["cappaccino"]["Cost"]
                if moneyrecd < mony_cof:
                    print(f' You paid {moneyrecd} And it is not enough to buy a {Coffe}')
                else:
                    print("Pls Take ur cappaccino")
                    print("It Consist of")
                    print(f'Water :{Coffee["cappaccino"]["Ingrediants"]["Water"]} ml')
                    print(f'Milk :{Coffee["cappaccino"]["Ingrediants"]["Milk"]} ml')
                    print(f'Coffee :{Coffee["cappaccino"]["Ingrediants"]["Coffee"]} g')
                    print(f'Price :{Coffee["cappaccino"]["Cost"]}₹')
                    Profit += Coffee["cappaccino"]["Cost"]
                    Storage["Coffee"] -= Coffee["cappaccino"]["Ingrediants"]["Coffee"]
                    Storage["Milk"] -= Coffee["cappaccino"]["Ingrediants"]["Milk"]
                    Storage["Water"] -= Coffee["cappaccino"]["Ingrediants"]["Water"]
                    if moneyrecd > mony_cof:
                        print(
                            f'Thanks for visiting You paid {moneyrecd} And remaining {moneyrecd - mony_cof} pls collect b4 u leave.')
                    else:
                        print(f'Pls collect your {Coffe}" have a good day ')

            elif Coffe == "report":
                if Coffe == "espresso":
                    print("Storage as of now")
                    print(f'Milk :{Storage["Water"]}')
                    print(f'Milk :{Storage["Coffee"]}')
                    print(f'Profit :{Profit}')
                else:
                    print(f'Milk :{Storage["Milk"]}ml')
                    print(f'Milk :{Storage["Water"]}ml')
                    print(f'Milk :{Storage["Coffee"]}g')
                    print(f'Profit :{Profit}₹')

    else:
        print(f' Entered Invalid No .')