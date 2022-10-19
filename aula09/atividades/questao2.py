'''
2. Use um dicionário para armazenar os números favoritos
   de algumas pessoas. Escolha cinco colegas, e pergunte
   quais seus números favoritos. Use seus nomes para serem
   as chaves de cada número favorito. Ao final, exiba o nome
   de cada pessoa e seu número favorito.
'''

num_fav = {"Léo": 8, "Endi": 2, "Felipe": 10, "Carlos": 444, "Zé": 15}

for key in num_fav:
  print(f"{key}: {num_fav[key]}")