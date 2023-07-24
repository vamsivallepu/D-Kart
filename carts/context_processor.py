from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            # Get the user's cart
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            # Get the cart items from the user's cart
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            # Loop through the cart items to get the total quantity
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)