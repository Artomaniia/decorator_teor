# Интерфейс
class Strategy:
    def deliver(self, package): 
        pass
# Конкретные реализации
class CourierStrategy(Strategy):
    def deliver(self, package): 
        return f"Доставка {package} курьером"

class DroneStrategy(Strategy):
    def deliver(self, package): 
        return f"Доставка {package} дроном"
# Контекст
class DeliveryService:
    def __init__(self, strategy): 
        self.strategy = strategy
    def send(self, item): 
        print(self.strategy.deliver(item))

        