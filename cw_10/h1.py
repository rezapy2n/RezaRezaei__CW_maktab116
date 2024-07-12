class FileReader:
    def __init__(self,fileaddres,mode) -> None:
        self.fileaddres = fileaddres
        self.mode = mode
        self.file = None

    def __enter__(self): 
        self.file = open(self.fileaddres,self.mode)
        return self.file
    
    def __exit__(self,exc_type, exc_value):
        if self.file:
            self.file.close()

        if exc_type is not None:
            print(f'find Error:{exc_value}')  
            return False
        return True  

