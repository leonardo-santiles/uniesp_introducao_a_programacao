'''
6. Seja criativo ao desenvolver este programa.
- Crie uma lista de convidados para um jantar em sua casa, com
  pelo menos 5 celebridades.
- Envie um convite para cada uma dessas pessoas. Com a mesma
  mensagem e nome personalizado.
- Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você
  deverá enviar novos convites. Imprima o nome das pessoas que não
  poderão comparecer.
- Modifique sua lista, substitua os desistentes por novos convidados.
- Exiba um novo convite para cada pessoa que continua presente em sua lista.
'''
convidados = ["Coringa", "Thor", "Jesus", "Naruto", "Loki"];

for convidado in convidados:
  mensagem = f"Bora pra balada, {convidado}!";
  print(mensagem);

print("Jesus: Infelizmente, não posso estar no mesmo ambiente que Loki!");
print("Coringa: Infelizmente, não posso estar no mesmo ambiente que Naruto!");

convidados[2] = "Madre Teresa de Calcutá";
convidados[0] = "Pinguim";

for convidado in convidados:
  mensagem = f"Bora pra balada, {convidado}!";
  print(mensagem);