class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = int(rooms)
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = int(plot)

    def __str__(self):
        return (f"Dom: Adres: {self.address}, Cena: {self.price} PLN, Powierzchnia: {self.area} m2, Pokoje: {self.rooms}, Działka: {self.plot} m2")

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Mieszkanie: Adres: {self.address}, Cena: {self.price} PLN, Powierzchnia: {self.area} m2, Pokoje: {self.rooms}, Piętro: {self.floor}")

dom = House(area=150, rooms=5, price=1100000, address="ul. Mogilna 79/8, Gdańsk", plot=479)

mieszkanie = Flat(area=79, rooms=4, price=970000, address="ul. Narcyzowa 84/5, Gdańsk", floor=5)

print(dom)
print(mieszkanie)