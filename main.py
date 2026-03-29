import os
import shutil

pasta = "C:/Users/YanFSC/Downloads/Telegram Desktop"

# Dicionário: extensão → nome da pasta
TIPOS = {
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".webp": "Imagens",

    ".xlsx": "Documentos",
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".pptx": "Documentos",
    ".txt": "Documentos",

    ".mp4": "Videos",
    ".avi": "Videos",

    ".mp3": "Audio",
    ".aac": "Audio",

    ".exe": "Softwares",
    ".msi": "Softwares",

    ".rar": "Compactados",
    ".7z": "Compactados",
    ".zip": "Compactados",

    ".brd": "Boardviews",
    ".bdv": "Boardviews",
    ".bv": "Boardviews",
    ".bv2": "Boardviews",
    ".asc": "Boardviews",
    ".cad": "Boardviews",
    ".cst": "Boardviews",
    ".gr": "Boardviews",
    ".f2b": "Boardviews",
    ".fz": "Boardviews",
}

arquivos = os.listdir(pasta)

for arquivo in arquivos:
    caminho_arquivo = os.path.join(pasta, arquivo)

    if os.path.isdir(caminho_arquivo):
        continue

    nome, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()

    if extensao in TIPOS:
        nome_pasta = TIPOS[extensao]

        caminho_pasta = os.path.join(pasta, nome_pasta)

        # cria pasta se não existir
        if not os.path.exists(caminho_pasta):
            os.mkdir(caminho_pasta)

        novo_caminho = os.path.join(caminho_pasta, arquivo)

        shutil.move(caminho_arquivo, novo_caminho)

        print(f"{arquivo} → {nome_pasta}")