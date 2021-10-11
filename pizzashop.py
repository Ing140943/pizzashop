from pizza import Pizza

# This function shows a limitation on tool-assisted
# refactoring in a dynamic language like Python.
#
# When you rename the Pizza getPrice method to get_price,
# does it rename the method here?
# - if no type annotation on the pizza parameter, maybe not
# - if use type annotation ':Pizza' on the parameter, it should

def order_pizza(pizza):
    """Print a description of a pizza, along with its price."""

    # create printable description of the pizza such as
    # "small pizza with muschroom" or "small plain pizza"
    description = pizza.size
    if pizza.toppings:
        description += " pizza with "+ ", ".join(pizza.toppings)
    else:
        description += " plain cheeze pizza"
    print(f"A {description}")
    print("Price:", pizza.getPrice())


if __name__ == "__main__":
    pizza = Pizza('small')
    pizza.addTopping("mushroom")
    pizza.addTopping("tomato")
    pizza.addTopping("pinapple")
    order_pizza(pizza)

    # a plain pizza
    pizza2 = Pizza("medium")
    order_pizza(pizza2)

    # pizza with only one topping
    pizza3 = Pizza("large")
    pizza3.addTopping("seafood")
    order_pizza(pizza3)
