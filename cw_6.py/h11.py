Class FileHandler:
    def __init__(self) -> None:
        pass

    @classmethod    
    def read_file(cls,file_location):
        with open(file_location,"r") as fp:
            fp = fp.readline()

            for line in fp:
                return line
        
f1 = FileHandler()
print(f1.read_file("D:/MaktabSharif/W06/CW06/test.txt"))  