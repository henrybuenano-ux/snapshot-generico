#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del deck "Sistema para Clínicas" (omibu).
TEMPLATIZADO: cambiá el bloque CONFIG (marca, colores, logo) y re-ejecutá.
    python build_deck.py
Salida: omibu-sistema-clinicas.pptx
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os

# ============================ CONFIG (editar acá) ============================
BRAND      = "omibu"
SUBBRAND   = "Sistema de Captación, Atención y Reputación para Clínicas"
NICHOS     = "Odontología · Estética · Medicina estética"
LOGO_PATH  = ""               # poné la ruta de un PNG y aparece en la portada
PRIMARY    = RGBColor(0x0B, 0x1F, 0x3A)   # navy
ACCENT     = RGBColor(0x14, 0xB8, 0xA6)   # teal
ACCENT2    = RGBColor(0x25, 0x63, 0xEB)   # azul
INK        = RGBColor(0x0F, 0x17, 0x2A)
GRAY       = RGBColor(0x64, 0x74, 0x8B)
LIGHT      = RGBColor(0xF1, 0xF5, 0xF9)
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
FONT       = "Calibri"
OUT        = os.path.join(os.path.dirname(__file__), "omibu-sistema-clinicas.pptx")
# ===========================================================================

prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW, SH = prs.slide_width, prs.slide_height

def slide():
    return prs.slides.add_slide(BLANK)

def rect(s, l, t, w, h, fill, line=None, rounded=False):
    shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,
                             Inches(l), Inches(t), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if line is None: shp.line.fill.background()
    else: shp.line.color.rgb = line; shp.line.width = Pt(1)
    shp.shadow.inherit = False
    return shp

def text(s, l, t, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, sp=4):
    tb = s.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    if isinstance(runs[0], tuple): runs = [runs]
    for i, para in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_after = Pt(sp)
        for (txt, size, bold, color) in para:
            r = p.add_run(); r.text = txt
            r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = FONT
    return tb

def footer(s, n, title=""):
    rect(s, 0.55, 6.92, 12.2, 0.012, LIGHT)
    text(s, 0.55, 6.96, 9, 0.4, [[(f"{BRAND}  ·  {title}", 9, False, GRAY)]])
    text(s, 11.0, 6.96, 1.78, 0.4, [[(f"{n:02d} / 14", 9, False, GRAY)]], align=PP_ALIGN.RIGHT)

def head(s, kicker, title, sub):
    rect(s, 0.55, 0.6, 0.32, 0.32, ACCENT, rounded=True)
    text(s, 1.0, 0.5, 11, 0.5, [[(kicker.upper(), 11, True, ACCENT)]])
    text(s, 0.55, 0.95, 12.2, 0.9, [[(title, 30, True, PRIMARY)]])
    if sub: text(s, 0.55, 1.75, 12.2, 0.6, [[(sub, 15, False, GRAY)]])

def chain(s, items, top=3.2, h=1.5):
    n = len(items); gap = 0.2; total = 12.2
    w = (total - gap*(n-1)) / n
    for i, (t, d) in enumerate(items):
        l = 0.55 + i*(w+gap)
        c = rect(s, l, top, w, h, LIGHT, rounded=True)
        text(s, l+0.12, top+0.16, w-0.24, h-0.3,
             [[(t, 13, True, PRIMARY)], [(d, 10.5, False, GRAY)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < n-1:
            text(s, l+w-0.02, top, gap+0.04, h, [[("›", 20, True, ACCENT)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

def cards(s, items, top=2.6, h=3.2, cols=3):
    gap = 0.3; total = 12.2; w = (total - gap*(cols-1)) / cols
    for i, (title, body, accent) in enumerate(items):
        row, col = divmod(i, cols)
        l = 0.55 + col*(w+gap); t = top + row*(h+0.3)
        rect(s, l, t, w, h, LIGHT, rounded=True)
        rect(s, l, t, w, 0.14, accent, rounded=False)
        text(s, l+0.22, t+0.32, w-0.44, 0.7, [[(title, 15, True, PRIMARY)]])
        runs = [[("•  " + b, 11.5, False, INK)] for b in body]
        text(s, l+0.22, t+1.05, w-0.44, h-1.2, runs, sp=6)

# ---------------- S1 Portada ----------------
s = slide(); rect(s, 0, 0, SW.inches, SH.inches, PRIMARY)
rect(s, 0, 0, 0.25, SH.inches, ACCENT)
text(s, 1.0, 2.2, 11.5, 0.5, [[("GUÍA PARA EQUIPO Y CLIENTE", 13, True, ACCENT)]])
text(s, 1.0, 2.7, 11.5, 1.2, [[(BRAND, 54, True, WHITE)]])
text(s, 1.0, 3.9, 11.5, 0.9, [[(SUBBRAND, 22, False, WHITE)]])
text(s, 1.0, 4.8, 11.5, 0.5, [[(NICHOS, 15, False, ACCENT)]])
if LOGO_PATH and os.path.exists(LOGO_PATH):
    s.shapes.add_picture(LOGO_PATH, Inches(10.6), Inches(0.6), height=Inches(1.0))
text(s, 1.0, 6.3, 11.5, 0.5, [[("Cómo convertimos anuncios en pacientes —  y pacientes en reseñas de 5★.", 13, False, WHITE)]])

# ---------------- S2 Problema ----------------
s = slide(); head(s, "El problema", "El paciente escribe… y se pierde", "Lo que hoy le pasa a casi toda clínica que invierte en publicidad.")
cards(s, [
 ("Nadie contesta a tiempo", ["El lead escribe a las 22:00", "Le responden al otro día", "Ya agendó en otra clínica"], ACCENT2),
 ("Todo disperso", ["WhatsApp, Instagram, Facebook", "Mensajes que se traspapelan", "No se sabe de qué anuncio vino"], ACCENT2),
 ("Agenda con huecos", ["Citas sin recordatorio", "Ausencias y cancelaciones", "Sin seguimiento al que no agendó"], ACCENT2),
 ("Reputación al azar", ["Pocas reseñas en Google", "Las malas sí se publican", "Sin pedirlas de forma sistemática"], ACCENT2),
], top=2.55, h=1.9, cols=2)
footer(s, 2, "El problema")

# ---------------- S3 Solución ----------------
s = slide(); head(s, "La solución", "No es una herramienta. Es un SISTEMA.", "El snapshot de omibu: todo preconfigurado y conectado, sobre GoHighLevel.")
cards(s, [
 ("Captar", ["Atiende WhatsApp/IG/FB", "al instante, 24/7"], ACCENT),
 ("Convertir", ["IA reserva la cita", "y mueve el pipeline solo"], ACCENT),
 ("Fidelizar", ["Recordatorios + reseñas", "Google automáticas"], ACCENT),
], top=2.7, h=2.4)
text(s, 0.55, 5.6, 12.2, 0.8, [[("→ Una sola cuenta, las piezas se hablan entre sí, un solo costo. Listo para instalar.", 14, True, PRIMARY)]])
footer(s, 3, "La solución")

# ---------------- S4 Cómo funciona ----------------
s = slide(); head(s, "Cómo funciona", "El recorrido del paciente, en piloto automático", "De un clic en el anuncio a una reseña de 5★ —  sin que nadie mueva un dedo.")
chain(s, [("Anuncio / Redes","Meta Ads, IG, FB"),("Mensaje","WhatsApp/IG/FB"),("Sofía (IA)","atiende y califica"),
          ("Agenda","reserva la cita"),("Recordatorios","24h antes"),("Reseña","Google tras el servicio")], top=3.0, h=1.7)
text(s, 0.55, 5.4, 12.2, 0.9, [[("Resultado: el lead deja sus datos → la IA lo atiende → agenda solo → asiste → deja reseña → vuelve.", 14, True, ACCENT)]])
footer(s, 4, "Cómo funciona")

# ---------------- S5 Sofía IA ----------------
s = slide(); head(s, "El asistente IA", "Sofía: tu recepcionista que no duerme", "Atiende cada mensaje al instante, en el tono de la clínica, y reserva citas sola.")
cards(s, [
 ("Atiende 24/7", ["Responde en segundos", "Sin sueldo ni descansos", "Mismo tono de la marca"], ACCENT),
 ("Reserva citas", ["Ofrece día y hora libres", "Agenda en el calendario", "Pide datos con consentimiento RGPD"], ACCENT),
 ("Sabe cuándo parar", ["Deriva a humano si hace falta", "Comprobantes, dudas médicas", "Nunca inventa precios"], ACCENT),
], top=2.7, h=2.6)
footer(s, 5, "Asistente IA")

# ---------------- S6 Multicanal ----------------
s = slide(); head(s, "Captación", "Todos los canales en una bandeja —  y sabés de dónde vino cada lead", "")
cards(s, [
 ("Multicanal", ["WhatsApp, Instagram, Facebook", "Una sola conversación por paciente", "Nada se traspapela"], ACCENT2),
 ("Atribución de anuncios", ["Guarda UTM y el anuncio (Ad)", "Sabés qué campaña trae pacientes", "Mides retorno real por fuente"], ACCENT2),
 ("Canal detectado", ["Etiqueta canal-whatsapp/ig/fb", "La IA pide el teléfono solo si hace falta", "Listo para remarketing"], ACCENT2),
], top=2.7, h=2.6)
footer(s, 6, "Captación multicanal")

# ---------------- S7 Pipeline ----------------
s = slide(); head(s, "Pipeline de ventas", "Ves en qué punto está cada paciente", "Cada oportunidad avanza por etapas claras —  como una operación con fases.")
chain(s, [("Nuevo Lead",""),("En conversación",""),("Pre-reserva",""),("Cita Reservada",""),("Cita Confirmada",""),("Servicio Realizado",""),("No reservó",""),], top=3.2, h=1.4)
text(s, 0.55, 5.2, 12.2, 1.0, [[("Los robots mueven al paciente de etapa automáticamente. Vos ves el tablero y sabés exactamente qué falta para cada cierre.", 14, False, GRAY)]])
footer(s, 7, "Pipeline de ventas")

# ---------------- S8 Automatizaciones ----------------
s = slide(); head(s, "Automatizaciones", "9 robots que trabajan solos", "Configurados y listos. Cada uno hace una tarea sin que nadie la recuerde.")
cards(s, [
 ("Bienvenida + IA", ["Activa a Sofía", "Crea la oportunidad"], ACCENT),
 ("Cita reservada", ["Confirma por WhatsApp", "Mueve el pipeline"], ACCENT),
 ("Recordatorio 24h", ["Reduce ausencias", "Mensaje automático"], ACCENT),
 ("Remarketing", ["Recupera al que no agendó", "2 toques en 48h"], ACCENT),
 ("Señal / depósito", ["Valida el pago", "Confirma la cita"], ACCENT),
 ("Reputación Google", ["Pide reseña tras el servicio", "Filtra 4-5★ → Google"], ACCENT),
], top=2.55, h=1.85, cols=3)
footer(s, 8, "Automatizaciones")

# ---------------- S9 Reputación ----------------
s = slide(); head(s, "Reputación Google (RBD)", "Más reseñas de 5★ —  y las malas, en privado", "El diferenciador: pide valoración tras cada servicio y filtra antes de Google.")
rect(s, 0.55, 2.7, 5.9, 2.6, LIGHT, rounded=True); rect(s, 0.55, 2.7, 5.9, 0.14, ACCENT)
text(s, 0.8, 3.0, 5.4, 2.2, [[("⭐ 4–5 estrellas", 16, True, PRIMARY)], [("→ va directo a dejar la reseña en Google", 12.5, False, INK)], [("Más reputación pública, más pacientes nuevos.", 12, False, GRAY)]], sp=8)
rect(s, 6.85, 2.7, 5.9, 2.6, LIGHT, rounded=True); rect(s, 6.85, 2.7, 5.9, 0.14, ACCENT2)
text(s, 7.1, 3.0, 5.4, 2.2, [[("⭐ 1–3 estrellas", 16, True, PRIMARY)], [("→ va a un formulario privado (no a Google)", 12.5, False, INK)], [("Recuperás al paciente y proteges la reputación.", 12, False, GRAY)]], sp=8)
text(s, 0.55, 5.6, 12.2, 0.7, [[("También reactiva tu base de datos antigua para traer pacientes que ya tenías.", 13.5, True, ACCENT)]])
footer(s, 9, "Reputación Google")

# ---------------- S10 Por nicho ----------------
s = slide(); head(s, "Adaptable por nicho", "El mismo sistema, ajustado a cada clínica", "Cambia el catálogo, el tono y si se pide señal. La estrategia es la misma.")
cards(s, [
 ("Odontología", ["Limpieza, ortodoncia, blanqueamiento", "Tono cercano y claro", "Señal: normalmente no"], ACCENT2),
 ("Estética / Belleza", ["Faciales, micropigmentación, depilación", "Tono cálido", "Señal: habitual (sí)"], ACCENT),
 ("Medicina estética", ["Ácido, bótox, tratamientos", "Tono profesional", "Dudas clínicas → a humano"], ACCENT2),
], top=2.7, h=2.7)
footer(s, 10, "Por nicho")

# ---------------- S11 Templatizado ----------------
s = slide(); head(s, "Instalación", "Templatizado: solo cambian 3–4 cosas", "El sistema completo ya está montado. Personalizar un cliente toma horas, no semanas.")
cards(s, [
 ("Se personaliza", ["Logo y colores", "Datos del negocio", "Servicios y precios", "¿Pide señal? sí/no"], ACCENT),
 ("Ya viene hecho", ["Bot, pipeline y etapas", "Los 9 workflows", "Reputación Google (RBD)", "Plantillas de mensajes"], ACCENT2),
 ("Cómo se llena", ["Custom Values (1 sola vez)", "Todo lo lee el sistema", "Mismo snapshot para todos", "Onboarding por formulario"], ACCENT),
], top=2.7, h=2.7)
footer(s, 11, "Instalación templatizada")

# ---------------- S12 Antes / Después ----------------
s = slide(); head(s, "El cambio", "Antes vs. Después", "Lo que ve el dueño de la clínica cuando enciende el sistema.")
rect(s, 0.55, 2.7, 5.9, 3.4, LIGHT, rounded=True); rect(s, 0.55, 2.7, 5.9, 0.14, GRAY)
text(s, 0.85, 3.0, 5.4, 3.0, [[("ANTES", 15, True, GRAY)],
 [("—  Leads que escriben y nadie contesta", 12.5, False, INK)],
 [("—  Agenda con huecos y ausencias", 12.5, False, INK)],
 [("—  Mensajes perdidos entre apps", 12.5, False, INK)],
 [("—  Pocas reseñas, y las malas públicas", 12.5, False, INK)],
 [("—  Sin saber qué anuncio funciona", 12.5, False, INK)]], sp=8)
rect(s, 6.85, 2.7, 5.9, 3.4, LIGHT, rounded=True); rect(s, 6.85, 2.7, 5.9, 0.14, ACCENT)
text(s, 7.15, 3.0, 5.4, 3.0, [[("DESPUÉS", 15, True, ACCENT)],
 [("✓  Cada lead atendido en segundos, 24/7", 12.5, False, INK)],
 [("✓  Agenda llena, con recordatorios", 12.5, False, INK)],
 [("✓  Todo en una bandeja, nada se pierde", 12.5, False, INK)],
 [("✓  Flujo constante de reseñas 5★", 12.5, False, INK)],
 [("✓  Retorno medible por campaña", 12.5, False, INK)]], sp=8)
footer(s, 12, "Antes vs Después")

# ---------------- S13 Planes (placeholder) ----------------
s = slide(); head(s, "Planes omibu", "Cada plan de ads, enchufado al sistema", "El anuncio trae el lead; el sistema lo convierte y lo fideliza. Juntos = resultado.")
rect(s, 0.55, 2.6, 12.2, 1.0, RGBColor(0xFE,0xF3,0xC7), rounded=True)
text(s, 0.8, 2.75, 11.7, 0.8, [[("⚠️  PENDIENTE: insertar precios/planes de ads de omibu (Excel/PDF). ", 13, True, RGBColor(0x92,0x40,0x0E)),
                                  ("Mandámelo y completo esta sección con los planes reales.", 13, False, RGBColor(0x92,0x40,0x0E))]])
cards(s, [
 ("Plan [Inicial]", ["Inversión ads: $___", "Setup snapshot incluido", "Ideal: 1 nicho / 1 sede"], ACCENT2),
 ("Plan [Crecimiento]", ["Inversión ads: $___", "Snapshot + optimización", "Más campañas / canales"], ACCENT),
 ("Plan [Escala]", ["Inversión ads: $___", "Snapshot + gestión integral", "Multi-sede / multi-nicho"], ACCENT2),
], top=3.85, h=2.5)
footer(s, 13, "Planes + sistema")

# ---------------- S14 Cierre ----------------
s = slide(); rect(s, 0, 0, SW.inches, SH.inches, PRIMARY); rect(s, 0, 0, 0.25, SH.inches, ACCENT)
text(s, 1.0, 2.1, 11.5, 0.5, [[("EN RESUMEN", 13, True, ACCENT)]])
text(s, 1.0, 2.6, 11.5, 1.6, [[("Un sistema probado que capta,", 30, True, WHITE)],
                               [("atiende y fideliza —  solo.", 30, True, WHITE)]], sp=2)
text(s, 1.0, 4.4, 11.5, 1.4, [[("✓  Instalado y operativo sobre GoHighLevel", 15, False, WHITE)],
                               [("✓  En español, adaptable a odontología, estética y medicina", 15, False, WHITE)],
                               [("✓  Templatizado: nuevo cliente en horas", 15, False, WHITE)]], sp=8)
text(s, 1.0, 6.2, 11.5, 0.6, [[("omibu  ·  info@omibu.com", 14, True, ACCENT)]])

prs.save(OUT)
print("OK ->", OUT, "·", len(prs.slides.__iter__.__self__._sldIdLst), "slides")
