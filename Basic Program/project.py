name = ["Ram", "Syam", "Hari"]
print(name)
q = input('Do you want add or remove name input add or remaing: ')
if q == 'add':
  a = int(input('add number of Name: '))
  for x in range(a):
    new = input('Enter name:')
    name.append(new)
    print(name)

if q == 'rem':
  a = input('Enter remove of Name: ')
  name.remove(a)
  print(name)