def tuple_into_string(tuple):
 return   tuple[0]+ " " +tuple[1]


tuple_list =  [('Hello', 'World'), ('Open', 'AI'), ('GPT', '3')]
a=list(map(tuple_into_string,tuple_list))
print(a)​ 