def pershendetja():
    print('pershendetje')

pershendetja()
'''
print('Pershendetje Blina')
print('Pershenteje Deon')
print('Pershenteje Jon')
print('Pershendetje Ajan')
print('Pershendetje Puhiza')
'''


def greeting(name):
    print('Pershendetje', name)

greeting('Puhiza')
greeting('Blina')

greeting('Orges')
# local variables, te qasshme vetem brenda funksionit
def shuma(num1 ,num2):
    print(num1+num2)

shuma(2, 3)
shuma(4, 6)
shuma(10, 8)


#global variable

niveli = 'Python advanced'

def shkolla_digjitale(name):
    message = f'Pershendetje une jam {name} dhe jam ne nivelin {niveli}' # f string, ben bashk tekstin dhe variablat etj
    print(message)

#E therrasim funksionin duke dhene parametrin name
shkolla_digjitale('Blina')

#Shendrrimi i nje variable locale ne variable globale
def age():
    global message1
    message1 = f'Une jam Blina dhe kam 17 vjet'

age()
print(message1)