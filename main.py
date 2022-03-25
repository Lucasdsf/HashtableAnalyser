import hashlib  # Importa a lib hashlib.
import os  # Importa a lib os.
import pandas as pd  # Importa a lib pandas como pd.



def imprimirHash(
    hashtabela
):  # Define uma função com o nome display_hash com o atributo hashtabela.
    for i in range(len(hashtabela)):  # Percorre a hashtabela
        print(i, end=" ")  # Imprime a hashtabela com espaço a cada item.

        for j in hashtabela[i]:  # Percorre os itens da hashtabela.
            print(
                "-->", end=" "
            )  # Imprime as chaves dahashtabela com "-->" e espaço no final.
            print(j, end=" ")  # Imprime os valores da hash tabela com espaço.

        print()  # Imprime a hash tabela.


Hashtabela = [[] for _ in range(1000)
              ]  #Cria uma variavel Hashtabela e define seu tamanho.


def Hashing(
    valorChave
):  # Define uma função com o nome Hashing com o atributo valorChave.
    return valorChave % len(
        Hashtabela
    )  # Retorna o numero de valores de todas as chaves da hashtabela.


def insercao(
    hash_table, chave, valor
):  # Cria uma função de inserir com os atributos hashtabela, valorChave e valor.
	hash_chave= hash(chave) % len(hash_table)
	chave_existe = False
	numero = hash_table[hash_chave]	
	for i, cv in enumerate(numero):
		c = cv
		if chave ==c:
			chave_existe = True 
			break
	if chave_existe:
		numero[i] = (valor)
	else:
		numero.append(valor)


def busca(hash_table, chave):  # Cria uma função com nome busca com os atributos hash_table e chave.
  return hash_table[chave] #retorna o valor da hashTable
    

def remove(hash_table, chave): 
  if len(hash_table) < chave:## Verifica se a chave é maior que o hashTable
    print("Essa chave não existe.")
  else:
    for i in range(len(hash_table[chave])): ##Percorre a hashTable até o valor que deseja ser removido
      hash_table[chave].pop(0) #Remove o valor
    print(f"Chave {chave} removida.")

def contarEspacoBranco(
    hashtabela
):  # Cria uma função com o nome display_hash com o atributo hashtabela.
    count = 0  # Contador definido com valor inicial 0.
    for i in range(len(hashtabela)):  # Percorre a hashtabela
        if len(hashtabela[i]) == 0:
            count += 1  # Percorre os itens da hashtabela.
    print("\n\nPorcentagem de espaço ocioso: ",
          count / 1500 * 100,
          "%.",
          sep="")  # Imprime a porcentagem de tempo ocioso.


spotify = pd.read_csv(
    "file.csv", encoding='utf8'
)  # A função read_csv é utilizada para ler o "file.csv" em utf-8.
for linha in spotify.index:  # Percorre cada linha do csv.
    insercao(Hashtabela,spotify['streams'][linha], spotify['title'][linha])
    #Utiliza a função insercao criada para inserir a coluna "title" junto com as streams na hashtabela.



colisao = 0  #Cria uma variavel colisao com valor igual a 0.
for _ in range(1000):  ## Percorre todo o vetor
    tabela = {}  ## É usado para armazenar os valores hash já vistos.
    for _ in range(16):
        rBinario = os.urandom(500)
        resultados = hashlib.md5(rBinario).digest(
        )  ##Retorna os dados codificados em formato de byte.
        resultados = resultados[:1]
        if resultados not in tabela:  ##Se o resultado não está presente em um valor hash já visto, um valor binário aleatório é atribuito
            tabela[
                resultados] = rBinario  #Atribui um valor aleatório a um valor do dado codificado em byte
        else:
            colisao += 1  ##Se o valor já existe, soma um a colisão
            print("\n")
            break


imprimirHash(Hashtabela)
contarEspacoBranco(Hashtabela)  #Chama a função contarEspacoBranco.
print("O número de colisões é: ",colisao," e porcentagem de colisão é ", colisao * 100 / 1000, "%\n", sep="") #Imprime a porcentagem de colisão.
remove(Hashtabela, 980) #Chama a função remove.
print("\nEncontrei: ", busca(Hashtabela, 990)) #Imprime a função busca.