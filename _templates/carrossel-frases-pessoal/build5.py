import base64,os
P=os.getcwd()
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
TG='/usr/share/texmf/fonts/opentype/public/tex-gyre/'
def ff(fam,p,w,fmt): return f"@font-face{{font-family:'{fam}';src:url(data:font/{fmt};base64,{b64(p)}) format('{ {'otf':'opentype','woff2':'woff2'}[fmt]}');font-weight:{w}}}"
F=''.join([ff('Heros',TG+'texgyreheros-regular.otf',400,'otf'),ff('Heros',TG+'texgyreheros-bold.otf',700,'otf'),
 ff('Scholar','Scholar-Italic.otf',400,'otf'),ff('Space Mono','node_modules/@fontsource/space-mono/files/space-mono-latin-400-normal.woff2',400,'woff2')])
GRID="background-image:linear-gradient(rgba(248,248,248,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(248,248,248,.035) 1px,transparent 1px);background-size:64px 64px;"
GRAIN='<div class="grain"></div>'
def hd(n,dark=True): return f'<div class="hd {"" if dark else "lt"}"><span>SEM ACHISMO · 0{n}/05</span><span>@_RAFAELGALAK</span></div>'
ARR='<div class="arr">ARRASTE <b>→</b></div>'
css=f"""*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#222;padding:30px;display:flex;flex-direction:column;gap:30px;align-items:center}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;background:#171717;color:#fff;font-family:Heros}}
.s img.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:saturate(.8) contrast(1.06)}}
.grain{{position:absolute;inset:0;opacity:.08;mix-blend-mode:overlay;pointer-events:none;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/></filter><rect width='200' height='200' filter='url(%23n)'/></svg>")}}
.hd{{position:absolute;top:64px;left:72px;right:72px;display:flex;justify-content:space-between;font:400 21px 'Space Mono';letter-spacing:3px;color:rgba(255,255,255,.75);z-index:5}}
.hd.lt{{color:rgba(23,23,23,.55)}}
.arr{{position:absolute;bottom:60px;right:72px;font:400 21px 'Space Mono';letter-spacing:3px;color:rgba(255,255,255,.75);z-index:5}}.arr b{{color:#D6FF68;font-weight:400}}
.sc{{font-family:Scholar;color:#D6FF68;font-weight:400;letter-spacing:-.5px}}
.grid{{{GRID}}}
.s1 .gr{{position:absolute;inset:0;background:rgba(15,15,15,.28)}}
.s1 .h,.s1 .sc{{text-shadow:0 2px 30px rgba(0,0,0,.45),0 1px 3px rgba(0,0,0,.35)}}
.s1 .bl{{position:absolute;left:72px;top:170px;width:820px}}
.s1 .h{{font:700 104px/.93 Heros;letter-spacing:-5px;text-transform:uppercase}}
.s1 .sc{{font-size:70px;line-height:1;margin-top:22px;width:720px}}
.s2{{background:#F4F4F1;color:#171717}}
.s2 .tw{{position:absolute;left:100px;right:100px;top:440px}}
.s2 .who{{display:flex;align-items:center;gap:22px;margin-bottom:38px}}
.s2 .av{{width:112px;height:112px;border-radius:50%;object-fit:cover;object-position:center 20%}}
.s2 .nm{{font:700 40px Heros;display:flex;align-items:center;gap:10px}}.s2 .us{{font:400 32px Heros;color:#6B6B6B;margin-top:4px}}
.s2 .ok{{width:36px;height:36px}}
.s2 .tx{{font:400 64px/1.28 Heros;letter-spacing:-1.2px}}
.s3 .win{{position:absolute;left:96px;right:96px;top:360px;background:#1F1F1F;border:1px solid rgba(255,255,255,.09);border-radius:22px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.5)}}
.s3 .bar{{height:64px;display:flex;align-items:center;gap:12px;padding:0 26px;border-bottom:1px solid rgba(255,255,255,.07)}}
.s3 .bar i{{width:16px;height:16px;border-radius:50%;background:#3A3A3A}}.s3 .bar i:first-child{{background:#D6FF68}}
.s3 .bar span{{margin-left:16px;font:400 20px 'Space Mono';color:rgba(255,255,255,.45);letter-spacing:1px}}
.s3 .bd{{padding:64px 60px 70px;font:400 50px/1.42 'Space Mono';letter-spacing:-1px;color:#EDEDED}}
.s3 .bd .cur{{display:inline-block;width:26px;height:50px;background:#D6FF68;vertical-align:-8px;margin-left:6px}}
.s3 .cap{{position:absolute;left:96px;top:930px;font-size:56px}}
.s4 .fr{{position:absolute;left:72px;right:72px;top:200px;border:1px solid rgba(255,255,255,.18);padding:18px 18px 0;background:#1C1C1C}}
.s4 .fr img{{width:100%;height:520px;object-fit:cover;display:block;filter:saturate(.75) contrast(1.06)}}
.s4 .fr .meta{{display:flex;justify-content:space-between;padding:20px 4px 22px;font:400 19px 'Space Mono';letter-spacing:3px;color:rgba(255,255,255,.55)}}
.s4 .bl{{position:absolute;left:72px;top:930px;width:920px}}
.s4 .h{{font:700 96px/.93 Heros;letter-spacing:-5px;text-transform:uppercase}}
.s4 .sc{{font-size:76px;line-height:1.05;margin-top:14px}}
.l4{{background:#F4F4F1;color:#171717}}
.l4 .fr{{background:#fff;border:1px solid rgba(23,23,23,.15);box-shadow:0 24px 60px rgba(0,0,0,.10)}}
.l4 .fr .meta{{color:rgba(23,23,23,.55)}}
.l4 .sc{{color:#171717}}
.s5 .gr{{position:absolute;inset:0;background:linear-gradient(to top,rgba(23,23,23,.97) 0%,rgba(23,23,23,.88) 34%,rgba(23,23,23,.25) 58%,rgba(23,23,23,0) 75%)}}
.s5 .bl{{position:absolute;left:72px;bottom:120px;width:860px}}
.s5 .op{{font-size:60px;margin-bottom:16px}}
.s5 .h{{font:700 66px/1.02 Heros;letter-spacing:-3px}}
.s5 .h b{{color:#D6FF68}}
.s5 .ln{{width:64px;height:5px;background:#D6FF68;margin:34px 0 22px}}
.s5 .cr{{font:400 28px Heros;color:rgba(255,255,255,.75)}}
"""
CHECK='<svg class="ok" viewBox="0 0 24 24"><path fill="#1D9BF0" d="M22.5 12.5c0-1.58-.88-2.95-2.15-3.6.15-.44.23-.91.23-1.4 0-2.21-1.71-4-3.82-4-.47 0-.92.09-1.34.25C14.8 2.48 13.5 1.5 12 1.5s-2.8.98-3.42 2.25c-.42-.16-.87-.25-1.34-.25-2.11 0-3.82 1.79-3.82 4 0 .49.08.96.23 1.4-1.27.65-2.15 2.02-2.15 3.6 0 1.5.8 2.8 1.97 3.48-.03.17-.04.34-.04.52 0 2.21 1.71 4 3.82 4 .47 0 .92-.09 1.34-.25.62 1.27 1.920 2.25 3.42 2.25s2.8-.98 3.42-2.25c.42.16.87.25 1.34.25 2.11 0 3.82-1.79 3.82-4 0-.18-.01-.35-.04-.52 1.17-.68 1.97-1.98 1.97-3.48z"/><path fill="#fff" d="M10.6 16.2l-3.7-3.7 1.4-1.4 2.3 2.3 5.3-5.3 1.4 1.4z"/></svg>'
S=[
f'<div class="s s1"><img class="bg" src="file://{P}/s_face.jpg" style="object-position:center 30%;filter:saturate(.8) contrast(1.04)"><div class="gr"></div>{hd(1)}<div class="bl"><div class="h">Nós somos falhos, mas não somos falsos,</div><div class="sc">e isso já nos diferencia de muita gente.</div></div>{GRAIN}{ARR}</div>',
f'<div class="s s2">{hd(2,False)}<div class="tw"><div class="who"><img class="av" src="file://{P}/avatar.png"><div><div class="nm">Rafael Ferreira {CHECK}</div><div class="us">@_rafaelgalak</div></div></div><div class="tx">tô off, se precisar de ajuda faz que nem eu, se vira sozinho.</div></div>{GRAIN}<div class="arr" style="color:rgba(23,23,23,.55)">ARRASTE <b style="color:#171717">→</b></div></div>',
f'<div class="s s3 grid">{hd(3)}<div class="win"><div class="bar"><i></i><i></i><i></i><span>verdade.galak</span></div><div class="bd">fica fraco pra você ver se você vale alguma coisa, a vida é uma troca de interesse sinistra.<span class="cur"></span></div></div><div class="cap sc">anota essa.</div>{GRAIN}{ARR}</div>',
f'<div class="s s4 l4">{hd(4,False)}<div class="fr"><img src="file://{P}/f_varanda.jpg"><div class="meta"><span>RIO DE JANEIRO</span><span>06:40 · 26.11.26</span></div></div><div class="bl"><div class="h">Me conduz Deus, eu quero</div><div class="sc">a vida que conversamos.</div></div>{GRAIN}<div class="arr" style="color:rgba(23,23,23,.55)">ARRASTE <b style="color:#171717">→</b></div></div>',
f'<div class="s s5"><img class="bg" src="file://{P}/dorsal.jpg" style="object-position:center 50%;filter:saturate(.8) contrast(1.06)"><div class="gr"></div>{hd(5)}<div class="bl"><div class="op sc">pra salvar</div><div class="h">em algum momento vão tentar te convencer que você sonha alto demais, <b>é importante que você não ouça e siga em frente.</b></div><div class="ln"></div><div class="cr">gypsy warrior</div></div>{GRAIN}</div>',
]
open('frases.html','w').write(f"<html><head><meta charset=utf-8><style>{F}{css}</style></head><body>{''.join(S)}</body></html>")
