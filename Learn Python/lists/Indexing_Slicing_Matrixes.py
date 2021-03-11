#Indexing, Slicing and Matrixes
languages = ['Python','Java','C#','C++']
full_stac = ['Python','Java','C++'],['HTML','CSS','JavaScript']
print("Languages: %s"%languages)
print("%s"%'\n*indexing*'.title())
print("languages[3]:",languages[3]) #Offsets start at zero
print("languages[-3]:",languages[-3]) #Negative: count from the right
print("%s"%'\n*slicing*'.title())
print("languages[2:]:-",languages[2:]) #Slicing fetches sections
print("%s"%'\n*matrixes*'.title())
print("full_stac: ",full_stac)
print("full_stac[0]: ",full_stac[0])
print("full_stac[1]: ",full_stac[1])
print("full_stac[0][1]: ",full_stac[0][1]) #Matrixes
print("full_stac[1][1]: ",full_stac[1][1]) #Matrixes