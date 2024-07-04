import os

class TemporaryFile:

    def __init__(self,filename) -> None:
        self.filename = filename
        with open(self.filename,'w') as fin:
            fin = fin.write
        print('file created')
    def __del__(self):
        os.remove(self.filename)
        print('file is deleted')

f1 = TemporaryFile('test.txt')