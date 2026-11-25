import base64, sys, re
exec(open("build.py").read().split("fonts=[ff(")[0])  # helpers
fonts=[ff("Barlow Condensed",f"{F}/barlow-condensed/files/barlow-condensed-{s}-800-normal.woff2",800,u) for s,u in [("latin",LAT),("latin-ext",EXT)]]
for w in [400,500,600,700,800]:
    for s_,u in [("latin",LAT),("latin-ext",EXT)]:
        fonts.append(ff("Inter",f"{F}/inter/files/inter-{s_}-{w}-normal.woff2",w,u))
imgs=dict(a.split("=",1) for a in sys.argv[1:])
T=7
CSS='''
:root{--L:#D6FF68;--O:#4F6B0A;--D:#0F100C;--W:#F6F6F1}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#2a2a2a;padding:40px 0;font-family:'Inter',sans-serif}
.wrap{display:flex;flex-direction:column;align-items:center;gap:20px}
.s{width:1080px;height:1350px;position:relative;overflow:hidden}
.hd{position:absolute;top:44px;left:64px;right:64px;display:flex;justify-content:space-between;font-size:17px;font-weight:600;letter-spacing:.2px;z-index:20}
.dark .hd{color:rgba(255,255,255,.55)}.light .hd{color:rgba(15,16,12,.5)}.lime .hd{color:rgba(15,16,12,.6)}
.dots{position:absolute;bottom:52px;left:0;right:0;display:flex;justify-content:center;gap:10px;z-index:20}
.dots i{width:10px;height:10px;border-radius:50%;display:block}
.dark .dots i{background:rgba(255,255,255,.22)}.dark .dots i.on{background:var(--L)}
.light .dots i{background:rgba(15,16,12,.15)}.light .dots i.on{background:var(--D)}
.lime .dots i{background:rgba(15,16,12,.18)}.lime .dots i.on{background:var(--D)}
.dark{background-color:var(--D);background-image:linear-gradient(rgba(248,248,248,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(248,248,248,.035) 1px,transparent 1px);background-size:64px 64px;color:#fff}.light{background:var(--W);color:var(--D)}.lime{background:var(--L);color:var(--D)}
/* capa */
.cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top}
.cover .g{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(0,0,0,.25) 0%,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 40%,rgba(0,0,0,.75) 62%,rgba(0,0,0,.95) 100%)}
.cover .ca{position:absolute;left:48px;right:48px;bottom:110px;text-align:center;z-index:10}
.badge{display:inline-flex;align-items:center;gap:12px;background:rgba(255,255,255,.12);border:1.5px solid rgba(255,255,255,.18);border-radius:60px;padding:10px 24px 10px 10px;margin-bottom:30px;font-size:22px;font-weight:700;color:#fff}
.badge b{width:34px;height:34px;border-radius:50%;background:var(--L);color:var(--D);display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:800}
.ch{font-family:'Barlow Condensed';font-weight:800;font-size:150px;line-height:.9;letter-spacing:-2px;text-transform:uppercase;color:#fff}
.ch em{font-style:normal;color:var(--L)}
.cs{margin-top:30px;font-size:30px;font-weight:700;color:#fff;text-transform:uppercase;letter-spacing:.3px;line-height:1.3}
.cs span{color:var(--L)}
/* internos */
.c{position:absolute;top:150px;left:64px;right:64px;bottom:120px;display:flex;flex-direction:column}
.c.bottom{justify-content:flex-end}
.h{font-size:76px;font-weight:800;line-height:1.08;letter-spacing:-2.2px;margin-bottom:36px}
.dark .h em{font-style:normal;color:var(--L)}.light .h em{font-style:normal;padding:0 .14em;margin:0 -.04em;box-decoration-break:clone;-webkit-box-decoration-break:clone;border-radius:6px}.light .h em.bk{background:var(--D);color:var(--L)}.light .h em.lm{background:var(--L);color:var(--D)}.light .h{line-height:1.22}
.p{font-size:38px;font-weight:500;line-height:1.42;letter-spacing:-.4px}
.dark .p{color:rgba(255,255,255,.7)}.light .p{color:rgba(15,16,12,.68)}.lime .p{color:rgba(15,16,12,.75)}
.p strong{font-weight:800}.dark .p strong{color:#fff}.light .p strong{color:var(--D)}
.p mark{background:none;color:var(--L);font-weight:800}.light .p mark{color:var(--D)}
.ph{width:100%;border-radius:22px;overflow:hidden;margin:6px 0 38px;flex-shrink:0}
.ph img{width:100%;height:100%;object-fit:cover;display:block}
.lab{font-size:24px;font-weight:800;text-decoration:underline;text-underline-offset:6px;margin:34px 0 18px}
.li{font-size:38px;font-weight:600;line-height:1.35;margin-bottom:16px;display:flex;gap:16px}
.li span{font-weight:800}
.dark .li span{color:var(--L)}.light .li span{color:var(--D)}.lime .li span{color:var(--D)}
.big{font-family:'Barlow Condensed';font-weight:800;font-size:260px;line-height:.85;letter-spacing:-6px;color:var(--L);margin-bottom:24px}
.lime .h{font-size:92px}
.kw{display:inline-block;background:var(--L);color:var(--D);font-family:'Barlow Condensed';font-weight:800;font-size:96px;line-height:1;padding:8px 22px 2px;border-radius:10px;margin:8px 0 22px}
'''
def hd(): return '<div class="hd"><span>Powered by HEYCHAMP</span><span>@heychampconsultoria</span><span>2026 ®</span></div>'
def dots(n): return '<div class="dots">'+''.join(f'<i class="{"on" if i==n else ""}"></i>' for i in range(1,T+1))+'</div>'
S=[]
S.append(f'''<div class="s dark cover"><img src="{imgs.get('capa','')}">{'<div class="g"></div>'}{hd()}
<div class="ca"><div class="badge"><b>H</b>@heychampconsultoria</div>
<div class="ch">Tarde demais<br>pra <em>ganhar força?</em></div>
<div class="cs"><span>→</span> Pessoas de 90 anos ficaram 174% mais<br>fortes em 8 semanas</div></div>{dots(1)}</div>''')
S.append(f'''<div class="s light">{hd()}<div class="c"><div class="h">A escada ficou<br><em class="bk">mais&nbsp;alta?</em></div>
<div class="p">Subir escada, carregar as compras, levantar do chão sem apoio. Quando isso começa a pesar, <strong>a culpa quase sempre cai na&nbsp;idade.</strong></div>
<div class="lab">O que pesa primeiro:</div>
<div class="li"><span>✕</span>Escada sem segurar no corrimão</div>
<div class="li"><span>✕</span>Sacola cheia numa mão só</div>
<div class="li"><span>✕</span>Levantar do chão sem apoio</div>
<div class="ph" style="height:330px;margin-top:30px"><img src="{imgs.get('capa','')}" style="object-position:center 78%"></div></div>{dots(2)}</div>''')
S.append(f'''<div class="s dark">{hd()}<div class="c bottom"><div class="big">3% a 5%</div>
<div class="h">O músculo vai embora <em>em&nbsp;silêncio.</em></div>
<div class="p">É o quanto o corpo perde de massa muscular a cada década, a partir dos 30 anos. Sem treino de força, <strong>quem sente primeiro são as&nbsp;pernas.</strong></div></div>{dots(3)}</div>''')
S.append(f'''<div class="s light">{hd()}<div class="c"><div class="h">Aos 90 anos,<br><em class="lm">174% mais&nbsp;fortes.</em></div>
<div class="ph" style="height:600px"><img src="{imgs.get('leg','')}" style="object-position:center 22%"></div>
<div class="p">Um estudo publicado no JAMA em 1990 colocou idosos de cerca de 90 anos pra treinar força com carga alta por 8 semanas. <strong>A força das pernas quase triplicou, em&nbsp;média.</strong></div></div>{dots(4)}</div>''')
S.append(f'''<div class="s dark">{hd()}<div class="c"><div class="ph" style="height:560px"><img src="{imgs.get('remada','')}" style="object-position:center 12%"></div><div class="h">Como começar <em>com&nbsp;segurança.</em></div>
<div class="li"><span>✓</span>Exercícios que respeitam suas articulações</div>
<div class="li"><span>✓</span>Carga que sobe aos poucos e fica anotada</div>
<div class="li"><span>✓</span>Execução corrigida por vídeo pra treinar sem&nbsp;medo</div></div>{dots(5)}</div>''')
S.append(f'''<div class="s lime">{hd()}<div class="c bottom"><div class="h">Força pros próximos 25&nbsp;anos.</div>
<div class="li"><span>→</span>Subir escada sem segurar no corrimão</div>
<div class="li"><span>→</span>Carregar todas as compras de uma vez</div>
<div class="li"><span>→</span>Levantar do chão sem apoio</div></div>{dots(6)}</div>''')
S.append(f'''<div class="s light">{hd()}<div class="c bottom">
<div class="p">Musculação com carga ajustada funciona em qualquer idade. <strong>Quanto antes começar, mais força você&nbsp;guarda.</strong></div>
<div class="h" style="margin:44px 0 0;font-size:96px">Manda pra quem<br><em class="bk">precisa ouvir&nbsp;isso.</em></div>
<div class="p" style="margin-top:14px;font-size:30px">Pai, mãe, tio ou amigo que acha que já passou da hora de&nbsp;treinar.</div></div>{dots(7)}</div>''')
html=f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{''.join(fonts)}{CSS}</style></head><body><div class='wrap'>{''.join(S)}</div></body></html>"
open("carrossel.html","w").write(html)
