strings_list = ["apple", "banana", "Orange", "grape", "kiwi"]
sorted_upper=list(map(lambda x:x.upper(),strings_list))
print(sorted_upper)
filter_list=list(filter(lambda x: "A" not  in x,sorted_upper))
print(filter_list)