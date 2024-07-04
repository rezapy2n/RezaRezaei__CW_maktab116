class Vehicle:
    def __init__(self, make, model, year):
        
        self._make = make
        self._model = model
        self._year = year

    def display_details(self):
        
        print(f"Make: {self._make}, Model: {self._model}, Year: {self._year}")

    def set_make(self, make):
        
        if isinstance(make, str) and make.strip():
            self._make = make
        else:
            print("Invalid make. Make must be a non-empty string.")

    def get_make(self):
        
        return self._make

    def set_model(self, model):
        
        if isinstance(model, str) and model.strip():
            self._model = model
        else:
            print("Invalid model. Model must be a non-empty string.")

    def get_model(self):
        
        return self._model

    def set_year(self, year):
       
        if isinstance(year, int) and year > 0:
            self._year = year
        else:
            print("Invalid year. Year must be a positive integer.")

    def get_year(self):
        
        return self._year


my_vehicle = Vehicle("hyundai", "genesis", 2011)
my_vehicle.display_details()
my_vehicle.set_make("Honda")
my_vehicle.set_year(2023)
print(f"Updated make: {my_vehicle.get_make()}, Updated year: {my_vehicle.get_year()}")
