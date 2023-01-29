s = '12abcd405'
result = ''.join(i for i in s if not i.isdigit())
print(result)
'abcd'