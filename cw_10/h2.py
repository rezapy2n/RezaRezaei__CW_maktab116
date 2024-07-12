
class FileReaderIterator:
    def __init__(self,fileaddres) -> None:
        self.fileaddres = fileaddres
        self.mode = 'r'
        self.file = None

    def __enter__(self): 
        self.file = open(self.fileaddres,self.mode)
        return self.file.readlines().__iter__()
    
    def __exit__(self,exc_type, exc_value,exc_traceback):
        if self.file:
            self.file.close()

        if exc_type is not None:
            print(f'find Error:{exc_value}')  
            return False
        return True  



with FileReaderIterator('x.txt') as file:
    while True:
        try:
            print(file.__next__(),end= '')
        except:
            break

