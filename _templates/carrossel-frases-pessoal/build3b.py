import base64,os
P=os.getcwd()
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
TG='/usr/share/texmf/fonts/opentype/public/tex-gyre/'
def ff(fam,p,w,fmt): return f"@font-face{{font-family:'{fam}';src:url(data:font/{fmt};base64,{b64(p)}) format('{ {'otf':'opentype','woff2':'woff2'}[fmt]}');font-weight:{w}}}"
F=''.join([ff('Heros',TG+'texgyreheros-regular.otf',400,'otf'),ff('Heros',TG+'texgyreheros-bold.otf',700,'otf'),
 ff('Scholar','Scholar-Italic.otf',400,'otf'),ff('Space Mono','node_modules/@fontsource/space-mono/files/space-mono-latin-400-normal.woff2',400,'woff2')])
GRID="background-image:linear-gradient(rgba(248,248,248,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(248,248,248,.035) 1px,transparent 1px);background-size:64px 64px;"
GRAIN='<div class="grain"></div>'
def hd_old(n,dark=True): return f'<div class="hd {"" if dark else "lt"}"><span>SEM ACHISMO · 0{n}/05</span><span>@_RAFAELGALAK</span></div>'
ARR='<div class="arr">ARRASTE <b>→</b></div>'
def hd(n,dark=True): return f'<div class="hd {"" if dark else "lt"}"><span>SEM ACHISMO · 0{n}/05</span><span>@_RAFAELGALAK</span></div>'
css=f"""*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#222;padding:30px;display:flex;flex-direction:column;gap:30px;align-items:center}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;background:#171717;color:#fff;font-family:Heros}}
.lt{{background:#F4F4F1;color:#171717}}
.grain{{position:absolute;inset:0;opacity:.08;mix-blend-mode:overlay;pointer-events:none;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/></filter><rect width='200' height='200' filter='url(%23n)'/></svg>")}}
.hd{{position:absolute;top:64px;left:72px;right:72px;display:flex;justify-content:space-between;font:400 21px 'Space Mono';letter-spacing:3px;color:rgba(255,255,255,.75);z-index:5}}
.hd.lt{{color:rgba(23,23,23,.55);background:none}}
.arr{{position:absolute;bottom:60px;right:72px;font:400 21px 'Space Mono';letter-spacing:3px;color:rgba(255,255,255,.75);z-index:5}}.arr b{{color:#D6FF68;font-weight:400}}
.lt .arr{{color:rgba(23,23,23,.55)}}.lt .arr b{{color:#171717}}
.sc{{font-family:Scholar;color:#D6FF68;font-weight:400;letter-spacing:-.5px}}
.lt .sc.dk{{color:#171717}}
/* 1 tipografico */
.s1 .bl{{position:absolute;left:72px;right:72px;top:300px}}
.s1 .h{{font:700 132px/.9 Heros;letter-spacing:-7px;text-transform:uppercase}}
.s1 .sc{{font-size:84px;line-height:1.02;margin-top:30px}}
.s1 .me{{position:absolute;left:72px;bottom:56px;display:flex;align-items:center;gap:16px;font:400 21px 'Space Mono';letter-spacing:3px;color:rgba(255,255,255,.75)}}
.s1 .me img{{width:56px;height:56px;border-radius:50%;object-fit:cover}}
/* 2 notificacao */
.s2 .bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:brightness(.55) saturate(.7)}}
.s2 .clk{{position:absolute;left:0;right:0;top:200px;text-align:center}}
.s2 .clk .d{{font:400 30px Heros;color:rgba(255,255,255,.85)}}.s2 .clk .t{{font:700 200px/1 Heros;letter-spacing:-6px;margin-top:6px}}
.s2 .nt{{position:absolute;left:60px;right:60px;top:610px;background:rgba(40,40,40,.62);backdrop-filter:blur(30px);border-radius:44px;padding:34px 38px;display:flex;gap:26px}}
.s2 .nt img{{width:84px;height:84px;border-radius:20px;object-fit:cover;flex-shrink:0}}
.s2 .nt .top{{display:flex;justify-content:space-between;font:700 32px Heros}}.s2 .nt .top span{{font-weight:400;color:rgba(255,255,255,.6);font-size:28px}}
.s2 .nt .msg{{font:400 38px/1.3 Heros;margin-top:8px;color:rgba(255,255,255,.95)}}
/* 3 notas */
.s3 .nb{{position:absolute;left:72px;right:72px;top:190px}}
.s3 .bk{{font:400 30px Heros;color:#B08A00;display:flex;justify-content:space-between}}
.s3 .dt{{text-align:center;font:400 24px Heros;color:#8A8A8A;margin:70px 0 30px}}
.s3 .ttl{{font:700 72px Heros;letter-spacing:-2px;margin-bottom:28px}}
.s3 .tx{{font:400 54px/1.34 Heros;letter-spacing:-1px}}
.s3 .tx mark{{background:#D6FF68;color:#171717;padding:0 6px}}
/* 4 citacao */
.s4 .q{{position:absolute;left:60px;top:190px;font:700 380px/1 Heros;color:#D6FF68;letter-spacing:-20px}}
.s4 .bl{{position:absolute;left:72px;right:72px;top:520px}}
.s4 .h{{font:700 100px/.95 Heros;letter-spacing:-5px;text-transform:uppercase}}
.s4 .sc{{font-size:82px;margin-top:20px}}
/* 5 editorial claro */
.s5 .bl{{position:absolute;left:72px;right:90px;top:250px}}
.s5 .op{{font:400 64px Scholar;color:#171717;margin-bottom:24px}}
.s5 .tx{{font:700 72px/1.2 Heros;letter-spacing:-3.5px}}
.s5 .tx span{{background:#171717;color:#D6FF68;padding:0 10px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.s5 .ln{{width:64px;height:5px;background:#171717;margin:44px 0 22px}}
.v5b{{background:#171717;color:#fff}}
.v5b .op{{color:#D6FF68}}.v5b .tx span{{background:#D6FF68;color:#171717}}.v5b .ln{{background:#D6FF68}}.s5.v5b .cr{{color:rgba(255,255,255,.6)}}
.v5c .card{{position:absolute;left:90px;right:90px;top:250px;bottom:250px;border:2px solid #171717;padding:70px 64px;display:flex;flex-direction:column;justify-content:center;text-align:center}}
.v5c .card .op{{font:400 60px Scholar;margin-bottom:34px}}
.v5c .card .tx{{font:400 62px/1.2 Scholar;letter-spacing:-.5px}}
.v5c .card .cr{{margin-top:44px;font:400 24px 'Space Mono';letter-spacing:4px;color:rgba(23,23,23,.6)}}
.lm{{background:#D6FF68;color:#171717}}
.s5 .sv{{position:absolute;right:72px;bottom:150px;width:120px;height:120px;border-radius:50%;background:#171717;display:flex;align-items:center;justify-content:center}}
.s5 .cr{{font:400 28px 'Space Mono';letter-spacing:2px;color:rgba(23,23,23,.6)}}
"""
S=[
f'<div class="s s1">{hd(1)}<div class="bl"><div class="h">Nós somos falhos, mas não somos falsos,</div><div class="sc">e isso já nos diferencia de muita gente.</div></div><div class="me"><img src="file://{P}/avatar.png">RAFAEL FERREIRA</div>{GRAIN}{ARR}</div>',
f'<div class="s s2"><img class="bg" src="file://{P}/blur.jpg">{hd(2)}<div class="clk"><div class="d">quarta-feira, 26 de novembro</div><div class="t">6:40</div></div><div class="nt"><img src="file://{P}/avatar.png"><div style="flex:1"><div class="top">_rafaelgalak <span>agora</span></div><div class="msg">tô off, se precisar de ajuda faz que nem eu, se vira sozinho.</div></div></div>{GRAIN}{ARR}</div>',
f'<div class="s s3 lt">{hd(3,False)}<div class="nb"><div class="bk"><span>‹ Notas</span><span>Ok</span></div><div class="dt">26 de novembro de 2026, 06:12</div><div class="ttl">pra não esquecer</div><div class="tx">fica fraco pra você ver se você vale alguma coisa, <mark>a vida é uma troca de interesse sinistra.</mark></div></div>{GRAIN}{ARR}</div>',
f'<div class="s s4">{hd(4)}<div class="q">“</div><div class="bl"><div class="h">Me conduz Deus, eu quero</div><div class="sc">a vida que conversamos.</div></div>{GRAIN}{ARR}</div>',
f'<div class="s s5 v5b">{hd(5)}<div class="bl"><div class="op">pra salvar</div><div class="tx">em algum momento vão tentar te convencer que você sonha alto demais, <span>é importante que você não ouça e siga em frente.</span></div><div class="ln"></div><div class="cr">GYPSY WARRIOR</div></div>{GRAIN}</div>',
f'<div class="s s5 lt v5c">{hd(5,False)}<div class="card"><div class="op">pra salvar</div><div class="tx">em algum momento vão tentar te convencer que você sonha alto demais, é importante que você não ouça e siga em frente.</div><div class="cr">GYPSY WARRIOR</div></div>{GRAIN}</div>',
]
open('frases.html','w').write(f"<html><head><meta charset=utf-8><style>{F}{css}</style></head><body>{''.join(S)}</body></html>")
