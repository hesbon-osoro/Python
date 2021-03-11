#Indexing, Slicing and Matrixes
lang = ('Java','Python','Swift')
web = ('HTML','CSS','JavaScript')
full_stac = lang, web
print("lang: ",lang)

print("%s"%'\n*indexing*'.title())
print("lang[2]:",lang[2]) #Offsets start at zero
print("lang[-3]:",lang[-3]) #Negative: count from the right

print("%s"%'\n*slicing*'.title())
print("lang[1:]:-",lang[1:]) #Slicing fetches sections

print("%s"%'\n*matrixes*'.title())
print("full_stac: ",full_stac)
print("full_stac[0]: ",full_stac[0])
print("full_stac[1]: ",full_stac[1])
print("full_stac[0][1]: ",full_stac[0][1]) #Matrixes
print("full_stac[1][1]: ",full_stac[1][1]) #Matrixes