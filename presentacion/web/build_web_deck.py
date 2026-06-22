#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deck completo (17 slides) en HTML, estilo de marca omnia. USO INTERNO.
Self-contained (logos en base64). Salida: web/omnia-deck.html
Imprimir → PDF respeta @media print (1 slide por página)."""
import os, base64
HERE = os.path.dirname(__file__)
A = os.path.join(HERE, "..", "assets")
OUT = os.path.join(HERE, "omnia-deck.html")
def b64(p):
    p=os.path.join(A,p); return base64.b64encode(open(p,"rb").read()).decode() if os.path.exists(p) else ""
LOGO, LOGOW = b64("omnia-logo.png"), b64("omnia-logo-white.png")

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{--grad:linear-gradient(135deg,#4f46e5 0%,#7c3aed 50%,#db2777 100%);--ink:#0f172a;--muted:#52525b;--line:#ece9f7}
html{scroll-snap-type:y mandatory;scroll-behavior:smooth}
body{font-family:'Plus Jakarta Sans',system-ui,sans-serif;color:var(--ink);background:#f6f5fb;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:'Outfit','Plus Jakarta Sans',sans-serif;letter-spacing:-.02em;line-height:1.06}
.slide{position:relative;width:100%;min-height:100vh;padding:7vh 7vw 9vh;display:flex;flex-direction:column;justify-content:center;scroll-snap-align:start;overflow:hidden;border-bottom:1px solid var(--line)}
.kick{font-family:'Outfit';font-weight:800;letter-spacing:.14em;text-transform:uppercase;font-size:.78rem;color:#7c3aed;margin-bottom:.7rem}
.h{font-size:clamp(1.9rem,4vw,3rem);font-weight:800}
.sub{color:var(--muted);font-size:clamp(1rem,1.35vw,1.18rem);margin-top:.7rem;max-width:64ch}
.gradtext{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.light:before{content:'';position:absolute;width:560px;height:560px;border-radius:50%;background:radial-gradient(circle,rgba(124,58,237,.12),transparent 70%);top:-200px;right:-140px;pointer-events:none}
.light:after{content:'';position:absolute;width:480px;height:480px;border-radius:50%;background:radial-gradient(circle,rgba(37,99,235,.10),transparent 70%);bottom:-220px;left:-160px;pointer-events:none}
.foot{position:absolute;left:7vw;right:7vw;bottom:3vh;display:flex;justify-content:space-between;color:#9aa0ad;font-size:.76rem;border-top:1px solid var(--line);padding-top:9px}
.conf{position:absolute;top:18px;right:22px;background:rgba(124,58,237,.1);color:#7c3aed;font-family:'Outfit';font-weight:800;font-size:.64rem;letter-spacing:.1em;padding:6px 12px;border-radius:999px;border:1px solid rgba(124,58,237,.25);z-index:3}
/* cover/cierre */
.cover{background:var(--grad);color:#fff;justify-content:center}
.cover:before{content:'';position:absolute;inset:0;background:radial-gradient(1200px 520px at 80% -10%,rgba(255,255,255,.22),transparent 60%)}
.cover .conf{background:rgba(255,255,255,.18);color:#fff;border-color:rgba(255,255,255,.4)}
.logo{position:relative;height:54px;margin-bottom:2rem}
.cover .h{color:#fff;font-size:clamp(2.4rem,5.2vw,4rem);max-width:18ch}
.cover .sub{color:rgba(255,255,255,.92);max-width:56ch}
.tagrow{margin-top:1.6rem;display:flex;gap:10px;flex-wrap:wrap}
.tag{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.3);color:#fff;font-weight:600;font-size:.9rem;padding:8px 16px;border-radius:999px;backdrop-filter:blur(6px)}
.cover .foot{color:rgba(255,255,255,.85);border-top-color:rgba(255,255,255,.25)}
/* grids/cards */
.grid{display:grid;gap:18px;margin-top:2.1rem}.g2{grid-template-columns:1fr 1fr}.g3{grid-template-columns:repeat(3,1fr)}
.card{background:#fff;border:1px solid var(--line);border-radius:20px;padding:24px;box-shadow:0 12px 34px rgba(79,70,229,.07);position:relative;overflow:hidden}
.card .bar{position:absolute;top:0;left:0;right:0;height:5px}.bar.a{background:#7c3aed}.bar.b{background:#4f46e5}.bar.c{background:#db2777}
.card h3{font-size:1.06rem;margin:6px 0 10px}
.card ul{list-style:none;display:flex;flex-direction:column;gap:7px}.card li{color:var(--muted);font-size:.88rem;padding-left:18px;position:relative;line-height:1.4}
.card li:before{content:'•';position:absolute;left:2px;color:#7c3aed;font-weight:800}
/* flow */
.flow{display:flex;gap:12px;flex-wrap:wrap;margin-top:2.4rem;align-items:stretch}
.step{flex:1;min-width:135px;background:#fff;border:1px solid var(--line);border-radius:18px;padding:18px;box-shadow:0 12px 30px rgba(79,70,229,.07)}
.step .n{width:40px;height:40px;border-radius:12px;background:var(--grad);color:#fff;font-family:'Outfit';font-weight:800;display:flex;align-items:center;justify-content:center;margin-bottom:12px;box-shadow:0 8px 18px rgba(124,58,237,.35)}
.step h3{font-size:1rem}.step p{color:var(--muted);font-size:.85rem;margin-top:4px;line-height:1.35}
.arrow{align-self:center;color:#c4b5fd;font-size:1.5rem;font-weight:800}
.note{margin-top:2rem;font-size:1.04rem;font-weight:600}.note b{color:#7c3aed}
/* pipeline */
.pipe{display:flex;gap:7px;flex-wrap:wrap;margin-top:2.4rem;align-items:center}
.stage{background:#fff;border:1px solid var(--line);border-radius:13px;padding:14px 12px;font-weight:700;font-family:'Outfit';font-size:.86rem;box-shadow:0 8px 20px rgba(79,70,229,.06);flex:1;min-width:115px;text-align:center}
.stage.win{background:var(--grad);color:#fff;border:0}.stage.lost{background:#fef2f2;color:#b91c1c;border-color:#fecaca}
.psep{color:#c4b5fd;font-weight:800}
/* compare 2-col */
.compare{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:2rem}
.col{background:#fff;border:1px solid var(--line);border-radius:20px;padding:0 26px 26px;box-shadow:0 12px 34px rgba(79,70,229,.07);overflow:hidden}
.col .top{height:6px;margin:0 -26px 20px}.top.g1{background:var(--grad)}.top.gray{background:#94a3b8}.top.blue{background:#4f46e5}
.col h3{font-size:1.15rem;margin-bottom:14px}
.col ul{list-style:none;display:flex;flex-direction:column;gap:10px}.col li{color:var(--muted);font-size:.95rem;padding-left:24px;position:relative;line-height:1.4}
.col.bad li:before{content:'—';position:absolute;left:0;color:#94a3b8}.col.good li:before{content:'✓';position:absolute;left:0;color:#7c3aed;font-weight:800}
/* tables */
.ptable{width:100%;border-collapse:separate;border-spacing:0;margin-top:2rem;font-size:.92rem;box-shadow:0 14px 40px rgba(79,70,229,.08);border-radius:16px;overflow:hidden}
.ptable th{background:#171430;color:#fff;font-family:'Outfit';font-weight:700;text-align:left;padding:13px 18px;font-size:.82rem}
.ptable th.r,.ptable td.r{text-align:right}
.ptable td{padding:12px 18px;border-top:1px solid var(--line);background:#fff}
.ptable tr:nth-child(even) td{background:#faf9fe}
.ptable .svc b{font-family:'Outfit'}.ptable .svc span{display:block;color:var(--muted);font-size:.78rem;margin-top:2px}
.ptable .big{font-family:'Outfit';font-weight:800;color:#171430}
.infobox{margin-top:1.4rem;background:#f3f1fb;border:1px solid #e6e1f7;border-radius:14px;padding:14px 18px;font-size:.86rem;color:var(--muted)}.infobox b{color:#7c3aed}
.warnbox{margin-top:1.4rem;background:#fff7ed;border:1px solid #fed7aa;color:#9a3412;border-radius:14px;padding:14px 18px;font-size:.88rem;font-weight:600}
/* pricing */
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:15px;margin-top:2.2rem}
.pcard{background:#fff;border:1px solid var(--line);border-radius:22px;padding:26px 20px;box-shadow:0 14px 40px rgba(79,70,229,.08);position:relative}
.pcard.feat{border:2px solid transparent;background:linear-gradient(#fff,#fff) padding-box,var(--grad) border-box;box-shadow:0 28px 64px rgba(124,58,237,.22);transform:translateY(-8px)}
.pbadge{position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:var(--grad);color:#fff;font-family:'Outfit';font-size:.68rem;font-weight:800;letter-spacing:.04em;padding:6px 14px;border-radius:999px;white-space:nowrap}
.pname{font-family:'Outfit';font-weight:800;font-size:1.02rem}
.price{font-family:'Outfit';font-size:1.9rem;font-weight:900;margin:.45rem 0 .1rem}.price small{font-size:.82rem;color:var(--muted);font-weight:600}
.brk{font-size:.8rem;color:#7c3aed;font-weight:700;margin-bottom:.7rem}
.pcard ul{list-style:none;display:flex;flex-direction:column;gap:8px}.pcard li{font-size:.82rem;color:var(--muted);padding-left:20px;position:relative;line-height:1.35}.pcard li:before{content:'✓';position:absolute;left:0;color:#7c3aed;font-weight:900}
/* pay */
.pay{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:2.1rem}
.paycard{background:#fff;border:1px solid var(--line);border-radius:20px;padding:0 28px 26px;box-shadow:0 12px 34px rgba(79,70,229,.07);overflow:hidden}
.paycard .top{height:6px;margin:0 -28px 22px}
.paycard .lbl{font-family:'Outfit';font-weight:800;letter-spacing:.06em;font-size:.78rem;color:#7c3aed;text-transform:uppercase}
.paycard .ln{font-size:1.1rem;font-weight:600;margin-top:10px}.paycard .tot{font-family:'Outfit';font-size:2.1rem;font-weight:900;margin-top:8px}
@media (max-width:900px){.cards{grid-template-columns:repeat(2,1fr)}.pcard.feat{transform:none}.g3{grid-template-columns:1fr}.compare,.pay{grid-template-columns:1fr}}
@media print{html,body{background:#fff}.slide{min-height:auto;height:100vh;page-break-after:always}.cover:before,.light:before,.light:after{display:none}}
"""

def foot(n, dark=False):
    return f'<div class="foot"><span>omnia · USO INTERNO — CONFIDENCIAL</span><span>{n} / 17</span></div>'
def conf():
    return '<div class="conf">USO INTERNO</div>'
def cards(items, cols, bar="a"):
    h=""
    for (t,bl) in items:
        lis="".join(f"<li>{x}</li>" for x in bl)
        h+=f'<div class="card"><div class="bar {bar}"></div><h3>{t}</h3><ul>{lis}</ul></div>'
    return f'<div class="grid g{cols}">{h}</div>'

S=[]
# 1 cover
S.append(f'''<section class="slide cover">{conf()}
<img class="logo" src="data:image/png;base64,{LOGOW}" alt="omnia">
<h1 class="h">Sistema <span style="opacity:.92">Ads + CRM</span><br>para Clínicas</h1>
<p class="sub">Convertimos anuncios en pacientes — y pacientes en reseñas de 5★. Captación, atención 24/7 y reputación, en un solo sistema con una sola factura.</p>
<div class="tagrow"><span class="tag">Odontología</span><span class="tag">Estética</span><span class="tag">Medicina estética</span></div>
<div class="foot"><span>DOCUMENTO INTERNO · NO COMPARTIR CON CLIENTES</span><span>omnia in business</span></div></section>''')
# 2 problema
S.append(f'''<section class="slide light">{conf()}<div class="kick">El problema</div>
<h2 class="h">El paciente escribe… <span class="gradtext">y se pierde</span></h2>
<p class="sub">Lo que hoy le pasa a casi toda clínica que invierte en publicidad.</p>
{cards([("Nadie contesta a tiempo",["El lead escribe a las 22:00","Le responden al otro día","Ya agendó en otra clínica"]),("Todo disperso",["WhatsApp, Instagram, Facebook","Mensajes que se traspapelan","No se sabe de qué anuncio vino"]),("Agenda con huecos",["Citas sin recordatorio","Ausencias y cancelaciones","Sin seguimiento al que no agendó"]),("Reputación al azar",["Pocas reseñas en Google","Las malas sí se publican","Sin pedirlas de forma sistemática"])],2,"b")}
{foot(2)}</section>''')
# 3 solución
S.append(f'''<section class="slide light">{conf()}<div class="kick">La solución</div>
<h2 class="h">No es una herramienta. <span class="gradtext">Es un SISTEMA.</span></h2>
<p class="sub">Anuncios que traen pacientes + un CRM que los atiende y fideliza — todo conectado.</p>
{cards([("1 · Captar",["Ads en Google/Meta","Atiende WhatsApp/IG/FB 24/7"]),("2 · Convertir",["La IA reserva la cita","Mueve el pipeline solo"]),("3 · Fidelizar",["Recordatorios automáticos","Reseñas de Google 5★"])],3,"a")}
<p class="note">Una sola cuenta, las piezas se hablan entre sí, <b>una sola factura</b>: omnia.</p>{foot(3)}</section>''')
# 4 cómo funciona
S.append(f'''<section class="slide light">{conf()}<div class="kick">Cómo funciona</div>
<h2 class="h">El recorrido del paciente, <span class="gradtext">en piloto automático</span></h2>
<p class="sub">De un clic en el anuncio a una reseña de 5★ — sin que nadie mueva un dedo.</p>
<div class="flow">
<div class="step"><div class="n">1</div><h3>Anuncio</h3><p>Google / Meta atraen al lead.</p></div><div class="arrow">›</div>
<div class="step"><div class="n">2</div><h3>Mensaje</h3><p>Entra por WhatsApp / IG / FB.</p></div><div class="arrow">›</div>
<div class="step"><div class="n">3</div><h3>Sofía (IA)</h3><p>Atiende al instante y califica.</p></div><div class="arrow">›</div>
<div class="step"><div class="n">4</div><h3>Agenda</h3><p>Reserva la cita sola.</p></div><div class="arrow">›</div>
<div class="step"><div class="n">5</div><h3>Recordatorios</h3><p>Avisa 24h antes.</p></div><div class="arrow">›</div>
<div class="step"><div class="n">6</div><h3>Reseña 5★</h3><p>Filtra hacia Google.</p></div></div>
<p class="note">El lead deja sus datos → la IA lo atiende → <b>agenda solo</b> → asiste → <b>deja reseña</b> → vuelve.</p>{foot(4)}</section>''')
# 5 Sofía
S.append(f'''<section class="slide light">{conf()}<div class="kick">El asistente IA</div>
<h2 class="h">Sofía: <span class="gradtext">la recepcionista que no duerme</span></h2>
<p class="sub">Atiende cada mensaje al instante, en el tono de la clínica, y reserva citas sola.</p>
{cards([("Atiende 24/7",["Responde en segundos","Sin sueldo ni descansos","Mismo tono de la marca"]),("Reserva citas",["Ofrece día y hora libres","Agenda en el calendario","Pide datos con RGPD"]),("Sabe cuándo parar",["Deriva a humano si hace falta","Comprobantes, dudas médicas","Nunca inventa precios"])],3,"a")}{foot(5)}</section>''')
# 6 captación
S.append(f'''<section class="slide light">{conf()}<div class="kick">Captación</div>
<h2 class="h">Todos los canales en una bandeja — <span class="gradtext">y sabes de dónde vino cada lead</span></h2>
{cards([("Multicanal",["WhatsApp, Instagram, Facebook","Una conversación por paciente","Nada se traspapela"]),("Atribución de ads",["Guarda UTM y el anuncio (Ad)","Sabes qué campaña trae pacientes"]),("Canal detectado",["Etiqueta canal-wa/ig/fb","Pide el teléfono solo si hace falta","Listo para remarketing"])],3,"b")}{foot(6)}</section>''')
# 7 pipeline
PIPE=["Nuevo Lead","En conversación humana","Pre-reserva / Cita Reservada","Cita Confirmada","No Asistió","Servicio Realizado (Ganado)","Perdido"]
pipe_html=""
for i,st in enumerate(PIPE):
    cl="win" if "Ganado" in st else ("lost" if st=="Perdido" else "")
    pipe_html+=f'<div class="stage {cl}">{st}</div>'+("" if i==len(PIPE)-1 else '<span class="psep">›</span>')
S.append(f'''<section class="slide light">{conf()}<div class="kick">Pipeline de ventas</div>
<h2 class="h">Ves en qué punto está <span class="gradtext">cada paciente</span></h2>
<p class="sub">Cada oportunidad avanza por etapas claras — como una operación con fases.</p>
<div class="pipe">{pipe_html}</div>
<p class="note">Los robots mueven al paciente de etapa <b>automáticamente</b>. Ves el panel y sabes qué falta para cada cierre.</p>{foot(7)}</section>''')
# 8 automatizaciones
S.append(f'''<section class="slide light">{conf()}<div class="kick">Automatizaciones</div>
<h2 class="h">9 robots que <span class="gradtext">trabajan solos</span></h2>
<p class="sub">Configurados y listos. Cada uno hace una tarea sin que nadie la recuerde.</p>
{cards([("Bienvenida + IA",["Activa a Sofía","Crea la oportunidad"]),("Cita reservada",["Confirma por WhatsApp","Mueve el pipeline"]),("Recordatorio 24h",["Reduce ausencias","Mensaje automático"]),("Remarketing",["Actúa en la etapa Perdido","Recupera al que no agendó"]),("Handoff a humano",["Deriva a una persona","Pausa el bot y avisa"]),("Reputación Google",["Pide reseña tras el servicio","Filtra 4-5★ → Google"])],3,"a")}{foot(8)}</section>''')
# 9 reputación
S.append(f'''<section class="slide light">{conf()}<div class="kick">Reputación Google</div>
<h2 class="h">Más reseñas de 5★ — <span class="gradtext">y las malas, en privado</span></h2>
<div class="compare">
<div class="col good"><div class="top g1"></div><h3>⭐ 4–5 estrellas</h3><ul><li>Van directo a dejar la reseña en Google</li><li>Más reputación pública</li><li>Más pacientes nuevos</li></ul></div>
<div class="col good"><div class="top blue"></div><h3>⭐ 1–3 estrellas</h3><ul><li>Van a un formulario privado (NO a Google)</li><li>Recuperas al paciente</li><li>Proteges la marca</li></ul></div></div>
<p class="note">También <b>reactiva tu base de datos</b> antigua para traer pacientes que ya tenías.</p>{foot(9)}</section>''')
# 10 por nicho
S.append(f'''<section class="slide light">{conf()}<div class="kick">Adaptable por nicho</div>
<h2 class="h">El mismo sistema, <span class="gradtext">ajustado a cada clínica</span></h2>
<p class="sub">Cambia el catálogo, el tono y si se pide señal. La estrategia es la misma.</p>
{cards([("Odontología",["Limpieza, ortodoncia, blanqueamiento","Tono cercano y claro","Señal: normalmente no"]),("Estética / Belleza",["Faciales, micropigmentación, spa de uñas y cejas","Tono cálido","Señal: habitual (sí)"]),("Medicina estética",["Ácido, bótox, tratamientos","Tono profesional","Dudas clínicas → a humano"])],3,"c")}{foot(10)}</section>''')
# 11 templatizado
S.append(f'''<section class="slide light">{conf()}<div class="kick">Instalación</div>
<h2 class="h">Templatizado: <span class="gradtext">solo cambian 3–4 cosas</span></h2>
<p class="sub">El sistema completo ya está montado. Personalizar un cliente toma horas, no semanas.</p>
{cards([("Se personaliza",["Logo y colores","Datos del negocio","Servicios y precios","¿Pide señal? sí/no"]),("Ya viene hecho",["Bot, pipeline y etapas","Los 9 workflows","Reputación Google","Plantillas de mensajes"]),("Cómo se llena",["Custom Values (1 vez)","Todo lo lee el sistema","Mismo snapshot para todos","Onboarding por formulario"])],3,"b")}{foot(11)}</section>''')
# 12 antes/después
S.append(f'''<section class="slide light">{conf()}<div class="kick">El cambio</div>
<h2 class="h">Antes <span class="gradtext">vs. Después</span></h2>
<div class="compare">
<div class="col bad"><div class="top gray"></div><h3>Antes</h3><ul><li>Leads que escriben y nadie contesta</li><li>Agenda con huecos y ausencias</li><li>Mensajes perdidos entre apps</li><li>Pocas reseñas, y las malas públicas</li><li>Sin saber qué anuncio funciona</li></ul></div>
<div class="col good"><div class="top g1"></div><h3>Después</h3><ul><li>Cada lead atendido en segundos, 24/7</li><li>Agenda llena, con recordatorios</li><li>Todo en una bandeja, nada se pierde</li><li>Flujo constante de reseñas 5★</li><li>Retorno medible por campaña</li></ul></div></div>{foot(12)}</section>''')
# 13 planes
S.append(f'''<section class="slide light">{conf()}<div class="kick">Planes</div>
<h2 class="h">El anuncio trae, <span class="gradtext">el sistema convierte</span></h2>
<p class="sub">Cada plan = gestión de ads (Google/Meta) + el sistema omnia completo.</p>
<div class="cards">
<div class="pcard"><div class="pname">Captación · Z</div><div class="price">447€<small>/mes</small></div><div class="brk">197€ sistema + 250€ ads</div><ul><li>Ads 1 canal (Google o Meta)</li><li>Sistema omnia completo</li><li>Activación única 290€</li></ul></div>
<div class="pcard feat"><div class="pbadge">MÁS ELEGIDO</div><div class="pname">Crecimiento · S</div><div class="price">647€<small>/mes</small></div><div class="brk">197€ sistema + 450€ ads</div><ul><li>Ads 2 canales + analítica</li><li>Sistema omnia completo</li><li>Activación única 290€</li></ul></div>
<div class="pcard"><div class="pname">Pro · P</div><div class="price">822€<small>/mes</small></div><div class="brk">197€ sistema + 625€ ads</div><ul><li>Gestión avanzada</li><li>Redistribución de presupuesto</li><li>Activación única 290€</li></ul></div>
<div class="pcard"><div class="pname">Escala · T</div><div class="price">A medida</div><div class="brk">197€ sistema + ads a medida</div><ul><li>Multi-sede / multi-campaña</li><li>Reporting a medida</li><li>Activación única 290€</li></ul></div></div>
<div class="warnbox">Aparte: inversión publicitaria (desde 300€/camp.) + consumos (WhatsApp, IA, correos). Precios + IVA · propuesta interna.</div>{foot(13)}</section>''')
# 14 cómo se paga
S.append(f'''<section class="slide light">{conf()}<div class="kick">Cómo se paga</div>
<h2 class="h">Fácil: un pago al empezar, <span class="gradtext">luego una cuota fija</span></h2>
<p class="sub">Ejemplo con el plan Captación. Funciona igual en todos los planes.</p>
<div class="pay">
<div class="paycard"><div class="top g1"></div><div class="lbl">El primer mes</div><div class="ln">290€ activación <b>(una sola vez)</b></div><div class="ln">+ 447€ primera mensualidad</div><div class="tot gradtext">= 737€</div></div>
<div class="paycard"><div class="top blue"></div><div class="lbl">Del mes 2 en adelante</div><div class="tot">447€<small style="font-size:1rem;color:var(--muted)">/mes</small></div><div class="ln" style="font-size:.95rem;color:var(--muted)">= 197€ sistema + 250€ ads</div><div class="ln" style="font-size:.9rem;color:var(--muted)">La activación NO se vuelve a pagar.</div></div></div>
<div class="warnbox">Aparte (a Google/Meta y proveedores, NO a omnia): inversión en anuncios (desde 300€) + consumos del sistema.</div>{foot(14)}</section>''')
# 15 economía (interno)
ECO=[("Captación · Z","250 €/mes","197 €/mes","447 €/mes"),("Crecimiento · S","450 €/mes","197 €/mes","647 €/mes"),("Pro · P","625 €/mes","197 €/mes","822 €/mes"),("Escala · T","a medida","197 €/mes","a medida")]
eco_rows="".join(f'<tr><td class="big">{n}</td><td>{a}</td><td>{s}</td><td class="r big">{t}</td></tr>' for (n,a,s,t) in ECO)
S.append(f'''<section class="slide light">{conf()}<div class="kick">Economía del modelo · interno</div>
<h2 class="h">Por nivel <span class="gradtext">(para dirección)</span></h2>
<table class="ptable"><tr><th>Nivel</th><th>Ads (precio cliente = ómibu)</th><th>Sistema omnia /mes</th><th class="r">Total cliente /mes</th></tr>{eco_rows}</table>
<div class="infobox">Activación única <b>290 €</b> · Ingreso recurrente omnia = sistema <b>197 €/mes</b> (producto propio). Ads: precio cliente = tarifa <b>ómibu</b>; omnia recibe descuento interno de ómibu (margen <b>EN DISCUSIÓN</b>). Ancla de valor: a medida = <b>5.683 $</b> (cotizador). Propuesta.</div>{foot(15)}</section>''')
# 16 costes operativos
COST=[("Licencia de Meta (WhatsApp Business)","Cuota mensual fija del proveedor","Mensual","€30/mes"),("Conversaciones WhatsApp","Plantillas · por conversación iniciada","Por conversación","€18 – €55"),("Tokens de IA (modelo conversacional)","Agente que cualifica, responde y agenda","Por volumen · o ilimitado *","€28–€74 · €127/mes *"),("Envío de correos","Recordatorios y seguimientos (opcional)","Por envío","€0 – €18")]
cost_rows="".join(f'<tr><td class="svc"><b>{n}</b><span>{d}</span></td><td>{m}</td><td class="r big">{e}</td></tr>' for (n,d,m,e) in COST)
S.append(f'''<section class="slide light">{conf()}<div class="kick">Consumos de terceros</div>
<h2 class="h">Costes operativos <span class="gradtext">estimados</span></h2>
<p class="sub">Servicios externos que se pagan según uso, aparte de la cuota de omnia. El cliente mantiene el control y la titularidad de cada cuenta.</p>
<table class="ptable"><tr><th>Servicio</th><th>Modelo de cobro</th><th class="r">Estimado mensual *</th></tr>{cost_rows}</table>
<div class="infobox">Estos consumos <b>no los factura omnia</b>: son pagos directos a los proveedores según el volumen real. <b>*</b> Tokens de IA: por volumen (€28–€74) o plan <b>ILIMITADO 127 €/mes</b> — recomendado para clínicas con alto tráfico de leads. Cifras en € (IVA no incluido).</div>{foot(16)}</section>''')
# 17 cierre
S.append(f'''<section class="slide cover">{conf()}
<img class="logo" src="data:image/png;base64,{LOGOW}" alt="omnia">
<div class="kick" style="color:rgba(255,255,255,.85)">En resumen</div>
<h2 class="h" style="color:#fff">Un sistema que capta, atiende<br>y fideliza — con una sola factura.</h2>
<div class="tagrow" style="flex-direction:column;align-items:flex-start;gap:8px;margin-top:1.4rem">
<span class="tag">✓ Ads (Google/Meta) + CRM en un solo sistema</span>
<span class="tag">✓ En español de España · odontología, estética y medicina</span>
<span class="tag">✓ Templatizado y masivo: nuevo cliente en horas</span></div>
<div class="foot"><span>DOCUMENTO INTERNO · CONFIDENCIAL</span><span>omnia · omniainbusiness.com</span></div></section>''')

html=f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>omnia · Sistema Ads + CRM para Clínicas (INTERNO)</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{''.join(S)}</body></html>"""
open(OUT,"w").write(html)
print("OK ->",OUT,"·",len(S),"slides ·",os.path.getsize(OUT),"bytes")
