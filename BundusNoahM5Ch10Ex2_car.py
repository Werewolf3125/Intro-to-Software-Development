class Car:
    def __init__(self, year_model: str, make: str, speed: int):
        self.year_model: str = year_model
        self.make: str = make
        self.speed: int = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.year_model, self.make, self.speed

