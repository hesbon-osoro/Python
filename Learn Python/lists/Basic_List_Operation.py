#Basic List Operation
languages = ['Python','Java','C#','C++','C','Perl','Ruby','Android','Swift']
nums = [0,1,2,3,4,5,6,7,8,9]
days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print("%s"%'***basic list operation***'.title())
print("%s"%'*length*'.title())
print("languages: %s"%languages)
print("len(languages):",len(languages))
print("nums: %s"%nums)
print("len(nums):",len(nums))
print("days: %s"%days)
print("len(days):",len(days))
print("months: %s"%months)
print("len(months):",len(months))
print("%s"%'*concatenation*'.title())
print("languages: %s"%(languages+nums))
print("len(languages + nums):",len(languages+nums))
print("%s"%'*repetition*'.title())
print("%s"%('-Programing is fun!'*3))
print("%s"%'*membership*'.title())
print("'java' in languages:",'java' in languages)
print("'Java' in languages:",'Java' in languages)
print("%s"%'*iteration*'.title())
for lan in languages:
    print(lan)
for lan in languages:
    print(lan, end=' ')

