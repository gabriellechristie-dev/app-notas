# 📝 Notes App (CLI)

Aplicação simples de gerenciamento de notas no terminal (CLI), desenvolvida em Python.
Permite criar, listar, editar e excluir notas com persistência em arquivo JSON.

---

## Funcionalidades

* Adicionar nota (título + conteúdo)
* Listar todas as notas
* Editar uma nota existente
* Excluir uma nota
* Salvamento automático em arquivo `notas.json`
* Carregamento automático ao iniciar o programa

---

##  Estrutura

* `carregar_dados()` → lê o arquivo JSON
* `salvar_dados()` → salva no JSON
* `adicionar_nota()` → cria nova nota
* `listar_notas()` → exibe notas
* `editar_nota()` → altera nota existente
* `excluir_nota()` → remove nota
* `menu()` → controla o fluxo da aplicação

---

##  Como executar

1. Instale o Python (versão 3.10 ou superior)

2. Baixe ou clone este projeto para o seu computador

3. Abra a pasta do projeto

   - No Windows: clique com o botão direito na pasta e escolha "Abrir no Terminal"
   - Ou abra o terminal e navegue até a pasta usando o comando cd

4. No terminal, execute:

   python main.py

   (ou python3 main.py, dependendo do sistema)

---

##  Armazenamento

As notas são salvas no arquivo:

```text
notas.json
```

Formato:

```json
[
  {
    "titulo": "Exemplo",
    "conteudo": "Minha anotação"
  }
]
```

---

##  Observações

* Caso o arquivo não exista, ele é criado automaticamente
* Caso esteja vazio ou inválido, o sistema inicia com lista vazia
* Índices exibidos começam em 1 (interface amigável)

---

##  Próximos passos

* Melhorar validação de entrada
* Separar responsabilidades em módulos
* Criar interface web (Flask + HTML + JS)

---
