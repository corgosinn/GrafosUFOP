from time import time
import grafo
import time

# Recebe nome do arquivo
arq = input("Digite o nome do arquivo: ")
# Recebe Origem e Destino
verticeOrigem = int(input("Origem: "))
verticeDestino = int(input("Destino: "))
# Inicia o time
inicioTime = time.time()

# Lê o grafo
g1 = grafo.Grafo()
arqNome = "grafos/" + arq  # Procurar dentro da pasta grafos
g1.ler_arquivo(arqNome)
print("Processando...")

# Processa o caminho atravez dos algoritmos
caminho = g1.definir_algoritmo(0)


# Printa na tela


print(f"Caminho: {caminho}")
print(f"{time.time()-inicioTime:.4f} segundos")
