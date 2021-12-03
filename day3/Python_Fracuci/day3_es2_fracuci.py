# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:32:39 2021

@author: fracuci
"""

fh = open('numberDay3.txt','r')
#fh = open('input_test.txt', 'r')

#### Binary Diagnostic of the submarine- PART TWO:
#### calculate oxygen generator rating and CO2 scrubber rating
#### to get the life support rating by multipling those two number


lines = fh.readlines()

#### Il dataset ha il carrige return('\n'), lo pulisco:

clean_lines = [l.strip('\n') for l in lines]

#lazy (E INUTILMENTE DIFFICILE) solution:

columns_oxygen_rate_num = {}
columns_co2_rate_num = {}

# inizializza un dizionario di colonne in cui ogni colonna è reppresentata da
# una lista che rappresenta la colonna di un dataset che di volta in volta si 
# riduce (il dataset usato nella colonna  i+1 è quello della colonna i)
# e, per ogni lista, il primo elemento 
# è il conteggio degli zeri nella colonna, il secondo elemento è il conteggio
# degli uno nella colonna, il terzo elemento è il sotto insieme dei numeri
# di volta in volta estratti - il numero di colonne è fisso

for i in range(0,len(clean_lines[0])+1):
    columns_oxygen_rate_num[str(i)] = [0,0, []]
    columns_co2_rate_num[str(i)] = [0,0, []]


# Inizializza il primo sotto-insieme nella colonna '0'
columns_oxygen_rate_num['0'][2] = clean_lines
columns_co2_rate_num['0'][2] = clean_lines



#riempi il dizionario e calcola il numero di 0 e 1 di ogni posizione e il
# nuovo subset di dati per l'oxygen_rate

for i in range (0, len(columns_oxygen_rate_num.keys())):
    # print(i)
    # print(columns_oxygen_rate_num[str(i)][2])
    
    if len(columns_oxygen_rate_num[str(i)][2]) > 1 or i < len(columns_oxygen_rate_num.keys())-1:
        
       # print(i)
       # print(columns_oxygen_rate_num[str(i)][2])
        
        for j in range(0,len(columns_oxygen_rate_num[str(i)][2])):
            
            
            if int(columns_oxygen_rate_num[str(i)][2][j][i]) == 0:
                
                columns_oxygen_rate_num[str(i)][0] +=1
            
            else:
                
                columns_oxygen_rate_num[str(i)][1] +=1
                
            
        if columns_oxygen_rate_num[str(i)][0] > columns_oxygen_rate_num[str(i)][1] and not columns_oxygen_rate_num[str(i)][0] == 1:
            
            for j in range(0,len(columns_oxygen_rate_num[str(i)][2])):
            
                if int(columns_oxygen_rate_num[str(i)][2][j][i]) == 0:
                    
                    columns_oxygen_rate_num[str(i+1)][2].append(columns_oxygen_rate_num[str(i)][2][j])
            
        elif columns_oxygen_rate_num[str(i)][0] < columns_oxygen_rate_num[str(i)][1] and not columns_oxygen_rate_num[str(i)][1] == 1:
            
            for j in range(0,len(columns_oxygen_rate_num[str(i)][2])):
            
                if int(columns_oxygen_rate_num[str(i)][2][j][i]) == 1:
                    
                    columns_oxygen_rate_num[str(i+1)][2].append(columns_oxygen_rate_num[str(i)][2][j])
            
        else:
            
            for j in range(0,len(columns_oxygen_rate_num[str(i)][2])):
            
                if int(columns_oxygen_rate_num[str(i)][2][j][i]) == 1:
                    
                    columns_oxygen_rate_num[str(i+1)][2].append(columns_oxygen_rate_num[str(i)][2][j])
      
    else:
        
        for j in range(0,len(columns_oxygen_rate_num[str(i)][2])):        

            if int(columns_oxygen_rate_num[str(i)][2][j][i-1]) == 0:
                            
                columns_oxygen_rate_num[str(i)][0] +=1
                        
            else:
                            
                columns_oxygen_rate_num[str(i)][1] +=1


        if columns_oxygen_rate_num[str(i)][0] > columns_oxygen_rate_num[str(i)][1] and not columns_oxygen_rate_num[str(i)][0] == 1:
            
            for j in range(0,len(columns_oxygen_rate_num[str(i)][2])):
            
                if int(columns_oxygen_rate_num[str(i)][2][j][i-1]) == 0:
                    
                    columns_oxygen_rate_num[str(i)][2].append(columns_oxygen_rate_num[str(i)][2][j])
            
        elif columns_oxygen_rate_num[str(i)][0] < columns_oxygen_rate_num[str(i)][1] and not columns_oxygen_rate_num[str(i)][1] == 1:
            
            for j in range(0,len(columns_oxygen_rate_num[str(i)][2])):
            
                if int(columns_oxygen_rate_num[str(i)][2][j][i-1]) == 1:
                    
                    columns_oxygen_rate_num[str(i)][2].append(columns_oxygen_rate_num[str(i)][2][j])
            
        else:
            
            for j in range(0,len(columns_oxygen_rate_num[str(i)][2])):
            
                if int(columns_oxygen_rate_num[str(i)][2][j][i-1]) == 1:
                    
                    columns_oxygen_rate_num[str(i)][2].append(columns_oxygen_rate_num[str(i)][2][j])                





#riempi il dizionario e calcola il numero di 0 e 1 di ogni posizione e il
# nuovo subset di dati per la co2_rate



for i in range (0, len(columns_co2_rate_num.keys())):
    # print(i)
    # print(columns_oxygen_rate_num[str(i)][2])
    
    if len(columns_co2_rate_num[str(i)][2]) > 1 or i < len(columns_co2_rate_num.keys())-1:
        
       # print(i)
       # print(columns_oxygen_rate_num[str(i)][2])
        
        for j in range(0,len(columns_co2_rate_num[str(i)][2])):
            
            
            if int(columns_co2_rate_num[str(i)][2][j][i]) == 0:
                
                columns_co2_rate_num[str(i)][0] +=1
            
            else:
                
                columns_co2_rate_num[str(i)][1] +=1
                
            
        if columns_co2_rate_num[str(i)][0] < columns_co2_rate_num[str(i)][1] and not columns_co2_rate_num[str(i)][1] == 1:
            
            for j in range(0,len(columns_co2_rate_num[str(i)][2])):
            
                if int(columns_co2_rate_num[str(i)][2][j][i]) == 0:
                    
                    columns_co2_rate_num[str(i+1)][2].append(columns_co2_rate_num[str(i)][2][j])
            
        elif columns_co2_rate_num[str(i)][0] > columns_co2_rate_num[str(i)][1] and not columns_co2_rate_num[str(i)][0] == 1:
            
            for j in range(0,len(columns_co2_rate_num[str(i)][2])):
            
                if int(columns_co2_rate_num[str(i)][2][j][i]) == 1:
                    
                    columns_co2_rate_num[str(i+1)][2].append(columns_co2_rate_num[str(i)][2][j])
            
        else:
            
            for j in range(0,len(columns_co2_rate_num[str(i)][2])):
            
                if int(columns_co2_rate_num[str(i)][2][j][i]) == 0:
                    
                    columns_co2_rate_num[str(i+1)][2].append(columns_co2_rate_num[str(i)][2][j])
      
    else:
        
        for j in range(0,len(columns_co2_rate_num[str(i)][2])):        

            if int(columns_co2_rate_num[str(i)][2][j][i-1]) == 0:
                            
                columns_co2_rate_num[str(i)][0] +=1
                        
            else:
                            
                columns_co2_rate_num[str(i)][1] +=1


        if columns_co2_rate_num[str(i)][0] < columns_co2_rate_num[str(i)][1] and not columns_co2_rate_num[str(i)][0] == 1:
            
            for j in range(0,len(columns_co2_rate_num[str(i)][2])):
            
                if int(columns_co2_rate_num[str(i)][2][j][i-1]) == 0:
                    
                    columns_co2_rate_num[str(i)][2].append(columns_co2_rate_num[str(i)][2][j])
            
        elif columns_co2_rate_num[str(i)][0] > columns_co2_rate_num[str(i)][1] and not columns_co2_rate_num[str(i)][1] == 1:
            
            for j in range(0,len(columns_co2_rate_num[str(i)][2])):
            
                if int(columns_co2_rate_num[str(i)][2][j][i-1]) == 1:
                    
                    columns_co2_rate_num[str(i)][2].append(columns_co2_rate_num[str(i)][2][j])
            
        else:
            
            for j in range(0,len(columns_co2_rate_num[str(i)][2])):
            
                if int(columns_co2_rate_num[str(i)][2][j][i-1]) == 0:
                    
                    columns_co2_rate_num[str(i)][2].append(columns_co2_rate_num[str(i)][2][j])       





k_oxygen = 0

for k in columns_oxygen_rate_num.keys():
    
    if len(columns_oxygen_rate_num[k][2]) > 0:
        
        k_oxygen = k
        
    else:
        
        break

print(k_oxygen, columns_oxygen_rate_num[str(k_oxygen)])

columns_oxygen_rate_num_decimal = 0

if columns_oxygen_rate_num[str(k_oxygen)][0] == 1:
    
    print(columns_oxygen_rate_num[str(k_oxygen)][2][0])
    for i in range (0,len(columns_oxygen_rate_num[str(k_oxygen)][2][0])):
        
        if int(columns_oxygen_rate_num[str(k_oxygen)][2][0][i]) == 1:
    
            columns_oxygen_rate_num_decimal += 2**(len(columns_oxygen_rate_num[str(k_oxygen)][2][0])-i-1)
        
else:
    
    print(columns_oxygen_rate_num[str(k_oxygen)][2][1])
    for i in range (0,len(columns_oxygen_rate_num[str(k_oxygen)][2][1])):
        
        if int(columns_oxygen_rate_num[str(k_oxygen)][2][1][i]) == 1:
    
            columns_oxygen_rate_num_decimal += 2**(len(columns_oxygen_rate_num[str(k_oxygen)][2][0])-i-1)
            
            
            
k_co2 = 0


for k in columns_co2_rate_num.keys():
    
    if len(columns_co2_rate_num[k][2]) > 0:
        
        k_co2 = k
        
    else:
        
        break



print(k_oxygen, columns_co2_rate_num[str(k_co2)])

columns_co2_rate_num_decimal = 0

if columns_co2_rate_num[str(k_co2)][0] == 1:
    
    print(columns_co2_rate_num[str(k_co2)][2][0])
    for i in range (0,len(columns_co2_rate_num[str(k_co2)][2][0])):
        
        if int(columns_co2_rate_num[str(k_co2)][2][0][i]) == 1:
    
            columns_co2_rate_num_decimal += 2**(len(columns_co2_rate_num[str(k_co2)][2][0])-i-1)
        
else:
    
    print(columns_co2_rate_num[str(k_co2)][2][0])
    for i in range (0,len(columns_co2_rate_num[str(k_co2)][2][0])):
        
        if int(columns_co2_rate_num[str(k_co2)][2][0][i]) == 1:
    
            columns_co2_rate_num_decimal += 2**(len(columns_co2_rate_num[str(k_co2)][2][0])-i-1)





            

print('columns_oxygen_rate_num_decimal: ', columns_oxygen_rate_num_decimal)


print('columns_oxygen_rate_num_decimal: ', columns_co2_rate_num_decimal)

print('Life support rating', columns_oxygen_rate_num_decimal*columns_co2_rate_num_decimal)

    
    
    
fh.close()