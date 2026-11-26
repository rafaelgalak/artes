import base64,os
P=os.getcwd()
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
TG='/usr/share/texmf/fonts/opentype/public/tex-gyre/'
N='node_modules/@fontsource/'
def ff(fam,p,w=400,st='normal',fmt='woff2'):
    f={'otf':'opentype','woff2':'woff2'}[fmt]
    return f"@font-face{{font-family:'{fam}';src:url(data:font/{fmt};base64,{b64(p)}) format('{f}');font-weight:{w};font-style:{st}}}"
F=''.join([ff('Heros',TG+'texgyreheros-regular.otf',400,fmt='otf'),ff('Heros',TG+'texgyreheros-bold.otf',700,fmt='otf'),
 ff('HerosCn',TG+'texgyreheroscn-bold.otf',700,fmt='otf'),ff('Scholar','Scholar-Italic.otf',400,fmt='otf'),
 ff('Mono',N+'space-mono/files/space-mono-latin-400-normal.woff2'),
 ff('Serif',N+'instrument-serif/files/instrument-serif-latin-400-normal.woff2'),ff('Serif',N+'instrument-serif/files/instrument-serif-latin-400-italic.woff2',400,'italic'),
 ff('Courier',N+'courier-prime/files/courier-prime-latin-400-normal.woff2')])
L='#D6FF68';D='#171717'
GRAIN='<div class="grain"></div>'
def img(f,pos='center',flt='saturate(.8) contrast(1.06)'): return f'<img class="bg" src="file://{P}/{f}" style="object-position:{pos};filter:{flt}">'
def hd(n,t,dark=True): return f'<div class="hd" style="color:{"rgba(255,255,255,.75)" if dark else "rgba(23,23,23,.55)"}"><span>{t} · 0{n}</span><span>@_RAFAELGALAK</span></div>'
FOLDER='<svg width="96" height="78" viewBox="0 0 48 39"><path d="M2 6a3 3 0 0 1 3-3h12l4 4h22a3 3 0 0 1 3 3v24a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3z" fill="#8FB8FF"/><path d="M2 12h44v22a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3z" fill="#A9C9FF"/></svg>'
CURSOR='<svg width="54" height="64" viewBox="0 0 18 22"><path d="M1 1l15 9-7 1.5L6 20z" fill="#fff" stroke="#171717" stroke-width="1.4" stroke-linejoin="round"/></svg>'
CLIP='<svg width="70" height="170" viewBox="0 0 30 72"><path d="M10 60V12a8 8 0 0 1 16 0v46a12 12 0 0 1-24 0V18" fill="none" stroke="#9A9A9A" stroke-width="3.2" stroke-linecap="round"/></svg>'
def barcode(w=220,h=60,c='#fff'):
    import random;random.seed(7);x=0;r=''
    while x<w:
        bw=random.choice([2,2,3,5,7]);r+=f'<rect x="{x}" y="0" width="{bw}" height="{h}" fill="{c}"/>';x+=bw+random.choice([2,3,4])
    return f'<svg width="{w}" height="{h}">{r}</svg>'
css=f"""*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#222;padding:30px;display:flex;flex-direction:column;gap:30px;align-items:center}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;background:{D};color:#fff;font-family:Heros}}
.s img.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.grain{{position:absolute;inset:0;opacity:.08;mix-blend-mode:overlay;pointer-events:none;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/></filter><rect width='200' height='200' filter='url(%23n)'/></svg>")}}
.hd{{position:absolute;top:64px;left:72px;right:72px;display:flex;justify-content:space-between;font:400 21px Mono;letter-spacing:3px;z-index:5}}
.dim{{position:absolute;inset:0;background:rgba(10,10,10,.25)}}
/* A etiquetas */
.lab{{position:absolute;background:#F4F4F1;color:{D};font:700 40px/1.15 Heros;letter-spacing:-1px;padding:14px 20px;box-shadow:0 10px 30px rgba(0,0,0,.3)}}
/* B desktop */
.desk .fd{{position:absolute;left:72px;display:flex;flex-direction:column;align-items:center;gap:8px;font:400 22px Heros;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.6)}}
.win{{position:absolute;background:#F4F4F1;border-radius:18px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.5)}}
.win .bar{{height:46px;background:#E4E4DF;display:flex;align-items:center;gap:10px;padding:0 18px}}.win .bar i{{width:14px;height:14px;border-radius:50%;background:#FF5F57}}.win .bar i:nth-child(2){{background:#FEBC2E}}.win .bar i:nth-child(3){{background:#28C840}}
.note{{position:absolute;background:#FFF8C5;color:{D};border-radius:14px;box-shadow:0 20px 50px rgba(0,0,0,.35);overflow:hidden}}
.note .t{{background:#F7E98E;font:700 22px Heros;padding:12px 20px;color:#8A7300}}.note .b{{padding:22px 24px;font:400 36px/1.3 Heros}}
/* C sticker */
.stk{{position:absolute;background:{D};color:{L};font:700 70px/1 Heros;letter-spacing:-3px;padding:16px 26px 20px;transform:rotate(-4deg);box-shadow:0 12px 30px rgba(0,0,0,.4)}}
.dash{{position:absolute;border:3px dashed #fff;padding:26px 34px;font:400 64px/1.1 Scholar;color:#fff;transform:rotate(2deg)}}
/* D mono */
.md .tag{{position:absolute;left:72px;top:250px;font:400 30px Mono;letter-spacing:2px;color:{L}}}
.md .h{{position:absolute;left:66px;right:60px;top:320px;font:700 150px/.88 HerosCn;letter-spacing:-4px;text-transform:uppercase}}
.md .p{{position:absolute;left:72px;width:560px;top:920px;font:400 30px/1.45 Heros;color:rgba(255,255,255,.7)}}
/* E bilhete */
.paper{{position:absolute;background:#F2EEE6;color:{D};box-shadow:0 30px 60px rgba(0,0,0,.45)}}
.paper .tx{{font:400 44px/1.35 Courier}}
/* F chat */
.chat{{position:absolute;left:70px;right:70px;display:flex;flex-direction:column;gap:18px}}
.bub{{max-width:86%;padding:22px 30px;border-radius:40px;font:400 38px/1.25 Heros}}
.in{{align-self:flex-start;background:rgba(60,60,60,.85);color:#fff;border-bottom-left-radius:10px}}
.out{{align-self:flex-end;background:{L};color:{D};border-bottom-right-radius:10px;font-weight:700}}
.ts{{align-self:center;font:400 22px Heros;color:rgba(255,255,255,.7)}}
/* G serif */
.sv .t{{position:absolute;left:60px;right:60px;top:300px;text-align:center;font:400 120px/.95 Serif;letter-spacing:-2px;text-shadow:0 4px 30px rgba(0,0,0,.35)}}
.sv .t em{{font-style:italic;color:{L}}}
.sv .sm{{position:absolute;left:0;right:0;top:720px;text-align:center;font:400 22px Mono;letter-spacing:6px}}
/* H ticket */
.tk{{position:absolute;left:110px;right:110px;top:300px;height:720px;background:#F4F4F1;color:{D};border-radius:28px;-webkit-mask:radial-gradient(circle at 0 470px,transparent 34px,#000 35px) left/51% 100% no-repeat,radial-gradient(circle at 100% 470px,transparent 34px,#000 35px) right/51% 100% no-repeat}}
.tk .top{{padding:56px 60px 0}}.tk .k{{font:400 22px Mono;letter-spacing:4px;color:rgba(23,23,23,.55)}}
.tk .h{{font:700 92px/.92 Heros;letter-spacing:-4px;margin-top:22px;text-transform:uppercase}}.tk .h em{{font:400 84px Scholar;text-transform:none;letter-spacing:-1px}}
.tk .perf{{position:absolute;left:50px;right:50px;top:470px;border-top:3px dashed rgba(23,23,23,.25)}}
.tk .bot{{position:absolute;left:60px;right:60px;top:520px;display:flex;justify-content:space-between;align-items:flex-end}}
.tk .bot div{{font:400 24px/1.6 Mono;letter-spacing:2px}}
"""
S=[
# A etiquetas
f'<div class="s">{img("dorsal.jpg","center 45%")}<div class="dim"></div>{hd(1,"ETIQUETAS")}<div class="lab" style="left:80px;top:300px">nós somos falhos,</div><div class="lab" style="left:330px;top:600px;transform:rotate(-2deg)">mas não somos falsos,</div><div class="lab" style="left:90px;top:930px;transform:rotate(1.5deg);background:{L}">e isso já nos diferencia<br>de muita gente.</div>{GRAIN}</div>',
# B desktop
f'<div class="s desk">{img("blur.jpg")}<div class="dim"></div>{hd(2,"DESKTOP")}<div class="fd" style="top:180px">{FOLDER}treino</div><div class="fd" style="top:330px">{FOLDER}dieta</div><div class="fd" style="top:480px">{FOLDER}mentalidade</div><div class="win" style="left:290px;right:70px;top:200px;height:640px"><div class="bar"><i></i><i></i><i></i></div><img src="file://{P}/s_face.jpg" style="width:100%;height:594px;object-fit:cover;object-position:center 35%"></div><div class="note" style="left:120px;right:240px;top:880px"><div class="t">‹ Notas</div><div class="b">tô off, se precisar de ajuda faz que nem eu, se vira sozinho.</div></div><div style="position:absolute;left:640px;top:1110px">{CURSOR}</div>{GRAIN}</div>',
# C sticker
f'<div class="s">{img("f_selfie.jpg","center 30%")}<div class="dim"></div>{hd(3,"STICKER")}<div class="stk" style="left:80px;top:250px;font-size:52px;line-height:1.08">fica fraco pra você ver<br>se você vale alguma coisa,</div><div class="dash" style="left:110px;top:500px">a vida é uma troca<br>de interesse sinistra.</div><div style="position:absolute;left:760px;top:640px">{CURSOR}</div>{GRAIN}</div>',
# D mono + condensado
f'<div class="s md">{hd(4,"MONO")}<div class="tag">[ sem achismo ]</div><div class="h">Me conduz Deus, eu quero a vida que conversamos.</div><div style="position:absolute;left:72px;bottom:80px">{barcode()}</div><div style="position:absolute;right:72px;bottom:86px;font:400 22px Mono;letter-spacing:3px;color:rgba(255,255,255,.6)">EST. 2026</div>{GRAIN}</div>',
# E bilhete
f'<div class="s">{img("blur.jpg")}<div class="dim"></div>{hd(5,"BILHETE")}<div class="paper" style="left:130px;right:130px;top:300px;height:760px;transform:rotate(-2deg);padding:110px 80px"><div style="position:absolute;left:90px;top:-60px">{CLIP}</div><div class="tx">em algum momento vão tentar te convencer que você sonha alto demais, é importante que você não ouça e siga em frente.<br><br><span style="font-size:30px;opacity:.6">gypsy warrior</span></div></div>{GRAIN}</div>',
# F chat
f'<div class="s">{img("dorsal.jpg","center 40%","saturate(.7) brightness(.55)")}{hd(6,"CHAT")}<div class="chat" style="top:360px"><div class="ts">Hoje 06:12</div><div class="bub out">tô off,</div><div class="bub out">se precisar de ajuda faz que nem eu,</div><div class="bub out">se vira sozinho.</div><div class="ts" style="align-self:flex-end">Lida</div></div>{GRAIN}</div>',
# G serif
f'<div class="s sv">{img("s_face.jpg","center 30%","saturate(.75) contrast(1.05) brightness(.8)")}<div class="dim"></div>{hd(7,"SERIF")}<div class="t">Me conduz Deus,<br>eu quero <em>a vida<br>que conversamos.</em></div><div class="sm">SEM ACHISMO · 2026</div>{GRAIN}</div>',
# H ticket
f'<div class="s" style="background:#0E0E0E">{hd(8,"TICKET")}<div class="tk"><div class="top"><div class="k">ADMIT ONE · SEM ACHISMO</div><div class="h" style="font-size:72px">Nós somos falhos, mas não somos falsos, <em style="font-size:62px">e isso já nos diferencia de muita gente.</em></div></div><div class="perf"></div><div class="bot"><div>EST.<br>2026</div><div>@_RAFAEL<br>GALAK</div><div>{barcode(180,70,"#171717")}</div></div></div>{GRAIN}</div>',
]
open('banco.html','w').write(f"<html><head><meta charset=utf-8><style>{F}{css}</style></head><body>{''.join(S)}</body></html>")
