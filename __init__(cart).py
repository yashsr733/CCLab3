import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        # Using a static method since it doesn't need to access the instance
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    # Fetch cart details for the username
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []

    items = []
    for cart_detail in cart_details:
        # Assuming contents are already in list format (instead of using eval)
        contents = cart_detail['contents']
        
        # Fetch corresponding products for each content
        items.extend(products.get_product(content_id) for content_id in contents)
    
    return items


def add_to_cart(username: str, product_id: int):
    # Add product to the cart
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    # Remove product from the cart
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    # Delete cart for the user
    dao.delete_cart(username)
