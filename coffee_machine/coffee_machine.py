#A coffee machine that takes in coins and brews coffee with the available resources
from coffee_resources import MENU, resources


def coffee_maker():
    """The whole coffee maker system"""

    # condition for the program to run
    machine_on = True
    while machine_on:
        # prompt the user to input the type of coffee
        coffee = input("What would you be having? cappuccino, espresso, latte: ")
        
        # condition for terminating the program
        if coffee == "off":
            machine_on = False
        # program generates report

        elif coffee == "report":
            for resource in resources:
                if resource == "water":
                    print(f"{resource} = {resources[resource]} ml")
                elif resource == "money":
                    print(f"{resource} = ${resources[resource]}")
                else:
                    print(f"{resource} = {resources[resource]} kg")
        else:

            def check_resources(cof, menu, res):
                """takes in 3 arguments and returns True if menu is less than resources"""
                for i in menu[cof]["ingredients"]:
                    return menu[cof]["ingredients"][i] <= res[i]

            ingredient_list = MENU[coffee]["ingredients"]
            coffee_cost = MENU[coffee]["cost"]

            resource_checker = check_resources(coffee, MENU, resources)

            cash_vault = {"Quarters": 0.25,
                          "Dimes": 0.10,
                          "Nickels": 0.05,
                          "Pennies": 0.01
                          }
            if resource_checker:
                print("insert coins")
                q = int(input("Number of Quarters: ")) * cash_vault["Quarters"]
                d = int(input("Number of Dimes: ")) * cash_vault["Dimes"]
                n = int(input("Number of Nickles: ")) * cash_vault["Nickels"]
                p = int(input("Number of Pennies: ")) * cash_vault["Pennies"]
                amount_paid = (q + d + n + p)

                if amount_paid < coffee_cost:
                    print("sorry that's not enough")
                else:
                    resources["money"] += coffee_cost
                    change = round(amount_paid - coffee_cost, 2)

                    if change == 0:
                        print()
                    else:
                        print(f"Here's your change ${change}")

                    for i in ingredient_list:
                        resources[i] -= ingredient_list[i]
                    print(f"Here's your {coffee} ☕")

            else:
                print("not enough resources")


coffee_maker()