'''
3. Armazene os nomes de alguns de seus
amigos em uma lista chamada amigos.
Exiba o nome de cada pessoa acessando
cada elemento da lista um de cada vez.
'''

# utilizando for
amigos = ["Endi", "Felipe", "João", "Leonardo", "Maria"];

for amigo in amigos:
    print(amigo);


# utilizando while
count = 0;
while count < len(amigos):
    print(amigos[count]);
    count += 1;