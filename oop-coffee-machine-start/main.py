from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
choice = menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine = True
while coffee_machine:

    user_choice = input(f"What would you like to have? {choice} ")
    if user_choice == "off":
        coffee_machine = False
    elif user_choice == "report":
        r_report = coffee_maker.report()
        m_report = money_machine.report()
    else:
        order = menu.find_drink(user_choice)
        print(user_choice)
        sufficient_resources = coffee_maker.is_resource_sufficient(order)

        if sufficient_resources:
            payment = money_machine.make_payment(order.cost)

            if payment:
                coffee_maker.make_coffee(order)
        else:
            print(f"sorry there isn't enough {sufficient_resources}")





