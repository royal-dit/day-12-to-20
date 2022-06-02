#                                    Coffee vending Machine

MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# returned_money = 0
#
# def resources_details():
#     water = resources['water']
#     milk = resources['milk']
#     coffee = resources['coffee']
#     return water, coffee, milk
#
#
# def expresso_details():
#     water= MENU["expresso"]['ingredients']['water']
#     coffee = MENU["expresso"]["ingredients"]['coffee']
#     return water,coffee
#
# def latte_details():
#     water= MENU['latte']['ingredients']['water']
#     milk = MENU['latte']['ingredients']['milk']
#     coffee = MENU['latte']['ingredients']['coffee']
#     return water,coffee,milk
#
# def cappuccino_details():
#     water= MENU["cappuccino"]['ingredients']['water']
#     milk = MENU["cappuccino"]['ingredients']['milk']
#     coffee = MENU["cappuccino"]['ingredients']['coffee']
#     return water,coffee,milk
#
# user_input = input("What would you like? (expresso/latte/cappuccino)")
# if user_input == "report":
#     for i in resources:
#         print(i,resources[i])
#
# coin_taken = int(input("Insert the coin: "))
#
# expresso_cost = MENU["expresso"]["cost"]
# latte_cost = MENU["latte"]["cost"]
# cappuccino_cost = MENU["cappuccino"]["cost"]
#
#
#
# if user_input == 'expresso' and coin_taken >= expresso_cost:
#     if coin_taken > expresso_cost:
#         returned_money = coin_taken-expresso_cost
#         print(f"Here is your {returned_money}$ change")
#         print("Enjoy the Expresso ! happy days")
#     else:
#         total_items_left = resources_details() - expresso_details()
#         print("Enjoy the Expresso ! happy days")
#
#
#
#
# if user_input == 'latte' and coin_taken >= latte_cost:
#     if coin_taken > latte_cost:
#         returned_money = coin_taken-latte_cost
#         print(f"Here is your {returned_money}$ change")
#         print("Enjoy the Latte ! happy days")
#     else:
#         print("Enjoy the Latte ! happy days")
#
# if user_input == 'cappuccino' and coin_taken >= cappuccino_cost:
#     if coin_taken > cappuccino_cost:
#         returned_money = coin_taken-cappuccino_cost
#         print(f"Here is your {returned_money}$ change")
#         print("Enjoy the cappuccino ! happy days")
#     else:
#         print("Enjoy the cappuccino ! happy days")

profit = 0

def is_resource_sufficent(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
          print(f"sorry there is not enough  {item}")
          is_enough= False
    return  is_enough


def process_coins():
     total = int(input("Please Insert Coin:"))
     return total

def is_transaction_sucessful(money_recived,drink_cost):
    """ return true os payment is accepted reture false is payment is insufficent """
    if money_recived >= drink_cost:
         change = round(money_recived-drink_cost,2)
         print(f"Here is ${change} in change")
         global  profit
         profit += drink_cost
         return True
    else:
       print("Sorry the money is not enough.money refunded")
       return False

def make_coffee(drink_name,order_ingredients):
    """ deduct the required infgredients from the resouces"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True

while is_on:
    choice = input("What would you like? (expresso/latte/cappuccino):")
    if choice == 'off':
        is_on = False
    elif choice == "report":
        for i in resources:
             print(i,resources[i])
        print((f"Money: ${profit}"))
    else:
        drink  = MENU[choice]
        if is_resource_sufficent(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_sucessful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])











