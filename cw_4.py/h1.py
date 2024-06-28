with open('test.txt','r') as fin:
    data = fin.read()
    data_sentences = data.split('.')

    data_sentences_dict = dict()

    for sentence in data_sentences:

        count = 0
        
        for word in sentence.split():
            
            if len(word) > 2:
                count += 1
                
        print()


        data_sentences_dict[sentence] = count

sentence_coount = list(data_sentences_dict.items())

sorted_sentence = sorted(sentence_coount,key = lambda x: x[0],reverse= True)

print(sorted_sentence[0][0],'\nword count= ',sentence_coount[0][1],'\n',len(sentence_coount[0][0]))