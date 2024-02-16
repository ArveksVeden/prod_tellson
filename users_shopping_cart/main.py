def solve(n, products, t, actions):
    cart = {}
    
    for product, quantity in products:
        cart[product] = int(quantity)
    
    for action, product in actions:
        if action == "+":
            cart[product] = cart.get(product, 0) + 1
        elif action == "-":

            if product in cart and cart[product] > 0:
                cart[product] -= 1

    sorted_cart = sorted(cart.items())
    
    return sorted_cart

n = int(input())
products = []

for i in range(n):
    products.append(input().split())
    
t = int(input())
actions = []

for i in range(t):
    actions.append(input().split()) 

for product, quantity in solve(n, products, t, actions):
    if quantity != 0:
        print(product, quantity)
