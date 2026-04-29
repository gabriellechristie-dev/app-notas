import json
import os


# ------------------------
# CARREGAR DADOS 
# ------------------------
def carregar_dados():
    if os.path.exists("notas.json"):
        try:
            with open("notas.json") as file:
                return json.load(file)
            
        except json.decoder.JSONDecodeError:
           return []
        
    else:
        return []


# ------------------------
# SALVAR DADOS 
# ------------------------
def salvar_dados(lista_de_notas):
    with open("notas.json", "w", encoding="utf-8") as file:
        json.dump(lista_de_notas, file, indent=4, ensure_ascii=False)
        

# ------------------------
# ADICIONAR NOTA
# ------------------------
def adicionar_nota(lista_de_notas):
    titulo =  input("Digite o título da nota: ")
    conteudo = input("Digite o conteudo da nota:")
    nota = {"titulo": titulo, "conteudo": conteudo}
    lista_de_notas.append(nota)
    salvar_dados(lista_de_notas)
    print("Nota adicionada com sucesso!")
    return lista_de_notas
    


# ------------------------
# LISTAR NOTAS  
# ------------------------
def listar_notas(lista_de_notas):
    if not lista_de_notas:
        print("Nenhuma nota cadastrada.")
    else:
        for index, nota in enumerate(lista_de_notas, start=1):
            print(f"{index}. {nota['titulo']}: {nota['conteudo']}")



# ------------------------
# EDITAR NOTA  
# ------------------------
def editar_nota(lista_de_notas):
    if not lista_de_notas:
        print("Nenhuma nota para editar.")
        return lista_de_notas
    
    listar_notas(lista_de_notas)
    indice = int(input("Digite o número da nota que deseja editar:")) - 1

    if 0 <= indice < len(lista_de_notas):
       
        
        novo_titulo = input("Digite o novo título da nota:")
        novo_conteudo = input("Digite o novo conteúdo da nota:")
        lista_de_notas[indice]["titulo"] = novo_titulo
        lista_de_notas[indice]["conteudo"] = novo_conteudo

        salvar_dados(lista_de_notas)
        print("Nota editada com sucesso!")
        return lista_de_notas
        
    else:
        print("Número inválido, tente novamente.")
        return lista_de_notas

# ------------------------
# EXCLUIR NOTA
# ------------------------
def excluir_nota(lista_de_notas):
    if not lista_de_notas:
        print("Nenhuma nota para excluir.")
        return lista_de_notas
    listar_notas(lista_de_notas)
    indice = int(input("Digite o número da nota que deseja excluir:")) - 1
    if 0 <= indice < len(lista_de_notas):
        lista_de_notas.pop(indice)
        salvar_dados(lista_de_notas)
        print("Nota excluída com sucesso")
        return lista_de_notas
        
    else:
        print("Número inválido, tente novamente.")
        return lista_de_notas

# ------------------------
# MENU PRINCIPAL
# ------------------------
def menu():
    lista_de_notas = carregar_dados()
    while True:
        print("Menu de Notas")
        print("1. Adicionar Nota")
        print("2. Listar Notas")
        print("3. Editar nota")
        print("4. Excluir Nota")
        print("5. Sair")
        escolha = int(input("Digite a opção desejada:"))
        if escolha == 1:
            lista_de_notas = adicionar_nota(lista_de_notas)
        elif escolha == 2:
            listar_notas(lista_de_notas)
        elif escolha == 3:
            lista_de_notas = editar_nota(lista_de_notas)
        elif escolha == 4:
            lista_de_notas = excluir_nota(lista_de_notas)
        elif escolha == 5:
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

# ------------------------
# EXECUÇÃO
# ------------------------
if __name__ == "__main__":
    menu()
 