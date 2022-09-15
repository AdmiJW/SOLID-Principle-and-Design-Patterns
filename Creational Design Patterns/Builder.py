
# The product with COMPLEX constructor
class Phone:
    def __init__(self, brand, model, price, color, size, battery_cap):
        self._brand = brand
        self._model = model
        self._price = price
        self._color = color
        self._size = size
        self._battery_cap = battery_cap

    def __str__(self):
        return f"{self._brand} {self._model} {self._price} {self._color} {self._size} {self._battery_cap}"


# Abstract builder
class PhoneBuilder:
    def set_brand(self, brand):
        self.phone._brand = brand
        return self                 # Return self to allow chaining

    def set_model(self, model):
        self.phone._model = model
        return self

    def set_price(self, price):
        self.phone._price = price
        return self

    def set_color(self, color):
        self.phone._color = color
        return self

    def set_battery_cap(self, battery_cap):
        self.phone._battery_cap = battery_cap
        return self

    def get_phone(self):
        return self.phone


# Concrete builders of different existing type of phones
class Nokia3310Builder(PhoneBuilder):
    def __init__(self):
        # Because is a Nokia builder, default arguments is inferred.
        self.phone = Phone('Nokia', '3310', '50', 'Blue', '84x48', '900')

class Iphone10Builder(PhoneBuilder):
    def __init__(self):
        self.phone = Phone("Iphone", "10", "1000", "Black", "143.6x70.9x7.7", "2716")


# Build some phones and modify them
if __name__ == '__main__':
    print( Nokia3310Builder().set_price(300).set_color('Red').get_phone() )
    print( Iphone10Builder().set_price(1999).set_model("11").set_color("Rose Red").get_phone() )