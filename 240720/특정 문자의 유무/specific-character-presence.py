def isIncluded(key, string):
    if key in string:
        print('Yes', end = ' ')
    else:
        print('No', end = ' ')

given = input()

key1 = 'ee'
key2 = 'ab'

isIncluded(key1, given)
isIncluded(key2, given)