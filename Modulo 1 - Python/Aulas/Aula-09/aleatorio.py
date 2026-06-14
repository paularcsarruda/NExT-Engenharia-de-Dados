import random as rd

for _ in range(10):
    print(rd.randint(1, 25))


#=====================================================
nomes = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
print(rd.choice(nomes))
print(rd.sample(nomes, 3)) # amostra de 3 nomes sem repetição
rd.shuffle(nomes) # embaralha a lista de nomes
print(nomes)

