import base64, sys
F="node_modules/@fontsource"
def ff(fam,path,w,ur):
    b=base64.b64encode(open(path,"rb").read()).decode()
    return f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:normal;src:url(data:font/woff2;base64,{b}) format('woff2');unicode-range:{ur}}}"
LAT="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
EXT="U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"
fonts=[ff("Barlow Condensed",f"{F}/barlow-condensed/files/barlow-condensed-{s}-900-normal.woff2",900,u) for s,u in [("latin",LAT),("latin-ext",EXT)]]
for w in [400,500,600,700,800]:
    for s,u in [("latin",LAT),("latin-ext",EXT)]:
        fonts.append(ff("Plus Jakarta Sans",f"{F}/plus-jakarta-sans/files/plus-jakarta-sans-{s}-{w}-normal.woff2",w,u))
CSS=open("style.css").read()
capa_img=sys.argv[1] if len(sys.argv)>1 else ""
T=7
def top(on): return f'<div class="accent-bar{" on-grad" if on=="grad" else ""}"></div><div class="brand-bar on-{on}"><span>HEYCHAMP</span><span>@heychampconsultoria</span><span>2026 ®</span></div>'
def prog(n): return f'<div class="prog"><div class="prog-track"><div class="prog-fill" style="width:{n/T*100:.1f}%"></div></div><span class="prog-num">{n}/{T}</span></div>'
bg = f'<img class="capa-photo" src="{capa_img}">' if capa_img else '<div class="capa-bg"></div>'
S=[]
S.append(f'''<div class="slide slide-capa on-dark">{bg}<div class="capa-grad"></div>{top("dark")}
<div class="capa-headline-area"><div class="capa-badge"><div class="badge-dot">H</div><div class="badge-handle">@heychampconsultoria</div></div>
<div class="capa-headline">Tarde demais pra <em>ganhar força?</em></div>
<div class="capa-sub">Pessoas de 90 anos ficaram 174% mais fortes em 8&nbsp;semanas&nbsp;→</div></div>{prog(1)}</div>''')
S.append(f'''<div class="slide slide-dark on-dark">{top("dark")}<div class="dark-bg-num">02</div><div class="content"><div class="tag">O problema</div>
<div class="dark-h1">A escada ficou<br><em>mais alta?</em></div>
<div class="dark-body">Subir escada, carregar as compras, levantar do chão sem apoio. Quando isso começa a pesar, <strong>a culpa quase sempre cai na&nbsp;idade.</strong></div></div>{prog(2)}</div>''')
S.append(f'''<div class="slide slide-light on-light">{top("light")}<div class="content"><div class="tag">O que acontece</div>
<div class="light-h1">O músculo vai embora<br><em>em silêncio</em></div>
<div class="light-body">A partir dos 30 anos, o corpo perde de 3% a 5% da massa muscular a cada década. Sem treino de força, <strong>quem sente primeiro são as&nbsp;pernas.</strong></div></div>{prog(3)}</div>''')
S.append(f'''<div class="slide slide-dark on-dark">{top("dark")}<div class="dark-bg-num">04</div><div class="content"><div class="tag">A prova</div>
<div class="dark-h1">Aos 90 anos,<br><em>174% mais fortes</em></div>
<div class="dark-body">Um estudo publicado no JAMA em 1990 colocou idosos de cerca de 90 anos pra treinar força com carga alta por 8 semanas. <strong>A força das pernas quase triplicou, em&nbsp;média.</strong></div></div>{prog(4)}</div>''')
S.append(f'''<div class="slide slide-light on-light">{top("light")}<div class="content"><div class="tag">Na prática</div>
<div class="light-h1">Como começar<br><em>com segurança</em></div>
<div class="light-card"><div class="light-body">Exercícios que respeitam suas articulações, carga que sobe aos poucos e fica anotada, e <strong>execução corrigida por vídeo</strong> pra treinar sem&nbsp;medo.</div></div></div>{prog(5)}</div>''')
S.append(f'''<div class="slide slide-grad on-grad">{top("grad")}<div class="grad-bg-num">06</div><div class="content"><div class="tag">Direção</div>
<div class="grad-h1">Força pros próximos 25&nbsp;anos</div>
<div class="grad-row"><span class="grad-arrow">→</span><span class="grad-text"><strong>Subir escada</strong> sem segurar no corrimão.</span></div>
<div class="grad-row"><span class="grad-arrow">→</span><span class="grad-text"><strong>Carregar todas as compras</strong> de uma vez.</span></div>
<div class="grad-row"><span class="grad-arrow">→</span><span class="grad-text"><strong>Levantar do chão</strong> sem apoio.</span></div></div>{prog(6)}</div>''')
S.append(f'''<div class="slide slide-light on-light">{top("light")}<div class="content">
<div class="cta-bridge">Musculação com carga ajustada funciona em qualquer idade. <strong>Quanto antes começar, mais força você&nbsp;guarda.</strong></div>
<div class="cta-headline">Manda pra quem<br><em>precisa ouvir isso</em></div>
<div class="cta-kbox"><div class="cta-kinstr">Pensou em alguém?</div><div class="cta-kword">ENVIA</div><div class="cta-kbenefit">Pai, mãe, tio ou amigo que acha que já passou da hora de&nbsp;treinar.</div></div>
<div class="cta-footer"><div class="cta-footer-dot">H</div><div class="cta-footer-text">@heychampconsultoria · treino com estratégia, sem achismo</div></div></div>{prog(7)}</div>''')
html=f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{''.join(fonts)}{CSS}</style></head><body><div class='slides-wrap'>{''.join(S)}</div></body></html>"
open("carrossel.html","w").write(html)
