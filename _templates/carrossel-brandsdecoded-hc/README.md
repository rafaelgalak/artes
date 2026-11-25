# Carrossel BrandsDecoded × HC (padrão desde 25/11/2026)

Referência: `heychamp/2026-11-25_tarde-demais-forca` (v5 aprovada).

- `build3.py`: monta o carrossel de 8 slides (cada slide num layout). Reaproveita as fontes de `build2.py`, que puxa os helpers de `build.py`.
- `shot.py`: exporta cada slide 1080×1350 com Playwright e confere as fontes.

Uso (na pasta, com `npm i @fontsource/barlow-condensed @fontsource/inter` e playwright instalados):
```
python3 build3.py capa=file:///caminho/capa.jpg leg=file:///caminho/foto2.jpg remada=file:///caminho/foto3.jpg
python3 shot.py   # gera out/01.png ... 08.png
```
Os textos estão dentro do `build3.py`: trocar por slide, e trocar a ordem dos layouts a cada carrossel.
