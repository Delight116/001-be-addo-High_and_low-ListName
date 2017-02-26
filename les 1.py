
def high_and_low(arg):
    mas = arg.split()
    print(str(max(mas)) + " " + str(min(mas)))
    return  str(max(mas)) + " " + str(min(mas))

high_and_low ("1 2 3 4 5") # возвращение "5 1"
high_and_low ("1 2 -3 4 5") # возвращение "5 -3"
high_and_low ("1 9 3 4 -5") # возвращение "9 -5"

def namelist(arg):
    result = ''
    if len(arg) == 0:
        result = "''"
    elif len(arg) == 1:
        result = arg[0]['name']
    else:
        for i,key in enumerate(arg):
            result += key['name']
            if i == len(arg) - 2:
                result += ' & '
            else:
                result += ', '
        result = result[:-2]
    print(result)
    return result




namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart, Lisa & Maggie'
namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'
namelist([ {'name': 'Bart'} ])
# returns 'Bart'
namelist([])
# returns ''