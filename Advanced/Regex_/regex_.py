#Regular Expressions
print('***Regular Expressions***')
print("""A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world. 
The module re provides full support for Perl-like regular expressions in Python. The re module raises the exception re.error if an error occurs while compiling or using a regular expression. 
We would cover two important functions, which would be used to handle regular expressions. Nevertheless, a small thing first: There are various characters, which would have special meaning when they are used in regular expression. To avoid any confusion while dealing with regular expressions, we would use Raw Strings asr'expression'. """)

print('*Basic patterns that match single chars*')
print("""    * a, X, 9, < -- ordinary characters just match themselves exactly. 
    * . (a period) -- matches any single character except newline '\\n' 
    * \\w -- matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. 
    * \\W -- matches any non-word character. 
    * \\b -- boundary between word and non-word 
    * \\s -- matches a single whitespace character -- space, newline, return, tab 
    * \\S -- matches any non-whitespace character. 
    * \\t, \\n, \\r -- tab, newline, return 
    * \\d -- decimal digit [0-9] 
    * ^ = matches start of the string 
    * $ = match the end of the string 
    * \ -- inhibit the "specialness" of a character.""")


print('\n*Compilation flags*')
print("""Compilation flags let you modify some aspects of how regular expressions work. Flags are available in the re module under two names, a long name such as IGNORECASE and a short, one-letter form such as I.""")
print("\nFLAG\t\t\tMEANING")
print("ASCII, A \t\tMakes several escapes like \\w, \\b, \\s and \\d match only on ASCII characters with the respective property. ")
print("DOTALL, S\t\tMake, match any character, including newlines")
print("IGNORECASE, I\tDo case-insensitive matches ")
print("LOCALE, L\t\tDo a locale-aware match ")
print("MULTILINE, M\tMulti-line matching, affecting ^ and $ ")
print("VERBOSE, X  \tEnable verbose REs, which can be organized more cleanly and understandably ")
print("(for ‘extended’)")

print('\n*The Match Function*')
print("""This function attempts to match RE pattern to string with optional flags. 
Here is the syntax for this function- 
    re.match(pattern, string, flags=0) 
Here is the description of the parameters- """)

print("PARAMETER\t\tDESCRIPTION")
print("pattern\t\tThis is the regular expression to be matched. ")
print("string\t\tThis is the string, which would be searched to match the pattern at the beginning of string. ")
print("flags\t\tThis is the string, which would be searched to match the pattern at the beginning of string. ")
print("""\nThe re.match function returns a match object on success, None on failure. We use group(num) or groups() function of match object to get matched expression.""")

print("MATCH OBJECT\t\tDESCRIPTION\n   METHODS")
print("group(num=0)\tThis method returns entire match (or specific subgroup num)")
print("groups()\t\tThis method returns all matching subgroups in a tuple (empty if there weren't any) ")

print('\nExample')
import re

str = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*',str,re.M|re.I)
print("""import re

str = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*',str,re.M|re.I)
""")

if matchObj:
    print("matchObj:", matchObj)
    print("matchObj.group():",matchObj.group())
    print("matchObj.group(0):", matchObj.group(0))
    print("matchObj.group(1):",matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("No match!")

print('\n*The Search Function*')
print("""This function searches for first occurrence of RE pattern within the string, with optional flags. 
Here is the syntax for this function- 
    re.search(pattern, string, flags=0) 
Here is the description of the parameters- """)

print("\nPARAMETER\t\tDESCRIPTION")
print("pattern\t\tThis is the regular expression to be matched")
print("string \t\tThis is the string, which would be searched to match the pattern anywhere in the string.")
print("flags \t\tYou can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.")
print("""\nThe re.search function returns a match object on success, none on failure. We use group(num) or groups() function of match object to get the matched expression. 
""")

print("MATCH OBJECT\t\tDESCRIPTION\n   METHODS")
print("group(num=0)\tThis method returns entire match (or specific subgroup num)")
print("groups()\t\tThis method returns all matching subgroups in a tuple (empty if there weren't any) ")

print('\nExample')
import re

str = "Cats are smarter than dogs"
searchObj = re.match(r'(.*) are (.*?) .*',str,re.M|re.I)
print("""import re

str = "Cats are smarter than dogs"
searchObj = re.match(r'(.*) are (.*?) .*',str,re.M|re.I)
""")

if searchObj:
    print("searchObj:", searchObj)
    print("searchObj.group():",searchObj.group())
    print("searchObj.group(0):", searchObj.group(0))
    print("searchObj.group(1):",searchObj.group(1))
    print("searchObj.group(2):", searchObj.group(2))
else:
    print("Nothing found!")

print("\n*Matching Versus Searching*")
print("""Python offers two different primitive operations based on regular expressions :match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string (this is what Perl does by default). 
""")
print('\nExample')
print("""import re
str = "Cats are smarter than dogs"
matchObj = re.match(r'dogs',str,re.M|re.I)
if matchObj:
    print("match--->matchObj():",matchObj.group())
else:
    print("No match!!")
searchObj = re.search(r'dogs',str,re.M|re.I)
if searchObj:
    print("search--->searchObj():",searchObj.group())
else:
    print("Nothing found!!")
""")
import re
str = "Cats are smarter than dogs"
matchObj = re.match(r'dogs',str,re.M|re.I)
if matchObj:
    print("match--->matchObj():",matchObj.group())
else:
    print("No match!!")
searchObj = re.search(r'dogs',str,re.M|re.I)
if searchObj:
    print("search--->searchObj():",searchObj.group())
else:
    print("Nothing found!!")

print("\n*Search and Replace*")
print("""One of the most important re methods that use regular expressions is sub. 
Syntax 
    re.sub(pattern, repl, string, max=0) 
This method replaces all occurrences of the RE pattern in string with repl, substituting all occurrences unless max is provided. This method returns modified string. 
""")

print('\nExample')
print("""phone = "+254-722-444-888 #This is a phone number"
print("phone:",phone)
#Delete python-style comments
num = re.sub(r'#.*$',"",phone)
print("num:",num)
#remove anything other than digits
num = re.sub(r'\D',"",phone)
print("num:",num)
print("format('+',num): {}{}".format('+',num))
num = re.sub(r'\d',"",phone)
print("num:",num)
""")
phone = "+254-722-444-888 #This is a phone number"
print("phone:",phone)
#Delete python-style comments
num = re.sub(r'#.*$',"",phone)
print("num:",num)
#remove anything other than digits
num = re.sub(r'\D',"",phone)
print("num:",num)
print("format('+',num): {}{}".format('+',num))
num = re.sub(r'\d',"",phone)
print("num:",num)

print('\n*Regular Expression Modifiers: Option Flags*')
print("""Regular expression literals may include an optional modifier to control various aspects of matching. The modifiers are specified as an optional flag. You can provide multiple modifiers using exclusive OR (|), as shown previously and may be represented by one of these- 
""")
print("MODIFIER\t\tDESCRIPTION")
print("re.I \t\tPerforms case-insensitive matching.")
print("re.L \t\tInterprets words according to the current locale. This interpretation affects the alphabetic group (\\w and \\W), as well as word boundary behavior (\\b and \\B). ")
print("re.M \t\tMakes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).")
print("re.S \t\tMakes a period (dot) match any character, including a newline.")
print("re.U \t\tInterprets letters according to the Unicode character set. This flag affects the behavior of \\w, \\W, \\b, \\B. ")
print("""re.X \t\tPermits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker. """)

print("\n*Regular Expression Patterns*")
print("""Except for the control characters, (+ ? . * ^ $ ( ) [ ] { } | \), all characters match themselves. You can escape a control character by preceding it with a backslash. 
The following table lists the regular expression syntax that is available in Python-""")

print("\nPATTERN\t\tDESCRIPTION")
print("^ \t\tMatches beginning of line. ")
print("$ \t\tMatches end of line. ")
print(". \t\tMatches any single character except newline. Using m option allows it to match newline as well.")
print("[...] \tMatches any single character in brackets. ")
print("[^...] \tMatches any single character not in brackets ")
print("re* \tMatches 0 or more occurrences of preceding expression.")
print("re+ \tMatches 1 or more occurrence of preceding expression. ")
print("re? \tMatches 0 or 1 occurrence of preceding expression.")
print("re{ n} \tMatches exactly n number of occurrences of preceding expression.")
print("re{ n,} \tMatches n or more occurrences of preceding expression. ")
print("re{ n, m} \tMatches at least n and at most m occurrences of preceding expression. ")
print("a| b \tMatches either a or b. ")
print("(re) \tGroups regular expressions and remembers matched text.")
print("(?imx) \tTemporarily toggles on i, m, or x options within a regular expression. If in parentheses, only that area is affected.")
print("(?-imx) \tTemporarily toggles off i, m, or x options within a regular expression. If in parentheses, only that area is affected. ")
print("(?: re) \tGroups regular expressions without remembering matched text.")
print("(?imx: re) \tTemporarily toggles on i, m, or x options within parentheses. ")
print("(?-imx: re) \tTemporarily toggles off i, m, or x options within parentheses. ")
print("(?#...) \tComment. ")
print("(?= re) \tSpecifies position using a pattern. Does not have a range.")
print("(?! re) \tSpecifies position using pattern negation. Does not have a range.")
print("(?> re) \tMatches independent pattern without backtracking.")
print("\w \tMatches word characters.")
print("\\W \tMatches nonword characters. ")
print("\\s \tMatches whitespace. Equivalent to [\\t\\n\\r\\f].")
print("\\S \tMatches nonwhitespace. ")
print("\\d \tMatches digits. Equivalent to [0-9].")
print("\\D \tMatches nondigits.")
print("\\A \tMatches beginning of string. ")
print("\\Z \tMatches end of string. If a newline exists, it matches just before newline. ")
print("\\z \tMatches end of string. ")
print("\\G \tMatches point where last match finished. ")
print("\\b \tMatches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets.")
print("\\B \tMatches nonword boundaries. ")
print("\\n, \\t, \tetc. Matches newlines, carriage returns, tabs, etc. ")
print("\\1...\9 \tMatches nth grouped subexpression.")
print("\\10 \tMatches nth grouped subexpression if it matched already. Otherwise refers to the octal representation of a character code.")


print("\n*Regular Expression Examples*")
print("Literal characters ")
print("EXAMPLE\t\tDESCRIPTION")
print("""python\t\tMatch "python" """)

print("\n*Character classes* ")
print("EXAMPLE\t\tDESCRIPTION")
print("""[Pp]ython Match "Python" or "python" """)
print("""rub[ye] Match "ruby" or "rube" """)
print("[aeiou] Match any one lowercase vowel")
print("[0-9] Match any digit; same as [0123456789]")
print("[a-z] Match any lowercase ASCII letter")
print("[A-Z] Match any uppercase ASCII letter")
print("[a-zA-Z0-9] Match any of the above ")
print("[^aeiou] Match anything other than a lowercase vowel ")
print("[^0-9] Match anything other than a digit")

print("\n*Special Character Classes* ")
print("EXAMPLE\t\tDESCRIPTION")
print(". Match any character except newline ")
print("\d Match a digit: [0-9]")
print("\D Match a nondigit: [^0-9]")
print("\s Match a whitespace character: [ \\t\\r\\n\\f] ")
print("\S Match nonwhitespace: [^ \\t\\r\\n\\f]")
print("\w Match a single word character: [A-Za-z0-9_] ")
print("\W Match a nonword character: [^A-Za-z0-9_]")


print("\n*Repetition Cases*")
print("EXAMPLE\t\tDESCRIPTION")
print("ruby? Match \"rub\" or \"ruby\": the y is optional ")
print("ruby* Match \"rub\" plus 0 or more ys ")
print("ruby+ Match \"rub\" plus 1 or more ys ")
print("\d{3} Match exactly 3 digits")
print("\d{3,} Match 3 or more digits ")
print("\d{3,5} Match 3, 4, or 5 digits")

print("\n*Nongreedy Repetition*")
print("This matches the smallest number of repetitions- ")
print("EXAMPLE\t\tDESCRIPTION")
print("<.*> Greedy repetition: matches \"<python>perl>\" ")
print("<.*?> Nongreedy: matches \"<python>\" in \"<python>perl>\" ")

print("\n*Grouping with Parentheses* ")
print("EXAMPLE\t\tDESCRIPTION")
print("\D\d+ No group: + repeats \d")
print("(\D\d)+ Grouped: + repeats \D\d pair")
print("([Pp]ython(, )?)+ Match \"Python\", \"Python, python, python\", etc.")

print("\n*Backreferences* ")
print("This matches a previously matched group again-")
print("EXAMPLE\t\tDESCRIPTION")
print("([Pp])ython&\\1ails Match python&pails or Python&Pails")
print("(['\"])[^\\1]*\\1 Single or double-quoted string. \\1 matches whatever the 1st group matched. \\2 matches whatever the 2nd group matched, etc.")

print("\n*Alternatives* ")
print("EXAMPLE\t\tDESCRIPTION")
print("python|perl Match \"python\" or \"perl\" ")
print("rub(y|le)) Match \"ruby\" or \"ruble\" ")
print("Python(!+|\?) \"Python\" followed by one or more ! or one ?")

print("\n*Anchors* ")
print("This needs to specify match position. ")
print("EXAMPLE\t\tDESCRIPTION")
print("""^Python Match "Python" at the start of a string or internal line """)
print("""Python$ Match "Python" at the end of a string or line""")
print("""\APython Match "Python" at the start of a string""")
print("""Python\Z Match "Python" at the end of a string""")
print("""\\bPython\\b Match "Python" at a word boundary """)
print("""\\brub\\B \\B is nonword boundary: match "rub" in "rube" and "ruby" but not alone """)
print("""Python(?=!) Match "Python", if followed by an exclamation point. """)
print("""Python(?!!) Match "Python", if not followed by an exclamation point.""")

print("\n*Special Syntax with Parentheses*")
print("EXAMPLE\t\tDESCRIPTION")
print("""R(?#comment) Matches "R". All the rest is a comment """)
print("""R(?i)uby Case-insensitive while matching "uby" """)
print("""R(?i:uby) Same as above """)
print("""rub(?:y|le)) Group only without creating \\1 backreference""")
