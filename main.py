def criar_nota():
    lista_de_notas = []
    print("Digite 'esc' para sair")
    
    while True:
        nota = (input("Digite sua anotação"))
        if nota == "esc":
            break
        else:
           lista_de_notas.append(nota)
    return lista_de_notas

def editar_nota(lista_de_notas):
    edicao = (input("Deseja editar uma nota? s/n"))
    if edicao == "s":
        print(lista_de_notas)
        num_usuario = (int(input("Digite o numero da nota")))
        if num_usuario >= 1 and num_usuario <= len(lista_de_notas):
            num_usuario -= 1
            nova_nota = (input("Digite sua edição"))
            lista_de_notas[num_usuario] = nova_nota
  
    return lista_de_notas


    