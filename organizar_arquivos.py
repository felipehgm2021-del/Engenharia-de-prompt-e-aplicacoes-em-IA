import os
import shutil

PASTAS_POR_EXTENSAO = {
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".gif": "Imagens",
    ".pdf": "PDFs",
    ".txt": "Textos",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".xls": "Planilhas",
    ".xlsx": "Planilhas",
    ".mp3": "Musicas",
    ".mp4": "Videos",
    ".zip": "Compactados",
    ".rar": "Compactados",
}


def organizar_arquivos(diretorio: str) -> None:
    if not os.path.isdir(diretorio):
        print(f"Erro: o diretório '{diretorio}' não existe.")
        return

    arquivos_movidos = 0
    arquivos_ignorados = 0

    for nome_arquivo in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, nome_arquivo)

        if not os.path.isfile(caminho_completo):
            continue

        _, extensao = os.path.splitext(nome_arquivo)
        extensao = extensao.lower()

        nome_pasta = PASTAS_POR_EXTENSAO.get(extensao, "Outros")

        pasta_destino = os.path.join(diretorio, nome_pasta)
        os.makedirs(pasta_destino, exist_ok=True)

        destino = os.path.join(pasta_destino, nome_arquivo)

        if os.path.exists(destino):
            base, ext = os.path.splitext(nome_arquivo)
            contador = 1
            while os.path.exists(destino):
                novo_nome = f"{base}_{contador}{ext}"
                destino = os.path.join(pasta_destino, novo_nome)
                contador += 1

        shutil.move(caminho_completo, destino)
        print(f"Movido: {nome_arquivo} → {nome_pasta}/")
        arquivos_movidos += 1

    if arquivos_movidos == 0 and arquivos_ignorados == 0:
        print("Nenhum arquivo encontrado para organizar.")
    else:
        print(f"\nConcluído! {arquivos_movidos} arquivo(s) organizado(s).")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        diretorio_alvo = sys.argv[1]
    else:
        diretorio_alvo = input("Digite o caminho do diretório a organizar: ").strip()

    organizar_arquivos(diretorio_alvo)
