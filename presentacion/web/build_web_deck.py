#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera una MUESTRA del deck en HTML con el estilo de marca omnia (pro).
Self-contained: logo embebido en base64. Salida: web/omnia-deck.html
Si se aprueba el estilo, se amplía a las 17 slides + export PDF/PPTX."""
import os, base64
HERE = os.path.dirname(__file__)
LOGO = os.path.join(HERE, "..", "assets", "omnia-logo.png")
OUT  = os.path.join(HERE, "omnia-deck.html")
os.makedirs(HERE, exist_ok=True)
b64 = base64.b64encode(open(LOGO,"rb").read()).decode() if os.path.exists(LOGO) else ""

HTML = r"""<!doctype html><html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>omnia · Sistema Ads + CRM para Clínicas</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--grad:linear-gradient(135deg,#4f46e5 0%,#7c3aed 50%,#db2777 100%);--ink:#0f172a;--muted:#52525b;--line:#ece9f7}
html{scroll-snap-type:y mandatory;scroll-behavior:smooth}
body{font-family:'Plus Jakarta Sans',system-ui,sans-serif;color:var(--ink);background:#f6f5fb;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:'Outfit','Plus Jakarta Sans',sans-serif;letter-spacing:-.02em;line-height:1.05}
.slide{position:relative;width:100%;min-height:100vh;padding:7vh 7vw;display:flex;flex-direction:column;justify-content:center;scroll-snap-align:start;overflow:hidden;border-bottom:1px solid var(--line)}
.kick{font-family:'Outfit';font-weight:800;letter-spacing:.14em;text-transform:uppercase;font-size:.78rem;color:#7c3aed;margin-bottom:.7rem}
.h{font-size:clamp(2rem,4.2vw,3.1rem);font-weight:800}
.sub{color:var(--muted);font-size:clamp(1rem,1.4vw,1.2rem);margin-top:.7rem;max-width:62ch}
.gradtext{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.light:before{content:'';position:absolute;width:560px;height:560px;border-radius:50%;background:radial-gradient(circle,rgba(124,58,237,.12),transparent 70%);top:-200px;right:-140px;pointer-events:none}
.light:after{content:'';position:absolute;width:480px;height:480px;border-radius:50%;background:radial-gradient(circle,rgba(37,99,235,.10),transparent 70%);bottom:-220px;left:-160px;pointer-events:none}
.foot{position:absolute;left:7vw;right:7vw;bottom:3.2vh;display:flex;justify-content:space-between;color:#9aa0ad;font-size:.78rem;border-top:1px solid var(--line);padding-top:10px}
/* cover */
.cover{background:var(--grad);color:#fff;justify-content:center}
.cover:before{content:'';position:absolute;inset:0;background:radial-gradient(1200px 500px at 80% -10%,rgba(255,255,255,.25),transparent 60%)}
.chip{position:relative;background:#fff;border-radius:18px;padding:15px 24px;box-shadow:0 24px 60px rgba(79,70,229,.4);width:max-content}
.chip img{height:48px;display:block}
.cover .h{color:#fff;font-size:clamp(2.4rem,5.2vw,4rem);margin-top:2rem;max-width:18ch}
.cover .sub{color:rgba(255,255,255,.92);max-width:54ch}
.cover .tagrow{margin-top:1.6rem;display:flex;gap:10px;flex-wrap:wrap}
.tag{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.3);color:#fff;font-weight:600;font-size:.9rem;padding:8px 16px;border-radius:999px;backdrop-filter:blur(6px)}
/* flow */
.flow{display:flex;gap:14px;flex-wrap:wrap;margin-top:2.6rem;align-items:stretch}
.step{flex:1;min-width:150px;background:#fff;border:1px solid var(--line);border-radius:20px;padding:22px;box-shadow:0 12px 34px rgba(79,70,229,.07);position:relative}
.step .n{width:42px;height:42px;border-radius:12px;background:var(--grad);color:#fff;font-family:'Outfit';font-weight:800;font-size:1.1rem;display:flex;align-items:center;justify-content:center;margin-bottom:14px;box-shadow:0 8px 18px rgba(124,58,237,.35)}
.step h3{font-size:1.06rem}.step p{color:var(--muted);font-size:.9rem;margin-top:5px;line-height:1.4}
.arrow{align-self:center;color:#c4b5fd;font-size:1.6rem;font-weight:800}
.note{margin-top:2.2rem;font-size:1.05rem;font-weight:600}.note b{color:#7c3aed}
/* pricing */
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:2.4rem}
.card{background:#fff;border:1px solid var(--line);border-radius:22px;padding:26px 22px;box-shadow:0 14px 40px rgba(79,70,229,.08);position:relative}
.card.feat{border:2px solid transparent;background:linear-gradient(#fff,#fff) padding-box,var(--grad) border-box;box-shadow:0 28px 64px rgba(124,58,237,.22);transform:translateY(-8px)}
.badge{position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:var(--grad);color:#fff;font-family:'Outfit';font-size:.7rem;font-weight:800;letter-spacing:.04em;padding:6px 14px;border-radius:999px;white-space:nowrap}
.card .name{font-family:'Outfit';font-weight:800;font-size:1.05rem}
.card .price{font-family:'Outfit';font-size:2rem;font-weight:900;margin:.5rem 0 .1rem}.price small{font-size:.85rem;color:var(--muted);font-weight:600}
.card .brk{font-size:.82rem;color:#7c3aed;font-weight:700;margin-bottom:.7rem}
.card ul{list-style:none;display:flex;flex-direction:column;gap:9px}
.card li{font-size:.84rem;color:var(--muted);padding-left:22px;position:relative;line-height:1.35}
.card li:before{content:'✓';position:absolute;left:0;top:0;color:#7c3aed;font-weight:900}
.pricenote{margin-top:1.8rem;background:#fff7ed;border:1px solid #fed7aa;color:#9a3412;border-radius:14px;padding:14px 18px;font-size:.9rem;font-weight:600}
@media (max-width:900px){.cards{grid-template-columns:repeat(2,1fr)}.card.feat{transform:none}}
@media print{html,body{background:#fff}.slide{min-height:auto;height:100vh;page-break-after:always}.cover:before,.light:before,.light:after{display:none}}
</style></head><body>

<!-- 1 PORTADA -->
<section class="slide cover">
  <div class="chip"><img src="data:image/png;base64,__LOGO__" alt="omnia"></div>
  <h1 class="h">Sistema <span style="opacity:.9">Ads + CRM</span><br>para Clínicas</h1>
  <p class="sub">Convertimos anuncios en pacientes — y pacientes en reseñas de 5★. Captación, atención 24/7 y reputación, en un solo sistema con una sola factura.</p>
  <div class="tagrow"><span class="tag">Odontología</span><span class="tag">Estética</span><span class="tag">Medicina estética</span></div>
</section>

<!-- 2 CÓMO FUNCIONA -->
<section class="slide light">
  <div class="kick">Cómo funciona</div>
  <h2 class="h">El recorrido del paciente, <span class="gradtext">en piloto automático</span></h2>
  <p class="sub">De un clic en el anuncio a una reseña de 5★ — sin que nadie mueva un dedo.</p>
  <div class="flow">
    <div class="step"><div class="n">1</div><h3>Anuncio</h3><p>Google / Meta atraen al lead.</p></div>
    <div class="arrow">›</div>
    <div class="step"><div class="n">2</div><h3>Sofía (IA)</h3><p>Atiende WhatsApp/IG/FB al instante y califica.</p></div>
    <div class="arrow">›</div>
    <div class="step"><div class="n">3</div><h3>Agenda</h3><p>Reserva la cita sola en el calendario.</p></div>
    <div class="arrow">›</div>
    <div class="step"><div class="n">4</div><h3>Recordatorios</h3><p>Avisa 24h antes y reduce ausencias.</p></div>
    <div class="arrow">›</div>
    <div class="step"><div class="n">5</div><h3>Reseña 5★</h3><p>Pide valoración y filtra hacia Google.</p></div>
  </div>
  <p class="note">El lead deja sus datos → la IA lo atiende → <b>agenda solo</b> → asiste → <b>deja reseña</b> → vuelve.</p>
  <div class="foot"><span>omnia · Sistema Ads + CRM</span><span>04 / 17</span></div>
</section>

<!-- 3 PLANES -->
<section class="slide light">
  <div class="kick">Planes</div>
  <h2 class="h">El anuncio trae, <span class="gradtext">el sistema convierte</span></h2>
  <p class="sub">Cada plan = gestión de ads (Google/Meta) + el sistema omnia completo.</p>
  <div class="cards">
    <div class="card"><div class="name">Captación · Z</div><div class="price">447€<small>/mes</small></div><div class="brk">197€ sistema + 250€ ads</div>
      <ul><li>Ads 1 canal (Google o Meta)</li><li>Sistema omnia completo</li><li>Activación única 290€</li></ul></div>
    <div class="card feat"><div class="badge">MÁS ELEGIDO</div><div class="name">Crecimiento · S</div><div class="price">647€<small>/mes</small></div><div class="brk">197€ sistema + 450€ ads</div>
      <ul><li>Ads 2 canales + analítica</li><li>Sistema omnia completo</li><li>Activación única 290€</li></ul></div>
    <div class="card"><div class="name">Pro · P</div><div class="price">822€<small>/mes</small></div><div class="brk">197€ sistema + 625€ ads</div>
      <ul><li>Gestión avanzada</li><li>Redistribución de presupuesto</li><li>Activación única 290€</li></ul></div>
    <div class="card"><div class="name">Escala · T</div><div class="price">A medida</div><div class="brk">197€ sistema + ads a medida</div>
      <ul><li>Multi-sede / multi-campaña</li><li>Reporting a medida</li><li>Activación única 290€</li></ul></div>
  </div>
  <div class="pricenote">Primer mes: 290€ activación + mensualidad. Después, solo la mensualidad. Aparte: inversión publicitaria (desde 300€) + consumos. Precios + IVA · propuesta.</div>
  <div class="foot"><span>omnia · Sistema Ads + CRM</span><span>13 / 17</span></div>
</section>

</body></html>"""
open(OUT,"w").write(HTML.replace("__LOGO__", b64))
print("OK ->", OUT, "·", os.path.getsize(OUT), "bytes")
