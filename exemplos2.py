# Exemplo de uso do método count() em Python
 
# Criando uma string de exemplo
frase = "Python é incrível. Python é divertido. Python é poderoso."
 
# Exibindo a stringoriginal
print(f"Fraseoriginal: '{frase}'")
 
# 1. count() - Contar a ocorrência de uma substringespecífica na string
# Contando quantas vezes a palavra "Python" aparece na frase
ocorrencias_python = frase.count("Python")
 
print(f"A palavra 'Python' aparece {ocorrencias_python} vezes na frase.")
 
# 2. count() com intervalos - Especificando uma faixa de índice (início e fim)
# Contando quantas vezes "Python" aparece entre os índices 0 e 30
ocorrencias_parte = frase.count("Python", 0, 30)
 
print(f"A palavra 'Python' aparece {ocorrencias_parte} vezes entre os índices 0 e 30.")
 
# 3. Contando ocorrências de caracteres individuais
# Contando quantas vezes o caractere 'e' aparece na frase
ocorrencias_e = frase.count("e")
 
print(f"O caractere 'e' aparece {ocorrencias_e} vezes na frase.")
 
# 4. Contando ocorrências de uma substring que não existe
# Tentando contar quantas vezes a palavra "Java" aparece na frase
ocorrencias_java = frase.count("Java")
 
print(f"A palavra 'Java' aparece {ocorrencias_java} vezes na frase.")

############################################################################

# Exemplo de uso do método split() em Python
 
# 1. Usando split() com o separador padrão (espaço em branco)
# Criando uma string com várias palavras separadas por espaços
frase = "Python é uma linguagem poderosa e fácil de aprender"
 
# O método split() sem argumentos divide a string com base nos espaços em branco
lista_palavras = frase.split()
 
print(f"Lista de palavras após split(): {lista_palavras}")
 
# 2. Usando split() com um separador específico
# Vamos dividir a string usando um hífen como separador
data = "2024-09-05"
 
# O método split() agora divide a string sempre que encontrar o hífen "-"
lista_data = data.split("-")
 
print(f"Lista após split('-'): {lista_data}")
 
# 3. Usando split() com múltiplos espaços
# O método split() por padrão ignora múltiplos espaços consecutivos
frase_com_espacos = "Python   é   incrível"
# Mesmo com múltiplos espaços, split() divide corretamente nas palavras
lista_palavras_espacos = frase_com_espacos.split()
 
print(f"Lista de palavras com múltiplos espaços: {lista_palavras_espacos}")
 
# 4. Usando split() com um número limitado de divisões
# Usando o argumento maxsplit para limitar o número de divisões
frase_longa = "Python é uma linguagem versátil e poderosa"
 
# Aqui, estamos limitando para apenas 2 divisões
lista_limitada = frase_longa.split(" ", maxsplit=2)
 
print(f"Lista com maxsplit=2: {lista_limitada}")
 
# 5. Dividindo uma string em caracteres (simulando comportamento do split)
# Se quisermos dividir uma string em caracteres, podemos usar list()
palavra = "Python"
 
# Isso retorna cada caractere como um elemento da lista
lista_caracteres = list(palavra)
 
print(f"Lista de caracteres: {lista_caracteres}")
 
# 6. Usando splitlines() para dividir uma string por quebras de linha
# Criando um texto com múltiplas linhas
texto_multilinhas = "Linha 1\nLinha 2\nLinha 3"
 
# O método splitlines() divide a string onde encontrar quebras de linha (\n)
linhas = texto_multilinhas.splitlines()
 
print(f"Lista de linhas: {linhas}")
 
# 7. Tratando casos em que o separador não existe na string
# Dividindo uma string onde o separador não aparece
frase_sem_ponto = "Python é incrível"
lista_sem_ponto = frase_sem_ponto.split(".")  # O ponto não existe na string
 
print(f"Lista quando o separador não existe: {lista_sem_ponto}")

#############################################################################

# Exemplo de uso do método join() em Python
 
# 1. Usando join() para concatenar uma lista de strings
# Criando uma lista de palavras
lista_palavras = ["Python", "é", "uma", "linguagem", "poderosa"]
 
# O método join() une os elementos da lista em uma única string.
# O que vem antes de join() será o separador entre os elementos da lista
frase = " ".join(lista_palavras)  # Aqui, estamos unindo com um espaço " "
print(f"Frase resultante com espaço: '{frase}'")
 
# 2. Usando join() com diferentes separadores
# Podemos usar qualquer string como separador entre os elementos
frase_com_hifen = "-".join(lista_palavras)  # Usando um hífen como separador
print(f"Frase resultante com hífen: '{frase_com_hifen}'")
 
# 3. Concatenando uma lista de caracteres com join()
# Criando uma lista de caracteres
lista_caracteres = ['P', 'y', 't', 'h', 'o', 'n']
 
# Unindo os caracteres sem nenhum separador
palavra = "".join(lista_caracteres)
print(f"Palavra formada: '{palavra}'")
# 4. Usando join() para formatar uma lista de números
# Criando uma lista de números
lista_numeros = [1, 2, 3, 4, 5]
 
# Como join() só funciona com strings, primeiro precisamos converter os números em strings
# Utilizamos list comprehension para realizar essa conversão
numeros_como_string = [str(numero) for numero in lista_numeros]
 
# Unindo os números em uma string separados por vírgula
numeros_formatados = ", ".join(numeros_como_string)
print(f"Números formatados: '{numeros_formatados}'")
 
# 5. Usando join() para criar uma estrutura com múltiplas linhas
# Criando uma lista de linhas
linhas = ["Linha 1: Cabeçalho", "Linha 2: Conteúdo", "Linha 3: Rodapé"]
 
# Unindo as linhas em uma string, separadas por uma quebra de linha
texto_multilinhas = "\n".join(linhas)
print(f"Texto com múltiplas linhas:\n{texto_multilinhas}")
 
# 6. Usando join() com conjuntos (set)
# Criando um conjunto de palavras
conjunto_palavras = {"Python", "é", "incrível"}
 
# Unindo os elementos do conjunto em uma string com espaço
# Nota: A ordem dos elementos no conjunto pode variar
frase_conjunto = " ".join(conjunto_palavras)
print(f"Frase resultante do conjunto: '{frase_conjunto}'")

##################################################################################

# Exemplo de uso de f-strings em Python
 
# Definindo algumas variáveis de exemplo
nome = "Maria"
idade = 25
altura = 1.68
ocupacao = "Engenheira de Software"
 
# 1. Usando f-strings para incluir variáveis dentro de uma string
# A f-string permite que variáveis sejam diretamente incorporadas à string usando chaves {}
frase = f"Meu nome é {nome}, tenho {idade} anos e minha altura é {altura} metros."
print(frase)
 
# 2. Executando expressões dentro de uma f-string
# Podemos usar expressões diretamente dentro das chaves
print(f"Daqui a 5 anos, {nome} terá {idade + 5} anos.")
 
# 3. Formatação numérica com f-strings
# Podemos controlar o número de casas decimais ou o formato de números
# Exemplo: limitar a altura a duas casas decimais
print(f"A altura de {nome} com duas casas decimais é {altura:.2f} metros.")
 
# 4. Inserindo valores diretamente na f-string sem variáveis
# Também podemos colocar valores diretamente nas chaves
print(f"O resultado de 10 + 20 é {10 + 20}.")
 
# 5. Alinhamento de texto com f-strings
# Alinhando texto à direita, esquerda ou ao centro usando f-strings
print(f"|{'Nome':<10}|{'Idade':^10}|{'Altura':>10}|")
print(f"|{nome:<10}|{idade:^10}|{altura:>10.2f}|")
 
# 6. Usando f-strings com dicionários
# Podemos extrair valores de um dicionário usando f-strings
dados = {"nome": "Carlos", "idade": 30, "cidade": "São Paulo"}
print(f"O nome é {dados['nome']}, tem {dados['idade']} anos e mora em {dados['cidade']}.")
 
# 7. Trabalhando com classes e f-strings
# F-strings também funcionam com atributos de objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
 
pessoa = Pessoa("João", 40)
print(f"{pessoa.nome} tem {pessoa.idade} anos.")

#######################################################################################

# Exemplo de implementação da cifra Zenit Polar em Python
 
# Função para aplicar a cifra Zenit Polar
def zenit_polar(mensagem):
    """
    Função que aplica a cifra de substituição Zenit Polar a uma mensagem.
    Substitui as letras ZENIT por POLAR e vice-versa.
 
    Parâmetros:
    mensagem: string - A mensagem a ser cifrada ou decifrada
    Retorna:
    string - A mensagem transformada
    """
    # Dicionário para mapear a substituição entre letras de ZENIT e POLAR
    substituicoes = {
        'Z': 'P', 'E': 'O', 'N': 'L', 'I': 'A', 'T': 'R',
        'P': 'Z', 'O': 'E', 'L': 'N', 'A': 'I', 'R': 'T',
        'z': 'p', 'e': 'o', 'n': 'l', 'i': 'a', 't': 'r',
        'p': 'z', 'o': 'e', 'l': 'n', 'a': 'i', 'r': 't'
    }
    # Inicializando uma lista para armazenar a mensagem cifrada/decifrada
    mensagem_transformada = []
# Iterar sobre cada caractere na mensagem
    for caractere in mensagem:
        # Se o caractere estiver nas substituições, trocamos pela letra correspondente
        if caractere in substituicoes:
            mensagem_transformada.append(substituicoes[caractere])
        else:
            # Se não, mantemos o caractere original (como espaços, pontuação, etc.)
            mensagem_transformada.append(caractere)
    # Juntar a lista de caracteres em uma única string
    return ''.join(mensagem_transformada)
 
# Testando a função com exemplos
 
# 1. Teste com uma mensagem simples
mensagem_original = "Zenit Polar é uma cifra simples!"
print(f"Mensagem original: {mensagem_original}")
 
# Aplicando a cifra Zenit Polar
mensagem_cifrada = zenit_polar(mensagem_original)
print(f"Mensagem cifrada: {mensagem_cifrada}")
 
# Aplicando novamente para voltar à mensagem original
mensagem_decifrada = zenit_polar(mensagem_cifrada)
print(f"Mensagem decifrada: {mensagem_decifrada}")
 
# 2. Teste com uma mensagem contendo letras minúsculas
mensagem_original2 = "Este método é reversível."
print(f"\nMensagem original: {mensagem_original2}")
 
# Aplicando a cifra Zenit Polar
mensagem_cifrada2 = zenit_polar(mensagem_original2)
print(f"Mensagem cifrada: {mensagem_cifrada2}")
 
# Desfazendo a cifra
mensagem_decifrada2 = zenit_polar(mensagem_cifrada2)
print(f"Mensagem decifrada: {mensagem_decifrada2}")

#################################################################################

# Exemplo de tratamento de exceções em Python
 
# Função para realizar uma divisão segura entre dois números
def dividir_numeros(a, b):
    """
    Função que tenta dividir dois números, tratando possíveis exceções.
    Parâmetros:
    a: int ou float - O numerador
    b: int ou float - O denominador
    Retorna:
    float ou None - O resultado da divisão se for bem-sucedida, ou None em caso de erro
    """
    try:
        # Tentativa de divisão
        resultado = a / b
    except ZeroDivisionError:
        # Tratamento da exceção se houver divisão por zero
        print("Erro: Não é possível dividir por zero.")
        return None
    except TypeError:
        # Tratamento da exceção se o tipo dos parâmetros for inválido
        print("Erro: Ambos os valores devem ser números (int ou float).")
        return None
    else:
        # O bloco else é executado se não houver exceção
        return resultado
    finally:
        # O bloco finally é sempre executado, com ou sem exceção
        print("Operação de divisão finalizada.")
 
# Testando a função dividir_numeros com diferentes entradas
 
# 1. Caso normal (sem exceção)
print("Teste 1: Divisão normal")
resultado1 = dividir_numeros(10, 2)
print(f"Resultado: {resultado1}\n")
 
# 2. Caso de divisão por zero (ZeroDivisionError)
print("Teste 2: Divisão por zero")
resultado2 = dividir_numeros(10, 0)
 
# 3. Caso com tipo de dado inválido (TypeError)
print("Teste 3: Tipo de dado inválido")
resultado3 = dividir_numeros(10, "cinco")
print(f"Resultado: {resultado3}\n")
 
# 4. Tratando exceções genéricas
def abrir_arquivo(nome_arquivo):
    """
    Função para abrir um arquivo e tratar exceções comuns.
    Parâmetros:
    nome_arquivo: string - Nome do arquivo a ser aberto
    Retorna:
    Conteúdo do arquivo ou None se ocorrer um erro
    """
    try:
        # Tentativa de abrir o arquivo no modo de leitura
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:
        # Tratamento da exceção caso o arquivo não seja encontrado
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except PermissionError:
        # Tratamento da exceção caso não haja permissão para acessar o arquivo
        print(f"Erro: Permissão negada para abrir o arquivo '{nome_arquivo}'.")
        return None
    finally:
        # Este bloco é executado independentemente do resultado
        print("Tentativa de abrir arquivo finalizada.")
 
# Testando a função abrir_arquivo
 
# 1. Caso normal (se o arquivo existir)
print("Teste 4: Abrindo um arquivo existente")
conteudo_arquivo = abrir_arquivo("exemplo.txt")
print(f"Conteúdo do arquivo: {conteudo_arquivo}\n")
 
# 2. Caso onde o arquivo não existe (FileNotFoundError)
print("Teste 5: Tentando abrir um arquivo que não existe")
conteudo_arquivo_inexistente = abrir_arquivo("arquivo_inexistente.txt")
print(f"Conteúdo do arquivo: {conteudo_arquivo_inexistente}\n")