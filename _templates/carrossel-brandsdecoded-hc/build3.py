import sys
src=open("build2.py").read()
exec(src.split("imgs=dict")[0])  # fonts (Barlow 800 + Inter)
imgs=dict(a.split("=",1) for a in sys.argv[1:])
T=8
GRID="background-image:linear-gradient(rgba(248,248,248,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(248,248,248,.035) 1px,transparent 1px);background-size:64px 64px;"
CSS='''
:root{--L:#D6FF68;--D:#0F100C;--W:#F6F6F1}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#2a2a2a;padding:40px 0;font-family:'Inter',sans-serif}
.wrap{display:flex;flex-direction:column;align-items:center;gap:20px}
.s{width:1080px;height:1350px;position:relative;overflow:hidden}
.dark{background-color:var(--D);'''+GRID+'''color:#fff}.light{background-color:var(--W);background-image:linear-gradient(rgba(15,16,12,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(15,16,12,.06) 1px,transparent 1px);background-size:64px 64px;color:var(--D)}.onph{background-color:var(--D);'''+GRID+'''color:#fff}.lime{background-color:var(--L);background-image:linear-gradient(rgba(15,16,12,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(15,16,12,.08) 1px,transparent 1px);background-size:64px 64px;color:var(--D)}
.hd{position:absolute;top:44px;left:64px;right:64px;display:flex;justify-content:space-between;font-size:17px;font-weight:600;z-index:30}
.dark .hd,.onph .hd{color:rgba(255,255,255,.6)}.light .hd{color:rgba(15,16,12,.5)}.lime .hd{color:rgba(15,16,12,.6)}
.dots{position:absolute;bottom:52px;left:0;right:0;display:flex;justify-content:center;gap:10px;z-index:30}
.dots i{width:10px;height:10px;border-radius:50%;display:block;background:rgba(127,127,127,.35)}
.dark .dots i.on,.onph .dots i.on{background:var(--L)}.light .dots i.on,.lime .dots i.on{background:var(--D)}
.h{font-size:72px;font-weight:800;line-height:1.1;letter-spacing:-2px}
.dark .h em,.onph .h em{font-style:normal;color:var(--L)}
.light .h em{font-style:normal;padding:0 .14em;border-radius:6px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.light .h em.bk{background:var(--D);color:var(--L)}.light .h em.lm{background:var(--L);color:var(--D)}
.light .h{line-height:1.22}
.p{font-size:36px;font-weight:500;line-height:1.42;letter-spacing:-.4px;margin-top:28px}
.dark .p,.onph .p{color:rgba(255,255,255,.75)}.light .p{color:rgba(15,16,12,.68)}.lime .p{color:rgba(15,16,12,.75)}
.p strong{font-weight:800}.dark .p strong,.onph .p strong{color:#fff}.light .p strong,.lime .p strong{color:var(--D)}
.tag{font-size:18px;font-weight:800;letter-spacing:3px;text-transform:uppercase;margin-bottom:22px}
.dark .tag,.onph .tag{color:var(--L)}.light .tag,.lime .tag{color:rgba(15,16,12,.55)}
.fill{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
/* capa */
.g1{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(0,0,0,.3) 0%,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 40%,rgba(0,0,0,.75) 62%,rgba(0,0,0,.95) 100%)}
.ca{position:absolute;left:48px;right:48px;bottom:110px;text-align:center;z-index:10}
.badge{display:inline-flex;align-items:center;gap:12px;background:rgba(255,255,255,.12);border:1.5px solid rgba(255,255,255,.18);border-radius:60px;padding:10px 24px 10px 10px;margin-bottom:30px;font-size:22px;font-weight:700;color:#fff}
.badge b{width:34px;height:34px;border-radius:50%;background:var(--L);color:var(--D);display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:800}
.ch{font-family:'Barlow Condensed';font-weight:800;font-size:150px;line-height:.9;letter-spacing:-2px;text-transform:uppercase;color:#fff}
.ch em{font-style:normal;color:var(--L)}
.cs{margin-top:30px;font-size:30px;font-weight:700;color:#fff;text-transform:uppercase;letter-spacing:.3px;line-height:1.3}.cs span{color:var(--L)}
/* foto topo */
.top{position:absolute;top:0;left:0;right:0;height:660px;overflow:hidden}
.top img{width:100%;height:100%;object-fit:cover}
.top:after{content:'';position:absolute;inset:0;background:linear-gradient(to bottom,rgba(0,0,0,.45),rgba(0,0,0,0) 25%)}
.below{position:absolute;top:720px;left:64px;right:64px}
/* chart */
.bigstat{font-family:'Barlow Condensed';font-weight:800;font-size:200px;line-height:.85;letter-spacing:-4px}
.chart{display:flex;gap:40px;align-items:flex-end;height:430px;margin-top:40px}
.bar{flex:1;display:flex;flex-direction:column;justify-content:flex-end;height:100%}
.bar .v{font-family:'Barlow Condensed';font-weight:800;font-size:64px;line-height:1;margin-bottom:12px}
.bar .b{border-radius:14px 14px 0 0}
.bar .l{font-size:24px;font-weight:700;margin-top:14px}
/* polaroid */
.pol{position:absolute;background:#F8F8F8;padding:20px 20px 26px;box-shadow:0 30px 60px rgba(0,0,0,.55)}
.pol img{display:block;object-fit:cover}
.pol p{margin:16px 4px 0;font-size:26px;font-weight:600;color:var(--D)}
.tape{position:absolute;width:170px;height:46px;background:rgba(214,255,104,.85)}
/* table */
.tb{margin-top:40px;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.th{font-size:22px;font-weight:800;letter-spacing:1px;text-transform:uppercase;padding:0 4px 6px;border-bottom:3px solid var(--D)}
.cl{background:#fff;border:2px solid rgba(15,16,12,.1);border-radius:14px;padding:26px 26px;font-size:28px;font-weight:600;line-height:1.3;color:rgba(15,16,12,.6);min-height:122px;display:flex;align-items:center}
.cr{background:var(--L);border-radius:14px;padding:26px 26px;font-size:28px;font-weight:800;line-height:1.3;color:var(--D);min-height:122px;display:flex;align-items:center}
/* full photo text */
.g2{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 18%,rgba(0,0,0,0) 40%,rgba(15,16,12,.97) 62%,rgba(15,16,12,.93) 100%)}
.bt{position:absolute;left:64px;right:64px;bottom:130px;z-index:10}
/* mac window */
.win{background:#1b1c17;border:1.5px solid #34342f;border-radius:22px;box-shadow:0 30px 70px rgba(0,0,0,.5);margin-top:50px}
.wb{display:flex;align-items:center;gap:12px;height:64px;padding:0 26px;border-bottom:1.5px solid #34342f}
.wb i{width:16px;height:16px;border-radius:50%;background:#6b6b63;display:block}.wb i:first-child{background:var(--L)}
.wb span{margin-left:12px;font-size:20px;font-weight:600;color:#a3a39a}
.wr{display:flex;gap:28px;align-items:center;padding:34px 36px;border-top:1.5px solid #34342f}
.wr:first-of-type{border-top:none}
.wr b{font-family:'Barlow Condensed';font-weight:800;font-size:60px;color:var(--L);line-height:1;width:70px}
.wr span{font-size:34px;font-weight:600;line-height:1.3}
/* cta */
.cbox{margin-top:46px;background:#fff;border:2px solid rgba(15,16,12,.1);border-radius:80px;display:flex;align-items:center;gap:20px;padding:14px 14px 14px 36px;box-shadow:0 20px 40px rgba(0,0,0,.08)}
.cbox .t{flex:1;font-size:30px;font-weight:600;color:rgba(15,16,12,.4)}.cbox .t b{color:var(--D);font-weight:800}
.cbox .go{width:86px;height:86px;border-radius:50%;background:var(--D);color:var(--L);display:flex;align-items:center;justify-content:center;font-size:42px;font-weight:800}
'''
def hd(): return '<div class="hd"><span>Powered by HEYCHAMP</span><span>@heychampconsultoria</span><span>2026 ®</span></div>'
def dots(n): return '<div class="dots">'+''.join(f'<i class="{"on" if i==n else ""}"></i>' for i in range(1,T+1))+'</div>'
S=[]
S.append(f'''<div class="s onph"><img class="fill" src="{imgs['capa']}" style="object-position:center top"><div class="g1"></div>{hd()}
<div class="ca"><div class="badge"><b>H</b>@heychampconsultoria</div><div class="ch">Tarde demais<br>pra <em>ganhar força?</em></div>
<div class="cs"><span>→</span> Pessoas de 90 anos ficaram 174% mais<br>fortes em 8 semanas</div></div>{dots(1)}</div>''')
S.append(f'''<div class="s light onph-top"><div class="top"><img src="{imgs['capa']}" style="object-position:center 82%"></div><div class="hd" style="color:rgba(255,255,255,.75)"><span>Powered by HEYCHAMP</span><span>@heychampconsultoria</span><span>2026 ®</span></div>
<div class="below"><div class="h">A escada ficou<br><em class="bk">mais&nbsp;alta?</em></div>
<div class="p">Subir escada, carregar as compras, levantar do chão sem apoio. Quando isso começa a pesar, <strong>a culpa quase sempre cai na&nbsp;idade.</strong></div></div>{dots(2)}</div>''')
S.append(f'''<div class="s lime">{hd()}<div style="position:absolute;top:150px;left:64px;right:64px">
<div class="tag">O que acontece</div><div class="h">O músculo vai embora em&nbsp;silêncio.</div>
<div class="p">A partir dos 30 anos, o corpo perde de 3% a 5% da massa muscular <strong>a cada década.</strong></div>
<div class="chart"><div class="bar"><div class="v">100%</div><div class="b" style="height:330px;background:var(--D)"></div><div class="l">30 anos</div></div>
<div class="bar"><div class="v">−9% a −15%</div><div class="b" style="height:290px;background:rgba(15,16,12,.25);border:3px dashed var(--D)"></div><div class="l">60 anos, sem treino de força</div></div></div></div>{dots(3)}</div>''')
S.append(f'''<div class="s dark">{hd()}
<div class="pol" style="top:150px;right:90px;transform:rotate(3deg)"><img src="{imgs['leg']}" style="width:560px;height:600px;object-position:center 20%"><p>leg press, 8 semanas</p>
<div class="tape" style="left:-34px;top:-20px;transform:rotate(-24deg)"></div><div class="tape" style="right:-36px;top:-16px;transform:rotate(26deg)"></div></div>
<div style="position:absolute;left:64px;right:64px;bottom:130px"><div class="tag">A prova</div><div class="h">Aos 90 anos,<br><em>174% mais fortes.</em></div>
<div class="p">Um estudo publicado no JAMA em 1990 colocou idosos de cerca de 90 anos pra treinar força com carga alta por 8 semanas. <strong>A força das pernas quase triplicou, em&nbsp;média.</strong></div></div>{dots(4)}</div>''')
S.append(f'''<div class="s light">{hd()}<div style="position:absolute;top:150px;left:64px;right:64px">
<div class="h">O que muda com<br><em class="lm">treino de força</em></div>
<div class="tb"><div class="th">Sem treino</div><div class="th">Com treino</div>
<div class="cl">Escada com a mão no corrimão</div><div class="cr">Sobe sem precisar de apoio</div>
<div class="cl">Compras divididas em várias viagens</div><div class="cr">Carrega tudo de uma vez</div>
<div class="cl">Levanta do chão se apoiando</div><div class="cr">Levanta sozinho</div>
<div class="cl">Força cai a cada década</div><div class="cr">Força responde em qualquer idade</div></div></div>{dots(5)}</div>''')
S.append(f'''<div class="s onph"><img class="fill" src="{imgs['remada']}" style="object-position:center 0%;height:62%"><div class="g2"></div>{hd()}
<div class="bt"><div class="tag">Na prática</div><div class="h">Como começar<br><em>com segurança.</em></div>
<div class="p">Carga ajustada, progressão e alguém olhando a execução. <strong>É isso que deixa o treino seguro em qualquer&nbsp;idade.</strong></div></div>{dots(6)}</div>''')
S.append(f'''<div class="s dark">{hd()}<div style="position:absolute;left:64px;right:64px;bottom:150px">
<div class="tag">Por onde começar</div><div class="h">Os 3 pontos que<br><em>não podem faltar.</em></div>
<div class="win"><div class="wb"><i></i><i></i><i></i><span>comeco.heychamp</span></div>
<div class="wr"><b>01</b><span>Exercícios que respeitam suas articulações</span></div>
<div class="wr"><b>02</b><span>Carga que sobe aos poucos e fica anotada</span></div>
<div class="wr"><b>03</b><span>Execução corrigida por vídeo</span></div></div></div>{dots(7)}</div>''')
S.append(f'''<div class="s light">{hd()}<div style="position:absolute;left:64px;right:64px;bottom:150px">
<div class="p" style="margin:0 0 40px">Musculação com carga ajustada funciona em qualquer idade. <strong>Quanto antes começar, mais força você&nbsp;guarda.</strong></div>
<div class="h" style="font-size:92px">Manda pra quem<br><em class="bk">precisa ouvir&nbsp;isso.</em></div>
<div class="cbox"><div class="t">Envia pro <b>pai, mãe ou tio</b> que acha que passou da&nbsp;hora</div><div class="go">→</div></div></div>{dots(8)}</div>''')
html=f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{''.join(fonts)}{CSS}</style></head><body><div class='wrap'>{''.join(S)}</div></body></html>"
open("carrossel.html","w").write(html)
