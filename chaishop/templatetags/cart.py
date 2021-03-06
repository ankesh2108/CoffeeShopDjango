from django import template

register = template.Library()

@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys=cart.keys()
    for id in keys:
        try:
            int_val = int(id)
            if int_val == product.id:
                return cart.get(id)
        except ValueError:
            print("Failure w/ value ")

    return 0
@register.filter(name='total')
def total(product,cart):
    quantity=cart_quantity(product,cart)
    return quantity*product.price


@register.filter(name="total_price")
def total_price(product,cart):
    sum=0
    for p in product:
        sum=sum+total(p,cart)

    return sum


@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:

        try:
            int_val = int(id)
            if int_val == product.id:
                return True
        except ValueError:
            print("Failure w/ value ")

    return False
     