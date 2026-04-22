def criar_nota():
    lista_de_notas = []
    
    while True:
        nota = (input("Digite sua anotação: "))
        if nota:
         lista_de_notas.append(nota)
           
        return lista_de_notas

def editar_nota(lista_de_notas):
    edicao = (input("Deseja editar uma nota? s/n"))
    if edicao == "s":
        for indice, valor in enumerate(lista_de_notas):
            print(indice + 1, "-", valor )
        num_usuario = (int(input("Digite o numero da nota")))
        if num_usuario >= 1 and num_usuario <= len(lista_de_notas):
            num_usuario -= 1
            nova_nota = (input("Digite sua edição"))
            lista_de_notas[num_usuario] = nova_nota
  
    return lista_de_notas

def excluir_nota(lista_de_notas):
    excluir = (input("Deseja excluir uma nota? s/n"))
    if excluir == "s":
        for indice, valor in enumerate(lista_de_notas):
            print(indice + 1, "-", valor )
        n_usuario = (int(input("Digite o número da nota ")))
        if n_usuario >= 1 and n_usuario <= len(lista_de_notas):
            n_usuario -= 1
            lista_de_notas.pop(n_usuario)

    return lista_de_notas

lista_de_notas = criar_nota()
lista_de_notas = editar_nota(lista_de_notas)
lista_de_notas = excluir_nota(lista_de_notas)


    