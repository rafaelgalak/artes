src=open('banco.py').read()
exec(src.split("S=[")[0])
def H(n,dark=True): return f'<div class="hd" style="color:{"rgba(255,255,255,.75)" if dark else "rgba(23,23,23,.55)"}"><span>SEM ACHISMO · 0{n}/05</span><span>@_RAFAELGALAK</span></div>'
ARR='<div style="position:absolute;bottom:60px;right:72px;font:400 21px Mono;letter-spacing:3px;color:rgba(255,255,255,.75);z-index:5">ARRASTE <b style="color:#D6FF68;font-weight:400">→</b></div>'
T1='nós somos falhos,'; T1b='mas não somos falsos,'; T1c='e isso já nos diferencia<br>de muita gente.'
T2='tô off, se precisar de ajuda faz que nem eu, se vira sozinho.'
T3a='fica fraco pra você ver<br>se você vale alguma coisa,'; T3b='a vida é uma troca<br>de interesse sinistra.'
T4='Me conduz Deus,<br>eu quero <em>a vida<br>que conversamos.</em>'
T5='em algum momento vão tentar te convencer que você sonha alto demais, é importante que você não ouça e siga em frente.'
M1=[
f'<div class="s">{img("dorsal.jpg","center 45%")}<div class="dim"></div>{H(1)}<div class="lab" style="left:80px;top:300px">{T1}</div><div class="lab" style="left:330px;top:600px;transform:rotate(-2deg)">{T1b}</div><div class="lab" style="left:90px;top:930px;transform:rotate(1.5deg);background:{L}">{T1c}</div>{GRAIN}{ARR}</div>',
f'<div class="s">{img("blur.jpg","center","brightness(.7) saturate(.7)")}{H(2)}<div class="chat" style="top:420px"><div class="ts">Hoje 06:12</div><div class="bub out">tô off,</div><div class="bub out">se precisar de ajuda faz que nem eu,</div><div class="bub out">se vira sozinho.</div><div class="ts" style="align-self:flex-end">Lida</div></div>{GRAIN}{ARR}</div>',
f'<div class="s">{img("s_face.jpg","center 30%")}<div class="dim"></div>{H(3)}<div class="stk" style="left:80px;top:250px;font-size:52px;line-height:1.08">{T3a}</div><div class="dash" style="left:110px;top:470px">{T3b}</div>{GRAIN}{ARR}</div>',
f'<div class="s sv">{img("f_varanda.jpg","center 40%","saturate(.75) contrast(1.05) brightness(.75)")}<div class="dim"></div>{H(4)}<div class="t">{T4}</div><div class="sm">SEM ACHISMO · 2026</div>{GRAIN}{ARR}</div>',
f'<div class="s">{H(5)}<div class="paper" style="left:130px;right:130px;top:300px;height:760px;transform:rotate(-2deg);padding:110px 80px"><div style="position:absolute;left:90px;top:-60px">{CLIP}</div><div class="tx">{T5}<br><br><span style="font-size:30px;opacity:.6">gypsy warrior</span></div></div>{GRAIN}</div>',
]
M2=[
f'<div class="s" style="background:#0E0E0E">{H(1)}<div class="tk"><div class="top"><div class="k">ADMIT ONE · SEM ACHISMO</div><div class="h" style="font-size:72px">Nós somos falhos, mas não somos falsos, <em style="font-size:62px">e isso já nos diferencia de muita gente.</em></div></div><div class="perf"></div><div class="bot"><div>EST.<br>2026</div><div>@_RAFAEL<br>GALAK</div><div>{barcode(180,70,"#171717")}</div></div></div>{GRAIN}{ARR}</div>',
f'<div class="s desk">{img("blur.jpg")}<div class="dim"></div>{H(2)}<div class="fd" style="top:180px">{FOLDER}treino</div><div class="fd" style="top:330px">{FOLDER}dieta</div><div class="fd" style="top:480px">{FOLDER}mentalidade</div><div class="win" style="left:290px;right:70px;top:200px;height:640px"><div class="bar"><i></i><i></i><i></i></div><img src="file://{P}/s_face.jpg" style="width:100%;height:594px;object-fit:cover;object-position:center 35%"></div><div class="note" style="left:120px;right:240px;top:880px"><div class="t">‹ Notas</div><div class="b">{T2}</div></div><div style="position:absolute;left:640px;top:1110px">{CURSOR}</div>{GRAIN}{ARR}</div>',
f'<div class="s md">{H(3)}<div class="tag">[ sem achismo ]</div><div class="h" style="font-size:118px">Fica fraco pra você ver se você vale alguma coisa,</div><div class="p" style="top:900px;font:400 76px/1.1 Scholar;color:{L};width:800px">a vida é uma troca de interesse sinistra.</div><div style="position:absolute;left:72px;bottom:80px">{barcode()}</div>{GRAIN}{ARR}</div>',
f'<div class="s">{img("f_varanda.jpg","center 40%","saturate(.8) contrast(1.05) brightness(.85)")}<div class="dim"></div>{H(4)}<div class="lab" style="left:80px;top:320px">Me conduz Deus,</div><div class="lab" style="left:300px;top:620px;transform:rotate(-2deg)">eu quero</div><div class="lab" style="left:110px;top:900px;transform:rotate(1.5deg);background:{L}">a vida que conversamos.</div>{GRAIN}{ARR}</div>',
f'<div class="s">{img("dorsal.jpg","center 40%","saturate(.7) brightness(.55)")}{H(5)}<div class="chat" style="top:330px"><div class="ts">Hoje 06:40</div><div class="bub out">em algum momento vão tentar te convencer que você sonha alto demais,</div><div class="bub out">é importante que você não ouça</div><div class="bub out">e siga em frente.</div><div class="ts" style="align-self:flex-end">gypsy warrior</div></div>{GRAIN}</div>',
]
for name,M in (('m1',M1),('m2',M2)):
    open(f'{name}.html','w').write(f"<html><head><meta charset=utf-8><style>{F}{css}</style></head><body>{''.join(M)}</body></html>")
