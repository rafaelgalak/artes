"""Gera manifest.json a partir das pastas heychamp/ e pessoal/.

Cada carrossel é uma pasta: <marca>/<AAAA-MM-DD>_<nome>/
  - imagens (.jpg .jpeg .png .webp), postadas na ordem do nome do arquivo
  - info.json opcional: {"titulo": "...", "status": "rascunho|pronto|postado", "legenda": "..."}
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARCAS = ["heychamp", "pessoal"]
IMG = (".jpg", ".jpeg", ".png", ".webp")


def titulo_da_pasta(nome):
    sem_data = re.sub(r"^\d{4}-\d{2}-\d{2}[_-]?", "", nome)
    return sem_data.replace("_", " ").replace("-", " ").strip().capitalize() or nome


def main():
    carrosseis = []
    for marca in MARCAS:
        base = os.path.join(ROOT, marca)
        if not os.path.isdir(base):
            continue
        for pasta in sorted(os.listdir(base), reverse=True):
            caminho = os.path.join(base, pasta)
            if not os.path.isdir(caminho):
                continue
            slides = sorted(f for f in os.listdir(caminho) if f.lower().endswith(IMG))
            if not slides:
                continue
            info = {}
            info_path = os.path.join(caminho, "info.json")
            if os.path.exists(info_path):
                try:
                    with open(info_path, encoding="utf-8") as fh:
                        info = json.load(fh)
                except ValueError:
                    info = {}
            data = re.match(r"^(\d{4}-\d{2}-\d{2})", pasta)
            carrosseis.append({
                "marca": marca,
                "pasta": f"{marca}/{pasta}",
                "titulo": info.get("titulo") or titulo_da_pasta(pasta),
                "data": data.group(1) if data else "",
                "status": info.get("status", "pronto"),
                "legenda": info.get("legenda", ""),
                "slides": slides,
            })
    with open(os.path.join(ROOT, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump({"carrosseis": carrosseis}, fh, ensure_ascii=False, indent=2)
    print(f"{len(carrosseis)} carrossel(is) no manifest")


if __name__ == "__main__":
    main()
