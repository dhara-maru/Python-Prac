class Car:
    make = "Toyota"
    model = "Camry"
    year = 2022

    def start_engine(self):
        return "Vroom!"


car1 = Car()


print("Make:", car1.make)
print("Model:", car1.model)
print("Year:", car1.year)

engine_sound = car1.start_engine()
print(engine_sound)
