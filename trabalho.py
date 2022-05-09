from colorsys import rgb_to_yiq
from time import time
import grafo
import time

# Thiago Corgosinho Silva - 20.2.8117

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
caminho = g1.definir_algoritmo(verticeOrigem, verticeDestino)


# Printa na tela o tempo
print(f"{round(time.time()-inicioTime,4)} segundos")
