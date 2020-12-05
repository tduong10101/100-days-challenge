MENU = {
    "espresso": {
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

QUARTER = 0.25
DIME = 0.1
NICLKE = 0.05
PENNY = 0.01

def report(resources):
    for key in resources:
        print(f"{key.title()}: {resources[key]}")


def insert_coins():
    amount = {}
    amount["quarters"] = int(input("how manay quarters?: "))
    amount["dimes"] = int(input("how manay dimes?: "))
    amount["nickes"] = int(input("how manay nickles?: "))
    amount["pennies"] = int(input("how manay pennies?: "))
    return amount


def coin_amount(coins):
    total = coins['quarters']*QUARTER + coins['dimes']*DIME + coins['nickes']*NICLKE + coins['pennies']*PENNY
    return round(total,2)


def process_coins(choice, drink):
    print(f"{choice.title()} cost {drink['cost']}. Please insert coins.")
    inserted_coins = insert_coins()
    inserted_amount = coin_amount(inserted_coins)
    change = round(inserted_amount - drink['cost'],2)
    # check if enough money inserted
    if inserted_amount < drink['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return [False, change]
    else:
        return [True, change]


def check_resources(drink, resources):
    miss_ingr = []
    # check if enough resources
    for key in drink['ingredients']:
        if drink['ingredients'][key] > resources[key]:
            miss_ingr.append(key)
    if len(miss_ingr) > 0:
        if len(miss_ingr) > 1:
            miss_ingr_str = f"{', '.join(miss_ingr[0:-1])} or {miss_ingr[-1]}"
        else:
            miss_ingr_str = miss_ingr[0]
        print(f"Sorry there is not enough {miss_ingr_str} to make your drink.")
        return False
    else:
        return True


def make_coffee(drink, resources):
    for key in drink['ingredients']:
        resources[key] -= drink['ingredients'][key]
    if 'money' in resources:
        resources['money'] += drink['cost']
    else:
        resources['money'] = drink['cost']
    return resources


def coffee_machine(resources):
    choice = (input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if choice == "report":
        report(resources)
    else:
        drink = MENU[choice]
        result, change = process_coins(choice, drink)
        if result:
            result = check_resources(drink, resources)
            if result:
                resources = make_coffee(drink, resources)
                print(f"Enjoy your {choice} ☕.")
                if change > 0:
                    print(f"Here is you change: ${change}")
    return resources


while True:    
    resources = coffee_machine(resources)
