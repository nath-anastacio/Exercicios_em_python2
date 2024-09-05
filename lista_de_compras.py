#Lista de compras
def main():
    print("Digite a seguir, os itens que deseja adicionar a sua lista de compras e digite 'SAIR' para sair:")
    lista_de_compras = []
    while True:
        item = input(">>")
        if item.upper() == "SAIR":
            break
        lista_de_compras.append(item.upper()) #Adiciona os dados já convetidos para maiúsculas
    with open("novoarquivo.txt", "w") as file: #Cria o novo arquivo e o abre no modo de escrita
        for i in lista_de_compras: #Percorre os itens da lista
            file.write(">>" + i + "\n") #Escreve no arquivo "novoarquivo.txt" cada item na lista
    print("O arquivo foi escrito com sucesso!")
    with open("novoarquivo.txt", "r") as file:
        conteudo = file.read()
        print(conteudo)

if __name__ == "__main__":
    main()