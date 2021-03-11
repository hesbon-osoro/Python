from textblob import TextBlob
mylist = ['Incorret', 'spellin']
corrected_list = []
for word in mylist:
    corrected_list.append(TextBlob(word))
print("Original list:",mylist)
print("Corrected list words are:")
for word in corrected_list:
    print(word.correct(), end=' ')
