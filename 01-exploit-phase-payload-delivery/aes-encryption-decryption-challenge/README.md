# Sistema de Criptografia e Descriptografia AES

## 🛠️ Ferramentas Necessárias
- 📂 Python 3  
- 🔒 Biblioteca `pyaes`  
- 💻 **Testado no Kali Linux**

---

## 🔐 Criptografando um Arquivo

1. **Abrir o Arquivo:**  
   Carregar o arquivo original (`teste.txt`) no modo binário:
   ```python
   file = open("teste.txt", "rb")
   file_data = file.read()
   file.close()
   ```

2. **Remover o Arquivo Original:**  
   Apagar o arquivo para evitar duplicatas:
   ```python
   os.remove("teste.txt")
   ```

3. **Configurar a Chave de Criptografia:**  
   Definir uma chave AES de 16, 24 ou 32 bytes no modo CTR:
   ```python
   key = b"testeransomwares"
   aes = pyaes.AESModeOfOperationCTR(key)
   ```

4. **Criptografar os Dados:**  
   Converter o conteúdo do arquivo para um formato seguro:
   ```python
   crypto_data = aes.encrypt(file_data)
   ```

5. **Salvar o Arquivo Criptografado:**  
   Escrever os dados criptografados em um novo arquivo:
   ```python
   new_file = open("teste.txt.ransomwaretroll", "wb")
   new_file.write(crypto_data)
   new_file.close()
   ```

---

## 🔓 Descriptografando um Arquivo

1. **Abrir o Arquivo Criptografado:**  
   Carregar o arquivo protegido (`teste.txt.ransomwaretroll`):
   ```python
   file = open("teste.txt.ransomwaretroll", "rb")
   file_data = file.read()
   file.close()
   ```

2. **Configurar a Chave de Descriptografia:**  
   Usar a mesma chave para reverter o processo de criptografia:
   ```python
   key = b"testeransomwares"
   aes = pyaes.AESModeOfOperationCTR(key)
   decrypt_data = aes.decrypt(file_data)
   ```

3. **Remover o Arquivo Criptografado:**  
   Apagar o arquivo criptografado:
   ```python
   os.remove("teste.txt.ransomwaretroll")
   ```

4. **Criar o Arquivo Descriptografado:**  
   Escrever os dados recuperados em um novo arquivo:
   ```python
   new_file = open("Teste.txt", "wb")
   new_file.write(decrypt_data)
   new_file.close()
   ```

---

## ⚠️ Atenção
Este projeto é apenas para fins educacionais. Não utilize para fins maliciosos.

## 📊 Resultados
Este script foi **testado no Kali Linux** e funciona perfeitamente para proteger ou recuperar arquivos utilizando o padrão AES. Use com responsabilidade!
