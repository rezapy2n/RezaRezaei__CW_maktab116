class Laptop:
    def __init__(self, brand, ram, storage):
        self._brand = brand
        self._ram = ram
        self._storage = storage

    
    def get_brand(self):
        return self._brand

    def get_ram(self):
        return self._ram

    def get_storage(self):
        return self._storage

    
    def set_brand(self, brand):
        if isinstance(brand, str) and brand.strip():
            self._brand = brand
        else:
            print("Brand must be a non-empty string.")

    def set_ram(self, ram):
        if isinstance(ram, int) and ram > 0:
            self._ram = ram
        else:
            print("RAM must be a positive integer.")

    def set_storage(self, storage):
        if isinstance(storage, int) and storage > 0:
            self._storage = storage
        else:
            print("Storage must be a positive integer.")

    
    def display_specifications(self):
        print(f"Brand: {self._brand}")
        print(f"RAM: {self._ram} GB")
        print(f"Storage: {self._storage} GB")



laptop1 = Laptop("asus", 32, 1024)
laptop1.display_specifications()


laptop1.set_brand("HP")
laptop1.set_ram(16)
laptop1.set_storage(1024)
laptop1.display_specifications()
