from cars import Car


car1 = Car("Toyota", "Corolla", 2015, 80000)
car2 = Car("Honda", "Civic", 2017, 60000)
car3 = Car("Ford", "Focus", 2018, 45000)
car4 = Car("BMW", "3 Series", 2020, 30000)
car5 = Car("Audi", "A4", 2019, 35000)
car6 = Car("Mercedes", "C-Class", 2021, 15000)
car7 = Car("Hyundai", "Elantra", 2016, 70000)
car8 = Car("Nissan", "Altima", 2014, 90000)
car9 = Car("Kia", "Optima", 2013, 100000)
car10 = Car("Chevrolet", "Malibu", 2022, 5000)

cars = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]

for car in cars:
    print(f"Name: {car.name}, Model: {car.model}, Year: {car.year}, Kilometers: {car.km}")


# Car class
# class atribute total_cars
# object atribute name, model, year, km
# method drive(distance) + km
# str method print(name, model, year, km)














































