import sys
from pathlib import Path

from pypdf import PdfReader

ARQUIVO_SAIDA = "contagem_paginas.txt"


def contar_paginas(caminho_pdf: Path) -> int | None:
    """Retorna o número de páginas do PDF, ou None se não conseguir ler."""
    try:
        leitor = PdfReader(str(caminho_pdf))
        if leitor.is_encrypted:
            leitor.decrypt("")
        return len(leitor.pages)
    except Exception as erro:
        print(f"[ERRO] Não foi possível ler '{caminho_pdf.name}': {erro}")
        return None


def main() -> None:
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
    else:
        entrada = input("Digite o caminho da pasta com os PDFs: ")

    entrada = entrada.strip().strip('"').strip("'")
    if not entrada:
        print("Nenhum caminho informado. Nada foi contado.")
        sys.exit(1)

    pasta = Path(entrada)

    if not pasta.is_dir():
        print(f"Pasta não encontrada: {pasta}")
        sys.exit(1)

    pdfs = sorted(
        (p for p in pasta.iterdir() if p.is_file() and p.suffix.lower() == ".pdf"),
        key=lambda p: p.name.lower(),
    )

    if not pdfs:
        print(f"Nenhum PDF encontrado em: {pasta}")
        sys.exit(0)

    linhas = []
    total = 0

    for pdf in pdfs:
        paginas = contar_paginas(pdf)
        if paginas is None:
            linhas.append(f"{pdf.stem} - erro ao ler")
            continue
        total += paginas
        linhas.append(f"{pdf.stem} {paginas} pag.")

    linhas.append("")
    linhas.append(f"total: {total} pag.")

    caminho_saida = pasta / ARQUIVO_SAIDA
    caminho_saida.write_text("\n".join(linhas), encoding="utf-8")

    print("\n".join(linhas))
    print(f"\nArquivo gerado: {caminho_saida}")


if __name__ == "__main__":
    main()