import os  # Modulo para manipulacao de arquivos e sistema operacional
import pyaes  # Biblioteca para criptografia e descriptografia AES

# Etapa 1: Abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"  # Nome do arquivo criptografado
file = open(file_name, "rb")  # Abre o arquivo no modo binario de leitura
file_data = file.read()  # Le o conteudo do arquivo
file.close()  # Fecha o arquivo

# Etapa 2: Configurar a chave para descriptografia
key = b"testeransomwares"  # Chave de 16, 24 ou 32 bytes para AES
aes = pyaes.AESModeOfOperationCTR(key)  # Configura AES no modo CTR
decrypt_data = aes.decrypt(file_data)  # Descriptografa os dados do arquivo

# Etapa 3: Remover o arquivo criptografado
os.remove(file_name)  # Apaga o arquivo criptografado

# Etapa 4: Criar o arquivo descriptografado
new_file = "Teste.txt"  # Nome do novo arquivo
new_file = open(new_file, "wb")  # Abre o arquivo no modo binario de escrita
new_file.write(decrypt_data)  # Escreve os dados descriptografados
new_file.close()  # Fecha o arquivo
