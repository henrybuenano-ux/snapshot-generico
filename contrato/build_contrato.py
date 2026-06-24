#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrato omnia (Sistema Ads + CRM) — HTML estilo de marca + PDF (weasyprint).
Plantilla genérica: los {{merge fields}} se muestran como chips.
Salida: contrato/omnia-contrato.html  +  contrato/omnia-contrato.pdf
"""
import os, re, base64, ssl, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "presentacion", "assets")
OUT_HTML = os.path.join(HERE, "omnia-contrato.html")
OUT_PDF  = os.path.join(HERE, "omnia-contrato.pdf")
CTX = ssl.create_default_context()

def b64_file(p):
    return base64.b64encode(open(p, "rb").read()).decode() if os.path.exists(p) else ""

LOGO  = b64_file(os.path.join(ASSETS, "omnia-logo.png"))
LOGOW = b64_file(os.path.join(ASSETS, "omnia-logo-white.png"))

# ── Fuentes de marca (TTF variables locales) incrustadas en base64 ─────────
def brand_fonts():
    """@font-face con las TTF variables de marca (Outfit + Plus Jakarta Sans).
    Self-contained (base64) para que HTML y PDF lleven la tipografía omnia."""
    spec = [("Outfit", "Outfit.ttf"), ("Plus Jakarta Sans", "PlusJakartaSans.ttf")]
    out = []
    for fam, fn in spec:
        p = os.path.join(HERE, "fonts", fn)
        if not os.path.exists(p):
            print(f"  fuente {fam}: no encontrada, fallback")
            continue
        d = base64.b64encode(open(p, "rb").read()).decode()
        out.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:100 900;"
                   f"src:url(data:font/ttf;base64,{d}) format('truetype');}}")
    if out:
        print(f"  fuentes de marca incrustadas: {len(out)}")
    return "\n".join(out)

FONTS = brand_fonts()
SANS = "'Plus Jakarta Sans','Liberation Sans','DejaVu Sans',sans-serif"
HEAD = "'Outfit','Plus Jakarta Sans','Liberation Sans',sans-serif"

CSS = r"""
""" + FONTS + r"""
*{box-sizing:border-box}
:root{--grad:linear-gradient(120deg,#4f46e5 0%,#7c3aed 52%,#db2777 100%);
  --ink:#11131c;--muted:#52525b;--soft:#6b7280;--line:#e8e4f5;--violet:#7c3aed;--ind:#4f46e5}
@page{size:A4;margin:20mm 16mm 16mm;
  @bottom-left{content:"omnia · Sistema Ads + CRM para Clínicas";font-family:HEADFONT;font-size:7.4pt;color:#a7a3b8}
  @bottom-right{content:"Pág. " counter(page) " / " counter(pages);font-family:HEADFONT;font-size:7.4pt;color:#a7a3b8}}
@page:first{margin:0 16mm 16mm}
html{font-size:10.3pt}
body{font-family:BODYFONT;color:var(--ink);line-height:1.5;margin:0;-weasy-font-smoothing:antialiased}
h1,h2,h3,.head{font-family:HEADFONT;letter-spacing:-.01em}
/* portada */
.cover{background:var(--grad);color:#fff;margin:0 -16mm 9mm;padding:20mm 16mm 11mm;position:relative}
.cover img{height:42px;margin-bottom:16px}
.cover h1{font-size:21pt;font-weight:800;line-height:1.12;max-width:24ch;margin:0}
.cover .lead{color:rgba(255,255,255,.92);margin-top:8px;font-size:10.5pt;max-width:60ch}
.badges{margin-top:14px;display:flex;gap:7px;flex-wrap:wrap}
.badge{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.34);border-radius:999px;
  padding:4px 11px;font-size:8pt;font-weight:600;font-family:HEADFONT;letter-spacing:.02em}
.conf{position:absolute;top:14px;right:16mm;background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.42);
  border-radius:999px;padding:4px 11px;font-size:7.4pt;font-weight:800;font-family:HEADFONT;letter-spacing:.08em}
/* avisos */
.legal{background:#fff7ed;border:1px solid #fed7aa;color:#9a3412;border-radius:11px;
  padding:11px 14px;font-size:8.6pt;margin:0 0 9mm;line-height:1.45}
.legal b{color:#9a3412}
.intro{color:var(--muted);font-size:9.4pt;margin:0 0 7mm}
/* clausulas */
h2.cl{font-size:12.5pt;font-weight:800;color:var(--ink);margin:7mm 0 2.5mm;padding-bottom:3px;
  border-bottom:2px solid transparent;border-image:var(--grad) 1;break-after:avoid}
h2.cl .n{color:var(--violet)}
h3.sub{font-size:10pt;font-weight:700;color:var(--ind);margin:4mm 0 1.5mm;break-after:avoid}
p{margin:0 0 2.4mm}
ul{margin:0 0 3mm;padding-left:0;list-style:none}
li{position:relative;padding-left:15px;margin-bottom:1.6mm;color:#2b2d3a}
li:before{content:"";position:absolute;left:2px;top:.62em;width:5px;height:5px;border-radius:50%;background:var(--violet)}
ul.az>li{padding-left:18px}ul.az>li:before{display:none}
ul.az>li>b.k{position:absolute;left:0;color:var(--violet);font-family:HEADFONT}
.callout{background:#f5f3fc;border:1px solid var(--line);border-left:3px solid var(--violet);
  border-radius:10px;padding:9px 13px;font-size:9pt;color:#3b3550;margin:0 0 3mm;break-inside:avoid}
.callout b{color:var(--violet)}
strong{color:#1c1330}
/* tablas */
table{width:100%;border-collapse:collapse;margin:2mm 0 4mm;font-size:9pt;break-inside:avoid}
th{background:#171430;color:#fff;font-family:HEADFONT;font-weight:700;text-align:left;padding:7px 11px;font-size:8.4pt}
td{padding:6.5px 11px;border-top:1px solid var(--line);vertical-align:top}
tr:nth-child(even) td{background:#faf9fe}
table.fill td:first-child{font-family:HEADFONT;color:var(--ind);font-weight:600;white-space:nowrap;width:38%}
/* merge fields */
.mf{background:#ede9fe;color:#5b21b6;border:1px solid #ddd6fe;border-radius:5px;
  padding:.5px 5px;font-size:8.4pt;font-family:'DejaVu Sans Mono',monospace;white-space:nowrap}
/* firmas */
.sign{display:flex;gap:18px;margin-top:6mm;break-inside:avoid}
.sign .box{flex:1;border:1px solid var(--line);border-radius:12px;padding:13px 15px}
.sign .who{font-family:HEADFONT;font-weight:800;color:var(--ink);font-size:9.5pt;margin-bottom:18px}
.sign .ln{border-top:1px solid #c9c4dd;margin-top:20px;padding-top:5px;font-size:8.4pt;color:var(--soft)}
.kv{font-size:8.6pt;color:var(--muted);margin-top:4px}
.end{margin-top:6mm;font-family:HEADFONT;font-weight:700;text-align:center;color:var(--ink);font-size:10pt}
""".replace("HEADFONT", HEAD).replace("BODYFONT", SANS)


def mf(s):
    """Envuelve {{merge fields}} en chips."""
    return re.sub(r"(\{\{[^}]+\}\})", r'<span class="mf">\1</span>', s)


BODY = mf(r"""
<section class="cover">
  <div class="conf">CONFIDENCIAL</div>
  <img src="data:image/png;base64,LOGOW_B64" alt="omnia">
  <h1>Contrato de Prestación de Servicios</h1>
  <div class="lead">Sistema Ads + CRM para Clínicas — captación, atención 24/7 con IA y reputación, en un solo sistema con una sola factura.</div>
  <div class="badges"><span class="badge">omnia</span><span class="badge">Plantilla genérica</span><span class="badge">España · RGPD</span></div>
</section>

<div class="legal"><b>Plantilla orientativa.</b> Rellenar los campos <span class="mf">{{…}}</span> por cliente (merge fields de GHL). Este documento <b>no constituye asesoramiento jurídico</b>: debe ser revisado y validado por asesoría legal antes de su uso, y adaptado a la legislación vigente (España / UE).</div>

<h2 class="cl"><span class="n">Datos</span> a rellenar (custom fields / custom values)</h2>
<table class="fill">
<tr><td>Prestador (omnia)</td><td>{{custom_values.omnia_razon_social}} · {{custom_values.omnia_cif}} · {{custom_values.omnia_domicilio}} · {{custom_values.omnia_email}}</td></tr>
<tr><td>Cliente</td><td>{{contact.company_name}} — repr. {{contact.full_name}} · {{contact.email}} · {{contact.phone}}</td></tr>
<tr><td>NIF/CIF y domicilio del Cliente</td><td>{{custom_values.cliente_cif}} · {{custom_values.cliente_domicilio}}</td></tr>
<tr><td>Plan contratado</td><td>{{custom_values.plan_contratado}} (Captación·Z / Crecimiento·S / Pro·P / Escala·T)</td></tr>
<tr><td>Canales de ads</td><td>{{custom_values.canales_ads}} (Google y/o Meta)</td></tr>
<tr><td>Activación / Mensualidad</td><td>{{custom_values.cuota_activacion}} · {{custom_values.cuota_mensual}} ({{custom_values.desglose_mensual}})</td></tr>
<tr><td>Permanencia / Preaviso</td><td>{{custom_values.permanencia}} · {{custom_values.preaviso_baja}}</td></tr>
<tr><td>Fecha de firma</td><td>{{custom_values.fecha_contrato}}</td></tr>
</table>

<p class="intro">En {{custom_values.omnia_domicilio}}, a {{custom_values.fecha_contrato}}.</p>

<h3 class="sub">REUNIDOS</h3>
<p>De una parte, <strong>{{custom_values.omnia_razon_social}}</strong> (en adelante, «<strong>omnia</strong>» o «el Prestador»), con CIF {{custom_values.omnia_cif}} y domicilio en {{custom_values.omnia_domicilio}}.</p>
<p>De otra parte, <strong>{{contact.company_name}}</strong> (en adelante, «el Cliente»), con NIF/CIF {{custom_values.cliente_cif}} y domicilio en {{custom_values.cliente_domicilio}}, representada por {{contact.full_name}}.</p>
<p>Ambas partes se reconocen capacidad legal suficiente para contratar y <strong>ACUERDAN</strong>:</p>

<h2 class="cl"><span class="n">1.</span> Objeto</h2>
<p>omnia prestará al Cliente el servicio <strong>«Sistema Ads + CRM para Clínicas»</strong>: la instalación y puesta en marcha de un sistema CRM preconfigurado (en adelante, el «Sistema») sobre la plataforma GoHighLevel, junto con la <strong>gestión de campañas publicitarias</strong> (Google/Meta) según el plan <strong>{{custom_values.plan_contratado}}</strong>.</p>

<h2 class="cl"><span class="n">2.</span> Alcance del servicio (capacidades — qué incluye)</h2>
<div class="callout">El <b>Sistema CRM es idéntico en los cuatro planes</b> (Z / S / P / T). Lo único que varía entre planes es el <b>alcance de la gestión de publicidad</b> (cláusula 2.3).</div>
<h3 class="sub">2.1. Sistema CRM «omnia para Clínicas» (instalación templatizada sobre GoHighLevel)</h3>
<p>Se entrega tal y como está configurado en el snapshot estándar de omnia, e incluye:</p>
<ul>
<li><strong>Asistente virtual con IA</strong> (1 asistente, en castellano): atención automatizada por chat, respuesta a preguntas frecuentes, cualificación de leads, <strong>reserva de citas</strong> y derivación a persona humana (<em>handoff</em>).</li>
<li><strong>Embudo de ventas:</strong> 1 pipeline de ventas estándar con sus etapas (lead → contacto → cita → asistencia → ganado / perdido).</li>
<li><strong>Automatizaciones estándar (workflows):</strong> bienvenida y activación del bot, pre-reserva, recordatorio de cita (24 h), remarketing a leads sin reservar, normalización del servicio de interés, confirmación de señal/depósito (si aplica), handoff a humano, baja/opt-out y solicitud de reseña.</li>
<li><strong>Módulo de reputación y reseñas de Google:</strong> reactivación de base de datos, captación de reseñas de 5★, redirección a Google y gestión de valoraciones.</li>
<li><strong>Formulario de alta (onboarding)</strong> con volcado automático de los datos del negocio a la configuración del Sistema.</li>
<li><strong>Calendario de citas:</strong> 1 calendario (zona horaria, duración y disponibilidad).</li>
<li><strong>Catálogo de servicios:</strong> hasta 6 servicios con su precio.</li>
<li><strong>Plantillas de mensajería estándar</strong> (WhatsApp / email / SMS) del snapshot.</li>
<li><strong>Personalización del snapshot</strong> a partir del formulario de alta: logotipo (vertical y horizontal), colores, datos del negocio, catálogo de servicios y precios, horarios, FAQ, política de privacidad y textos.</li>
</ul>
<div class="callout">El Sistema entregado es el <b>snapshot estándar de omnia (producto MVP)</b>. La personalización se limita a <b>marca, datos y textos</b>; no incluye desarrollos, lógica, integraciones ni automatizaciones a medida fuera del snapshot (cláusula 3).</div>
<h3 class="sub">2.2. Gestión de publicidad ({{custom_values.canales_ads}})</h3>
<p>Configuración, puesta en marcha y optimización de las campañas, dentro de los límites del plan <strong>{{custom_values.plan_contratado}}</strong>.</p>
<h3 class="sub">2.3. Alcance de publicidad por plan (lo único que cambia entre planes)</h3>
<table>
<tr><th>Plan</th><th>Gestión de ads incluida</th></tr>
<tr><td><strong>Captación · Z</strong></td><td>1 canal (Google <strong>o</strong> Meta)</td></tr>
<tr><td><strong>Crecimiento · S</strong></td><td>2 canales (Google <strong>y</strong> Meta) + analítica</td></tr>
<tr><td><strong>Pro · P</strong></td><td>Gestión avanzada + redistribución de presupuesto</td></tr>
<tr><td><strong>Escala · T</strong></td><td>Multi-sede / multi-campaña + reporting a medida</td></tr>
</table>
<h3 class="sub">2.4. Soporte</h3>
<p>Mantenimiento del Sistema en horario laboral (L-V).</p>

<h2 class="cl"><span class="n">3.</span> Límites y exclusiones (qué NO incluye)</h2>
<h3 class="sub">3.1. Naturaleza del producto</h3>
<p>El Sistema es un <strong>producto estándar (MVP)</strong>: se entrega <strong>tal cual</strong>, con <strong>ajustes limitados</strong> (marca, datos, textos y catálogo). No se modifican los workflows, las etapas del pipeline ni la lógica del asistente más allá de la configuración estándar.</p>
<h3 class="sub">3.2. Límites cuantitativos del Sistema</h3>
<p>Ampliar cualquiera de ellos se rige por la cláusula 9.</p>
<table>
<tr><th>Elemento</th><th>Incluido en el estándar</th></tr>
<tr><td>Asistente virtual (IA)</td><td>1, en castellano</td></tr>
<tr><td>Pipeline de ventas</td><td>1 (estándar)</td></tr>
<tr><td>Calendario de citas</td><td>1</td></tr>
<tr><td>Catálogo de servicios</td><td>hasta 6</td></tr>
<tr><td>Workflows / plantillas</td><td>los del snapshot estándar</td></tr>
<tr><td>Idiomas</td><td>1 (castellano)</td></tr>
</table>
<h3 class="sub">3.3. Exclusiones</h3>
<p>Salvo pacto expreso por escrito, <strong>NO</strong> están incluidos:</p>
<ul class="az">
<li><b class="k">a)</b> Desarrollos, automatizaciones (workflows) o funcionalidades <strong>adicionales</strong> a las del snapshot estándar.</li>
<li><b class="k">b)</b> Integraciones con sistemas de terceros no contempladas en el Sistema.</li>
<li><b class="k">c)</b> Diseño/desarrollo de páginas web, landing pages o funnels fuera de lo incluido en el plan.</li>
<li><b class="k">d)</b> Creatividades, fotografía o <strong>vídeos</strong> para anuncios (servicio aparte).</li>
<li><b class="k">e)</b> La <strong>inversión publicitaria</strong> (presupuesto que se paga a Google/Meta).</li>
<li><b class="k">f)</b> Los <strong>costes de comunicación y de terceros</strong> (ver cláusula 5).</li>
<li><b class="k">g)</b> Migraciones de datos, formaciones adicionales o consultoría fuera de alcance.</li>
<li><b class="k">h)</b> Soporte fuera de horario, SLA premium o incidencias imputables a plataformas de terceros.</li>
<li><b class="k">i)</b> Garantía de resultados comerciales concretos (nº de leads, citas o ventas).</li>
</ul>
<div class="callout"><b>Cualquier requerimiento no listado en la cláusula 2 se considera fuera de alcance</b> y se regirá por la cláusula 9.</div>

<h2 class="cl"><span class="n">4.</span> Precio y forma de pago</h2>
<ul>
<li><strong>Activación (pago único):</strong> {{custom_values.cuota_activacion}} + IVA, al inicio para la puesta en marcha.</li>
<li><strong>Cuota mensual:</strong> {{custom_values.cuota_mensual}} + IVA ({{custom_values.desglose_mensual}}).</li>
<li><strong>Primer mes:</strong> activación + primera mensualidad. <strong>Desde el segundo mes:</strong> solo la mensualidad.</li>
<li>Los precios se entienden <strong>sin IVA</strong>, que se repercutirá según normativa.</li>
<li>El impago de cualquier cuota faculta a omnia a <strong>suspender</strong> el servicio hasta su regularización (cláusula 10).</li>
</ul>

<h2 class="cl"><span class="n">5.</span> Costes de terceros (operativos) — a cargo del Cliente</h2>
<p>Los siguientes consumos se pagan <strong>directamente a los proveedores</strong> según el uso real y <strong>no los factura omnia</strong>; el Cliente mantiene la titularidad de dichas cuentas:</p>
<ul>
<li><strong>Licencia de Meta (WhatsApp Business):</strong> cuota mensual fija del proveedor.</li>
<li><strong>Conversaciones de WhatsApp</strong> (plantillas por conversación iniciada).</li>
<li><strong>Tokens de IA</strong> del asistente: por volumen o plan ilimitado.</li>
<li><strong>Envío de correos/SMS</strong> y, en su caso, telefonía.</li>
<li>La <strong>inversión publicitaria</strong> en Google/Meta.</li>
</ul>
<p>omnia facilitará estimaciones orientativas, sin que constituyan importe garantizado.</p>

<h2 class="cl"><span class="n">6.</span> Obligaciones del Cliente</h2>
<ul>
<li>Aportar de forma veraz y en plazo los <strong>datos y accesos</strong> necesarios (formulario de alta, cuentas de WhatsApp/Meta/Google, dominios, etc.).</li>
<li>Revisar y <strong>aprobar</strong> los contenidos y la configuración.</li>
<li>Cumplir las <strong>políticas</strong> de Meta, Google y WhatsApp, así como la normativa aplicable.</li>
<li>Realizar los pagos en los plazos pactados.</li>
</ul>

<h2 class="cl"><span class="n">7.</span> Obligaciones de omnia</h2>
<ul>
<li>Instalar y poner en marcha el Sistema según la cláusula 2.</li>
<li>Gestionar la publicidad dentro de los límites del plan.</li>
<li>Prestar el soporte de mantenimiento acordado.</li>
</ul>

<h2 class="cl"><span class="n">8.</span> Duración, renovación y baja</h2>
<ul>
<li><strong>Duración:</strong> indefinida, con <strong>permanencia mínima</strong> de {{custom_values.permanencia}} desde la activación.</li>
<li><strong>Renovación:</strong> mensual automática salvo baja.</li>
<li><strong>Baja:</strong> cualquiera de las partes podrá resolver con un <strong>preaviso</strong> de {{custom_values.preaviso_baja}}. La activación no es reembolsable.</li>
</ul>

<h2 class="cl"><span class="n">9.</span> Modificaciones del alcance, nuevos trabajos y upsells</h2>
<p>Toda solicitud de servicios, funcionalidades o cambios <strong>no incluidos</strong> en la cláusula 2 (ver exclusiones de la cláusula 3):</p>
<ul class="az">
<li><b class="k">a)</b> Se <strong>cotizará por separado</strong> mediante presupuesto escrito (nuevo alcance) o se ofrecerá como <strong>upsell</strong>.</li>
<li><b class="k">b)</b> <strong>No se iniciará</strong> ni se entenderá incluida hasta su <strong>aceptación expresa por escrito</strong> y, en su caso, pago.</li>
<li><b class="k">c)</b> Podrá facturarse como pago único, como ampliación de la cuota mensual o como nuevo producto, según corresponda.</li>
</ul>
<p>Ningún trabajo fuera de alcance se considera comprometido por el mero hecho de solicitarse.</p>

<h2 class="cl"><span class="n">10.</span> Suspensión y resolución</h2>
<p>omnia podrá <strong>suspender o resolver</strong> el contrato en caso de impago, uso indebido del Sistema, incumplimiento de las políticas de terceros o de las obligaciones del Cliente. La resolución no exime de los importes devengados.</p>

<h2 class="cl"><span class="n">11.</span> Propiedad intelectual</h2>
<ul>
<li>El <strong>Sistema, el snapshot, las automatizaciones, las plantillas y la metodología</strong> son propiedad de omnia; el Cliente recibe un <strong>derecho de uso</strong> mientras esté vigente el contrato y al corriente de pago.</li>
<li>Los <strong>datos, contactos, cuentas y contenidos</strong> del Cliente son de su titularidad.</li>
<li>A la finalización, cesa el derecho de uso del Sistema; el Cliente conserva sus datos y cuentas de terceros.</li>
</ul>

<h2 class="cl"><span class="n">12.</span> Protección de datos (RGPD)</h2>
<ul>
<li>El Cliente es <strong>Responsable del tratamiento</strong> y omnia, <strong>Encargado del tratamiento</strong>, conforme al RGPD (UE 2016/679) y la LOPDGDD. Se suscribirá el correspondiente <strong>contrato de encargo</strong> (anexo).</li>
<li>omnia tratará los datos solo para prestar el servicio y guardará <strong>confidencialidad</strong>.</li>
</ul>

<h2 class="cl"><span class="n">13.</span> Garantías y limitación de responsabilidad</h2>
<ul>
<li>omnia presta el servicio con diligencia profesional, <strong>sin garantizar resultados comerciales concretos</strong> (leads, citas o ventas), por depender de factores ajenos (mercado, inversión, plataformas de terceros).</li>
<li>omnia <strong>no responde</strong> de fallos, cambios de política, costes o suspensiones de plataformas de terceros (Meta, Google, GoHighLevel).</li>
<li>La responsabilidad de omnia se limita, como máximo, al importe de las <strong>cuotas del último mes</strong> facturadas.</li>
</ul>

<h2 class="cl"><span class="n">14.</span> Confidencialidad</h2>
<p>Ambas partes mantendrán confidencial la información a la que accedan con motivo del contrato.</p>

<h2 class="cl"><span class="n">15.</span> Legislación y jurisdicción</h2>
<p>El contrato se rige por la <strong>legislación española</strong>. Para cualquier controversia, las partes se someten a los <strong>Juzgados y Tribunales</strong> del domicilio de omnia, salvo norma imperativa en contrario.</p>

<p class="end">Y en prueba de conformidad, ambas partes firman el presente contrato.</p>
<div class="sign">
  <div class="box"><div class="who">Por omnia</div><div class="kv">{{custom_values.omnia_razon_social}}</div><div class="ln">Firma y fecha</div></div>
  <div class="box"><div class="who">Por el Cliente</div><div class="kv">{{contact.company_name}}</div><div class="ln">Firma y fecha</div></div>
</div>
""").replace("LOGOW_B64", LOGOW)

HTML = f"<!doctype html><html lang='es'><head><meta charset='utf-8'><title>Contrato omnia — Sistema Ads + CRM</title><style>{CSS}</style></head><body>{BODY}</body></html>"

open(OUT_HTML, "w", encoding="utf-8").write(HTML)
print("HTML ->", OUT_HTML, f"({len(HTML)//1024} KB)")

from weasyprint import HTML as WHTML
WHTML(string=HTML, base_url=HERE).write_pdf(OUT_PDF)
print("PDF  ->", OUT_PDF, f"({os.path.getsize(OUT_PDF)//1024} KB)")
