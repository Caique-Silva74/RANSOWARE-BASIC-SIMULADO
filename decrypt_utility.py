from cryptography.fernet import Fernet
import os

def carregar_chave():
    return open ("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):
    print(f"Tentando descriptografar: {arquivo}")
    f = Fernet(chave)

    with open(arquivo, 'rb') as file:
        dados = file.read()

    try:
        dados_descriptografados = f.decrypt(dados)
    except Exception as e:
        print(f"ERRO em {arquivo}: {e}")
        return  # pula o arquivo para continuar o resto

    with open(arquivo, 'wb') as file:
        file.write(dados_descriptografados)

    print(f"OK: {arquivo}")



def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for name in arquivos:
            caminho = os.path.join(raiz, name)
            if name != "ransoware.py" and not name.endswith(".key"):
                lista.append(caminho)
    return lista

def main():
    chave =carregar_chave()
    arquivos = encontrar_arquivos('Meus_arquivos')
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
    print('ARQUIVOS RESTAURADOS COM SUCESSO')

if __name__ == "__main__":
    main()
