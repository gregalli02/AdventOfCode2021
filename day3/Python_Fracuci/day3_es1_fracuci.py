# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:30:54 2021

@author: fracuci
"""



fh = open('numberDay3.txt','r')
#fh = open('input_test.txt', 'r')

#### Binary Diagnostic of the submarine- PART ONE:
#### calculate gamma rate and epsilon rate
#### to get power consumption by multipling those two number


lines = fh.readlines()

#### Il dataset ha il carrige return('\n'), lo pulisco:

clean_lines = [l.strip('\n') for l in lines]

#lazy solution:

columns = {}

# inizializza un dizionario di colonne in cui ogni colonna è reppresentata da
# una lista che rappresenta la colonna del dataset e, per ogni lista, il primo elemento 
# è il conteggio degli zeri nella colonna, il secondo elemento è il conteggio
# degli uno nella colonna - il numero di colonne è fisso

for i in range(0,len(clean_lines[0])):
    columns[str(i)] = [0,0]


#riempi il dizionario e calcola il numero di 0 e 1 di ogni posizione

for j in range(0,len(clean_lines)):
    for i in range(0,len(clean_lines[j])):
        if int(clean_lines[j][i]) == 0:
            columns[str(i)][0] += 1
        else:
            columns[str(i)][1] += 1

print(columns)

gamma_rate = []
epsilon_rate = []

for k in columns.keys():
    if columns[k][0] > columns[k][1]:
        gamma_rate.append(0)
        epsilon_rate.append(1)
    else:
        gamma_rate.append(1)
        epsilon_rate.append(0)

print('gamma_rate: ', gamma_rate)
print('epsilon_rate: ', epsilon_rate)


# calcolo gamma_rate e epsilon rate in decimale:

gamma_rate_decimal = 0
epsilon_rate_decimal = 0
    
for i in range(0,len(gamma_rate)):

    if gamma_rate[i] == 1:
        gamma_rate_decimal += 2**(len(gamma_rate)-i-1)
        
    if epsilon_rate[i] == 1:
        epsilon_rate_decimal += 2**(len(gamma_rate)-i-1)

print('gamma_rate_decimal: ', gamma_rate_decimal, '\nepsilon_rate_decimal: ', epsilon_rate_decimal)

print('Power consumption: ', gamma_rate_decimal*epsilon_rate_decimal)
    
fh.close()



