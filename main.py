class Beverage:
    def get_description(self):
        raise NotImplementedError

    def get_price(self):
        raise NotImplementedError

class Cacao(Beverage):
    def get_description(self):
        return "Какао"

    def get_price(self):
        return 120
    
class Coffee(Beverage):
    def get_description(self):
        return "Кофе"

    def get_price(self):
        return 100


class BeverageDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage


class TonicDecorator(BeverageDecorator):
    def get_description(self):
        return self.beverage.get_description() + " + тоник"

    def get_price(self):
        return self.beverage.get_price() + 40

class MilkDecorator(BeverageDecorator):
    def get_description(self):
        return self.beverage.get_description() + " + молоко"

    def get_price(self):
        return self.beverage.get_price() + 20


class SyrupDecorator(BeverageDecorator):
    def get_description(self):
        return self.beverage.get_description() + " + сироп"

    def get_price(self):
        return self.beverage.get_price() + 15


latte = SyrupDecorator(MilkDecorator(Coffee()))

cacao_syrop = MilkDecorator(SyrupDecorator(Cacao()))
print(cacao_syrop.get_description())  # Какао + молоко + сироп
print(cacao_syrop.get_price())        

print(latte.get_description())  # Кофе + молоко + сироп
print(latte.get_price())        # 135

espresso_tonic = TonicDecorator(Coffee())

print(espresso_tonic.get_description())  # Кофе + тоник
print(espresso_tonic.get_price())        # 140