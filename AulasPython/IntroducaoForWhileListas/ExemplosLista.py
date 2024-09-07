# Inicializamos uma lista de frutas com três elementos
frutas = ["maçã", "banana", "laranja"]

# 1. Usando append para adicionar uma nova fruta ao final da lista
# Isso adiciona "uva" ao final da lista
frutas.append("uva")
fruta_adicionada = "uva"
# A lista agora é: ['maçã', 'banana', 'laranja', 'uva']
print("Após append:", frutas)
print("Fruta adicionada com append:", fruta_adicionada)

# 2. Usando insert para adicionar uma fruta em uma posição específica
# Isso insere "manga" na posição 1, deslocando os elementos subsequentes
frutas.insert(1, "manga")
fruta_inserida = "manga"
# A lista agora é: ['maçã', 'manga', 'banana', 'laranja', 'uva']
print("Após insert:", frutas)
print("Fruta inserida com insert:", fruta_inserida)

# 3. Usando remove para remover a primeira ocorrência de um elemento específico
# Isso remove a primeira ocorrência de "maçã" na lista
frutas.remove("maçã")
fruta_removida = "maçã"
# A lista agora é: ['manga', 'banana', 'laranja', 'uva']
print("Após remove:", frutas)
print("Fruta removida com remove:", fruta_removida)

# 4. Usando pop para remover e retornar o último elemento da lista
# Isso remove o último elemento da lista, que é "uva", e o armazena na variável fruta_removida
fruta_removida_pop = frutas.pop()
# A lista agora é: ['manga', 'banana', 'laranja']
print("Após pop:", frutas)
print("Fruta removida com pop:", fruta_removida_pop)
