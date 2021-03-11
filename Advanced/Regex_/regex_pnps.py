#Regex
print("***Regex***")
print("*Matching the beginning of a string*")

print("""import re

pattern = r'123'
string = '123aremynumbers123'
re.match(pattern,string)
mat = re.match(pattern,string)
print("re.match(pattern,string):",re.match(pattern,string))
print("mat.group():",mat.group())
""")
import re

pattern = r'123'
string = '123aremynumbers321'
re.match(pattern,string)
mat = re.match(pattern,string)
print("re.match(pattern,string):",re.match(pattern,string))
print("mat.group():",mat.group())

string = 'This device costs an amount of $32. It is an import'
pattern = r'amount\D+\d+'
print("\nstring:",string)
print("pattern:",pattern)
print("re.match(pattern,string):",re.match(pattern,string))
#match is done at the beginning, search is used instead
print("re.search(pattern,string):",re.search(pattern,string))
print("re.search(pattern,string).group():",re.search(pattern,string).group())

string = "\\t123blabla" # here the backslash is escaped, so there's no tab, just '\' and 't'
pattern = r'\\t123' # this will match \t (escaping the backslash) followed by 123
print("""\nstring = "\\t123blabla"
pattern = r'\\t123'""")
#matches '\t123'
print("re.match(pattern,string):",re.match(pattern,string))
print("re.match(pattern,string).group():",re.match(pattern,string).group())
print("re.search(pattern,string):",re.search(pattern,string))
print("re.search(pattern,string).group():",re.search(pattern,string).group())

pattern = r'\t123'
#no match since there is a space before 123
print()
print("re.match(pattern,string):",re.match(pattern,string))
#print("re.match(pattern,string).group():",re.match(pattern,string).group())
#AttributeError: 'NoneType' object has no attribute 'group'
print("re.search(pattern,string):",re.search(pattern,string))
#print("re.search(pattern,string).group():",re.search(pattern,string).group())
print()

#this shows how match is done at the beginning
match = re.match(r'(123)','abc123combination')
print("""match = re.match(r'(123)','abc123combination')""")
print("match is None:",match is None)

match = re.search(r'(123)','abc123combination')
print("""match = re.search(r'(123)','abc123combination')""")
print("match.group():",match.group())

string = '123abc123def123ghi'
pattern = r'123'
print("""\nstring = '123abc123def123ghi'
pattern = r'123'""")
print("re.match(pattern,string):",re.match(pattern,string))
print("re.match(pattern,string):",re.match(pattern,string).group())

print("re.search(pattern,string):",re.search(pattern,string))
print("re.search(pattern,string):",re.search(pattern,string).group())

print("re.findall(pattern,string):",re.findall(pattern,string))

print("\n*Searching*")
print("""pattern = r"(your base)" 
sentence = "All your base are belong to us. sample sentence" """)
pattern = r"(your base)"
sentence = "All your base are belong to us."
print("re.search(pattern, sentence):",re.search(pattern, sentence))
print("re.search(pattern, sentence).group():",re.search(pattern, sentence).group())
print(""" re.search(r"(belong.*)", sentence):""", re.search(r"(belong.*)", sentence))


print("\nSearch at the beginning")
print("You search at the beginning using (^) sign")
print("""re.search(r"^123", "123zzb"):""",re.search(r"^123", "123zzb"))
print("""re.search(r"^123", "123zzb").group():""",re.search(r"^123", "123zzb").group())


print("""\nre.search(r"^123", "aa123zzb"):""",re.search(r"^123", "aa123zzb"))
print("""\nre.search(r"^123", "aa123zzb"):""",re.search(r"^123", "aa123zzb"))

print("\nSearch at the end")
print("You search at the end using ($) sign")
print("""re.search(r"123$", "abd123"):""",re.search(r"123$", "abd123"))

print("\nSearch both")
print("You combine the signs (^,$)")
print("""re.search(r"^123$", "abd123"):""",re.search(r"^123$", "abd123"))
print("""re.search(r"^123$", "123"):""",re.search(r"^123$", "123"))

print("\n*Precompiled patterns*")
precompiled_pattern = re.compile(r'(\d+)')
matches = precompiled_pattern.search("The answer is 41!")
print("""precompiled_pattern = re.compile(r'(\d+)')
matches = precompiled_pattern.search("The answer is 41!") 
""")
print("matches.group():",matches.group())
matches = precompiled_pattern.search("The answer is 42!")
print("matches.group():",matches.group())

print("\n*Flags*")
print("""For some special cases we need to change the behavior of the Regular Expression, this is done using ﬂags. Flags can be set in two ways, through the flags keyword or directly in the expression.""")
print("\nFlags keyword")
print("""m = re.search("b", "ABC")  """)
m = re.search("b", "ABC")
print("m is None:",m is None)
print("""m = re.search("b", "ABC", flags=re.IGNORECASE)""")
m = re.search("b", "ABC", flags=re.IGNORECASE)
print("m.group():",m.group())
print("""\nm = re.search("a.b", "A\\nBC", flags=re.IGNORECASE) """)
m = re.search("a.b", "A\nBC", flags=re.IGNORECASE)
print("m is None:",m is None)
print("""m = re.search("a.b", "A\\nBC", flags=re.IGNORECASE|re.DOTALL) """)
m = re.search("a.b", "A\nBCab", flags=re.IGNORECASE|re.DOTALL)
print("m.group():",m.group())


print("\nCommon Flags")
print("FLAG\t\t\t\t\tSHORT DESCRIPTION")
print("""re.IGNORECASE, re.I \tMakes the pattern ignore the case 
re.DOTALL, re.S \t\tMakes . match everything including newlines 
re.MULTILINE, re.M \t\tMakes ^ match the begin of a line and $ the end of a line 
re.DEBUG \t\t\t\tTurns on debug information""")
print("\nInline Flags")
print("""From the docs:
(?iLmsux) (One or more letters from the set 'i', 'L', 'm', 's', 'u', 'x'.)
The group matches the empty string; the letters set the corresponding ﬂags: re.I (ignore case), re.L (locale dependent), re.M (multi-line), re.S (dot matches all), re.U (Unicode dependent), and re.X (verbose), for the entire regular expression. This is useful if you wish to include the ﬂags as part of the regular expression, instead of passing a ﬂag argument to the re.compile() function.
*Note that the (?x) ﬂag changes how the expression is parsed. It should be used ﬁrst in the expression string, or after one or more whitespace characters. If there are non-whitespace characters before the ﬂag, the results are undeﬁned.""")


print("\n*Replacing*")
print("Replacements can be made on strings using re.sub.")
print("Replacing Strings")
print("""re.sub(r"t[0-9][0-9]",'foo','my name t13 is t44 what t99 ever t44')""")
print(re.sub(r"t[0-9][0-9]",'foo','my name t13 is t44 what t99 ever t44'))
print("""re.sub(r"t[0-9]",'foo','my name t13 is t44 what t99 ever t44')""")
print(re.sub(r"t[0-9]",'foo','my name t13 is t44 what t99 ever t44'))
print("""re.sub(r"t\d+",'foo','my name t13 is t44 what t99 ever t44')""")
print(re.sub(r"t\d+",'foo','my name t13 is t44 what t99 ever t44'))
print("\nUsing group references")
print("""re.sub(r"t([0-9])([0-9])", r"t\\2\\1", "t13 t19 t81 t25")""")
print(re.sub(r"t([0-9])([0-9])", r"t\2\1", "t13 t19 t81 t25"))

print("""However, if you make a group ID like '10', this doesn't work: \\10 is read as 'ID number 1 followed by 0'. So you have to be more speciﬁc and use the \\g<i> notation:""")
print("""re.sub(r"t([0-9])([0-9])",r"t\g<2>\g<1>","t13 t19 t81 t25")""")
print(re.sub(r"t([0-9])([0-9])",r"t\g<2>\g<1>","t13 t19 t81 t25"))

print("\nUsing a replacement function")
items = ["zero","one","two","three"]
print("items:",items)
print("""re.sub(r"a\[([0-3])\]",lambda match:items[int(match.group(1))],"Items: a[0], a[1], something, a[2], a[3]")""")
print(re.sub(r"a\[([0-3])\]",lambda match:items[int(match.group(1))],"Items: a[0], a[1], something, a[2], a[3]"))

print("\n*Find All Non-Overlapping Matches*")
print("""re.findall(r"[0-9]{2,3}", "some 1 text 12 is 945 here 4445588899")""")
print(re.findall(r"[0-9]{2,3}", "some 1 text 12 is 945 here 4445588899"))

print("""\n*Note that the r before "[0-9]{2,3}" tells python to interpret the string as-is; as a "raw" string.
You could also use re.finditer() which works in the same way as re.findall() but returns an iterator with SRE_Match objects instead of a list of strings:""")

print("""\nresults = re.finditer(r"([0-9]{2,3})", "some 1 text 12 is 945 here 4445588899")""")
results = re.finditer(r"([0-9]{2,3})", "some 1 text 12 is 945 here 4445588899")
print(results)
#<callable_iterator object at 0x000000F5A0E8AD68>
for res in results:
    print(res.group(0))

print("\n*Checking for allowed characters*")
print("If you want to check that a string contains only a certain set of characters, in this case a-z, A-Z and 0-9, you can do so like this,")

print("""\ndef is_allowed(string):
    charRegex = re.compile(r"[^a-zA-Z0-9.]")
    string = charRegex.search(string)
    return not bool(string)
""")
def is_allowed(string):
    charRegex = re.compile(r"[^a-zA-Z0-9.]")
    string = charRegex.search(string)
    return not bool(string)

print("is_allowed('abyzABYZ0099'):",is_allowed('abyzABYZ0099'))
print("is_allowed(\"#*@#$%^\")",is_allowed("#*@#$%^"))
print("You can also adapt the expression line from [^a-zA-Z0-9.] to [^a-z0-9.], to disallow uppercase letters")

print("\n*Splitting a string using regular expressions*")
print("You can also use regular expressions to split a string.")
data = re.split(r"\s+",'James 94 Samantha 417 Scarlett 74')
print("""data = re.split(r"\s+",'James 94 Samantha 417 Scarlett 74')""")
print("data:",data)

print("\n*Grouping*")

print("Grouping is done with parentheses. Calling group() returns a string formed of the matching parenthesized subgroups.")

print("""match.group() # Group without argument returns the entire match found # Out: '123' 
match.group(0) # Specifying 0 gives the same result as specifying no argument # Out: '123
""")

sentence = "This is a phone number +2547-11-22-333-444"
pattern = r'.*(phone).*?([\d+-]+)'
match = re.match(pattern,sentence)
print("""sentence = "This is a phone number +2547-11-22-333-444"
pattern = r'.*(phone).*?([\d+-]+)'
match = re.match(pattern,sentence)
""")
print("match.group():",match.group())
print("match.group(0):",match.group(1))
print("match.group(1):",match.group(1))
print("match.group(2):",match.group(2))
print("match.group(1,2):",match.group(1,2))

print("\nNamed Groups")
match = re.search(r"My name is (?P<name>[A-Za-z ]+)",' My name is John Smith')
print("""match = re.search(r"My name is (?P<name>[A-Za-z ]+)",' My name is John Smith')""")
print("match.group():",match.group('name'))
print("match.group(1):",match.group(1))

match = re.search(r"My name is (?P<name>[A-Za-z]+)",' My name is John Smith')
print("""match = re.search(r"My name is (?P<name>[A-Za-z]+)",' My name is John Smith')""")
print("match.group():",match.group('name'))
print("match.group(1):",match.group(1))

print("Creates a capture group that can be referenced by name as well as by index.")

print("\nNon-capturing groups")
print("""Using (?:) creates a group, but the group isn't captured. This means you can use it as a group, but it won't pollute your "group space".""")

print("""re.match(r"(\d+)(\+(\d+))?",'11+22').groups():""",re.match(r"(\d+)(\+(\d+))?",'11+22').groups())
print("""re.match(r"(\d+)(?:\+(\d+))?",'11+22').groups():""",re.match(r"(\d+)(?:\+(\d+))?",'11+22').groups())

print("\n*Escaping Special Characters*")
print("Special characters (like the character class brackets [ and ] below) are not matched literally:")
match = re.search(r"[b]","a[b]c")
print("""match = re.search(r"[b]","a[b]c")""")
print("match.group():",match.group())
match = re.search(r"\[b\]","a[b]c")
print("match.group():",match.group())

print("\nThe re.escape() function can be used to do this for you:")
print("re.escape('a[b]c'):",re.escape('a[b]c'))
print("match = re.search(re.escape('a[b]c'), 'a[b]c')")
match = re.search(re.escape('a[b]c'), 'a[b]c')
print("match.group():",match.group())
print("\nThe re.escape() function escapes all special characters, so it is useful if you are composing a regular expression based on user input:")

username = 'A.C.'  # suppose this came from the user
print("re.findall(r'Hi {}!'.format(username), 'Hi A.C.! Hi ABCD!'):",re.findall(r'Hi {}!'.format(username), 'Hi A.C.! Hi ABCD!') )
# Out: ['Hi A.C.!', 'Hi ABCD!']
print("re.findall(r'Hi {}!'.format(re.escape(username)), 'Hi A.C.! Hi ABCD!'):",re.findall(r'Hi {}!'.format(re.escape(username)), 'Hi A.C.! Hi ABCD!'))


print("\n*Match an expression only in speciﬁc locations*")
print("""Often you want to match an expression only in speciﬁc places (leaving them untouched in others, that is). Consider the following sentence:
    An apple a day keeps the doctor away (I eat an apple everyday).
Here the "apple" occurs twice which can be solved with so called backtracking control verbs which are supported by the newer regex module. The idea is:
    forget_this | or this | and this as well | (but keep this)
With our apple example, this would be:""")
#import regex as reg
#string = "An apple a day keeps the doctor away (I eat an apple everyday)"
#rx = re.compile(r'''
#   \([^()]*\) (*SKIP)(*FAIL)  # match anything in parentheses and "throw it away"
#    |                          # or
#    apple                      # match an apple
#    ''', re.VERBOSE)
#apples = rx.findall(string)
#print(apples)
#ModuleNotFoundError: No module named 'regex'

print("\nUpdate to have the newer module regex\nand uncomment the source code for it to work...")

#print("""This matches "apple" only when it can be found outside of the parentheses.
#Here's how it works:
#While looking from left to right, the regex engine consumes everything to the left, the (*SKIP) acts as an "always-true-assertion". Afterwards, it correctly fails on (*FAIL) and backtracks. Now it gets to the point of (*SKIP) from right to left (aka while backtracking) where it is forbidden to go any further to the left. Instead, the engine is told to throw away anything to the left and jump to the point where the (*SKIP) was invoked.""")

print("\n*Iterating over matches using `re.ﬁnditer`*")
print("You can use re.finditer to iterate over all matches in a string. This gives you (in comparison to re.findall extra information, such as information about the match location in the string (indexes):")

text = "You can try to find an ant in this string"
pattern = 'an?\w' #find 'an' either with or without a following word character
for match in re.finditer(pattern,text):
    #start index of match (integer)
    start = match.start()
    #final index of match (integer)
    end = match.end()
    #complete match (string)
    group = match.group()
    #print match
    print("Match '{}' found at: [{},{}]".format(group,start,end))


