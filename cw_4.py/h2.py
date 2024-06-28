def read_write(input_file,output_file):

with open(input_file,'r') as fin:

data = fin.read()

with open(output_file,'a+') as fout:

fout.write(data)
fout.write(' ')

read_write('file1.txt','merged.txt')

read_write('file2.txt','merged.txt')

read_write('file3.txt','merged.txt')