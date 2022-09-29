# Pass in variables for formula
def cheatcode(moles, pressure, temp, length):
    count = 0
    while (count < length):
        # Enter formula 
        ans = (temp[count] * moles[count] * 8.3145) / pressure[count]
        # ans = ans/1000
        print(f'{count}: {ans}')
        count += 1


molearray = []
pressurearray = []
temparray = []
again = 'Y'

while (again == 'Y'):
    molesinput = float(input('Enter number of moles: '))
    pressureinput = float(input('Enter pressure : '))
    tempinput = float(input('Enter temperature: '))
    molearray.append(molesinput)
    pressurearray.append(pressureinput)
    temparray.append(tempinput)
    again = str(input('Run again?: ')).upper()

length = len(molearray)
cheatcode(molearray, pressurearray, temparray, length)
