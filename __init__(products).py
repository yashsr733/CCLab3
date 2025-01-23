from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data):
        # Static method to load data into a Product object
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    # List all products and return them as Product objects
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    # Get a single product by its ID
    return Product.load(dao.get_product(product_id))


def add_product(product: dict):
    # Add a new product
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    # Update the quantity of a product
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
