############################
##### Exercises step 2 #####
############################

########################
# Exercise 01

list=['apple','pears','bananas','kiwis'];

print("All elements in order:",list)

print("First element:", list[0]);
print("Second element:", list[1]);
print("Third element:", list[2]);
print("Forth element:", list[3]);


########################
# Exercise 02 - fist element?

print("First element:", list[0]);

########################
# Exercise 03 - last element?

print("Last element:", list[-1]);

########################
# Exercise 04 - one before last element?

print("Last element:", list[-2]);

########################
# Exercise 05 - Two first elements of list:

print("Two first elements of list", list[:2]);

########################
# Exercise 06 - Replace 'apples' by 'grapefruits':

list[0] = 'grapefruits'
print(list)

########################
# Exercise 07 - What's list len?

list_size = list.__len__()

int(list_size)
print("List size:",list_size,"elements.")

########################
# Exercise 08 - Add 'pineapple' in the end of the list

list.append('pineapple')

print(list);

########################
# Exercise 09 - Add 'carrots' as second element of the list


help(list.extend)

#list.extend('carrots':list[1])

print(list);

list.insert(2,'carrots')

print(list)

# 10 - Elimine o elemento 'bananas'.

list.remove('bananas')

print(list)

# 11 - Elimine o último elemento da lista.

list.pop(len(list)-1)

# 12 - Crie o reverso da lista atual.

list.reverse()

print(list)

# 13 13 - Adicione os seguintes elementos à lista:
'''- deodorant
- shampoo
- bread
- gum
- tictacs'''

for i in range(5):
    x=['deodorant','shampoo','bread','gun','tictacs']
    list.append(x[i])

list

# 14 - Qual é a principal diferença entre um tuplo e uma lista?
'Tupple é imutavel, enquanto que a lista é mutável.'

# 15 - Crie um tuplo com os elementos 1,2,3.

tuplo=(1,2,3)
tuplo

# 16 - Converta a sua lista num tuplo.

lista = tuple(list)
lista

# 17 - Quantos elementos tem o tuplo?

len(lista)

# 18 - Em que lugar do tuplo se encontra o elemento 'gum'?

lista.index('gun')

# 19 - Adicione o elemento 'water' ao tuplo.

new_tuple=('kiwis', 'carrots', 'pears', 'grapefruits', 'deodorant', 'shampoo', 'bread', 'gun', 'tictacs')
new_tuple

temp = list(new_tuple)
temp.append('water')
temp
new_tuple = tuple(temp)
new_tuple

# 20 - Qual é a diferença entre um set e um tuplo? E entre um set e uma lista?

'Set é mutável e o tuplo não. Set não pode ter o index reordenado, enquanto a lista e o tuplo podem.'.__setattr__

# 21 - Defina um set com as seguintes cores: azul, amarelo, branco, rosa:

my_set = {'azul','amarelo','branco','rosa'}
type(my_set)

# 22 - Qual é a posição que a cor branco ocupa no set?

'O set não é indexável, logo não existe posição index dos elementos.'

# 23 - Adicione a cor lilás ao set.

#my_set.add('lilás')

my_set.add('lilás')
my_set

# 24 - Adicione as seguintes cores ao set: castanho, laranja, verde

my_set.update(['castanho','laranja','verde'])

print(my_set)

'''my_set.update = (['castanho','laranja','verde'])
my_set
'''

# 25 - Quantos elementos em o set?

len(my_set)

# 26 - Crie um novo set com os elementos a,b,c,d.

new_set={'a','b','c','d'}
new_set

# 27 - Adicione o novo set ao anterior (criar novo set).

my_set3 = my_set.union(new_set)
my_set3

# 28 - Elimine todos os elementos do set my_set
my_set.clear()
my_set

# 29 - Dado o seguinte dicionário:
'''
estudante = {
    'nome': 'Alice',
    'idade': 25,
    'cursos': ['Matemática', 'Física', 'Química'],
    'notas': {'Matemática': 90, 'Física': 85, 'Química': 88}
}

Faça o seguinte:
- Adicione um novo par de chave-valor ao dicionário. A chave deve ser 'endereço' e o valor deve ser 'Rua Principal, 123'.
- Acrescente 'História' à lista de cursos.
- Aumente a idade da Alice em 1 ano.
- Altere a nota dela em Física para 90.
- Remova a chave 'notas' do dicionário.
'''

estudante = {
    'nome': 'Alice',
    'idade': 25,
    'cursos': ['Matemática','Física','Química'],
    'notas': {'Matemática': 90, 'Física':85, 'Qúimica':88}
}
#1)- Adicione um novo par de chave-valor ao dicionário. A chave deve ser 'endereço' e o valor deve ser 'Rua Principal, 123'.
estudante.update({'endereço':'Rua Principal, 123'})
estudante

#2)- Acrescente 'História' à lista de cursos.

temp=estudante['cursos']
print(temp)
estudante.update('cursos'
estudante

