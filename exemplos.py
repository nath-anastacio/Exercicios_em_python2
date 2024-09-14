# Cria um arquivo de texto chamado "meuarquivo.txt" e escreve conteúdo nele
with open("meuarquivo.txt", "w") as file:
    file.write("Olá! Meu nome é Nathália.")


# Lê o conteúdo do arquivo "meuarquivo.txt"
with open("meuarquivo.txt", "r") as file:
    conteudo = file.read()
 
# Exibe o conteúdo do arquivo
print(conteudo)


def main():
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")
    frases = []
    while True:
        entrada = input("> ")
        if entrada.lower() == "sair":
            break
        frases.append(entrada)
    with open("meu_arquivo.txt", "w") as arquivo:
        for frase in frases:
            arquivo.write(frase + "\n")
    print("Arquivo original criado. Agora vamos manipular os dados.")
    dados_modificados = []
    with open("meu_arquivo.txt", "r") as arquivo:
        for linha in arquivo:
            dados_modificados.append(linha.strip().upper())  # Exemplo de manipulação: converter para maiúsculas
    with open("meu_arquivo.txt", "w") as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + "\n")
    print("O arquivo foi sobrescrito com os dados modificados.")
if __name__ == "__main__":
    main()
    

# Abre o arquivo "meuarquivo.txt" em modo de adição
with open("meuarquivo.txt", "a") as file:
    # Acrescenta informações sobre alunos da Estácio
    file.write("\nLista de Alunos da Estácio:\n")
    file.write("1. João Silva\n")
    file.write("2. Maria Oliveira\n")
    file.write("3. Pedro Santos\n")
    file.write("4. Ana Costa\n")
 
# Confirmação de que os dados foram acrescentados
print("Informações sobre alunos da Estácio foram acrescentadas ao arquivo.")


# Lê o conteúdo do arquivo "meuarquivo.txt"
with open("meuarquivo.txt", "r") as file:
    linhas = file.readlines()
 
# Filtra as linhas que não contêm "Ana Costa"
linhas_filtradas = [linha for linha in linhas if "Ana Costa" not in linha]
 
# Escreve o conteúdo filtrado de volta ao arquivo
with open("meuarquivo.txt", "w") as file:
    file.writelines(linhas_filtradas)
 
print("A linha com 'Ana Costa' foi removida do arquivo.")