lista_de_notas = []

while True:
    print("Digite 'esc' para sair!")
    nota = (input("Digite uma nova nota..."))
    if nota == "esc":
        break
    elif nota == "":
        print("Não é possível criar uma  nota vazia")
        continue
    lista_de_notas.append(nota)
if not lista_de_notas:
    print("Nenhuma nota cadastrada!")
else:
    for indice, valor in enumerate(lista_de_notas):
        print(f"{indice + 1} - {valor}")

if not lista_de_notas:
    print("Nenhuma nota para remover!")
else:
    for indice, valor in enumerate(lista_de_notas):
        print(f"{indice + 1} - {valor}")
   