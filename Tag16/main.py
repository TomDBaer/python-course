from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# init systems
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

items = menu.get_items()


def coffee():
    machine_operating = True
    while machine_operating:
        order = input(f"Hey there, please input your order. ({items}): ").lower()

        if order == "off":
            machine_operating = False
        elif order == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            has_resource = coffee_maker.is_resource_sufficient(menu.find_drink(order))
            if has_resource:
                cost = menu.find_drink(order).cost
                has_money = money_machine.make_payment(cost)
                if has_money:
                    coffee_maker.make_coffee(menu.find_drink(order))


coffee()
