# SNAPSHOT ESTÉTICO / MÉDICO-ESTÉTICO / ODONTOLOGÍA — Estado del build

> Sub-cuenta GHL: **Odontologico / Estetico / Medico.** · Location ID `c8FNGEjTOUL3VfR43w7e`
> Build automatizado vía API pública (PIT) + API interna (Firebase). Decisiones: **señal = configurable** (WF-06 off por defecto, T02-b), **rebuild limpio**.
> Última actualización: build inicial.

---

## ✅ / ⏳ / ✋ ESTADO POR CAPA

| Capa | Estado | Cómo |
|---|---|---|
| Custom Fields | ✅ **Hecho** (13, alineados al blueprint) | API pública |
| Custom Values | ✅ **Hecho** (39, keys exactos) | API pública |
| Tags | ✅ **Hecho** (24, set del blueprint) | API pública |
| Pipeline Ventas (7 etapas) | ✅ **Hecho** (colores bg-tint) | API interna |
| Pipeline Reactivación/Reseñas (8 etapas) | ✅ **Hecho** | API interna |
| Calendario | ⏳ **Parcial** — existe pero requiere config (disponibilidad/equipo) y activar en UI | manual |
| Workflows Ventas (WF-01…09) | ✅ **Construidos** (drafts). Ver notas + pasos manuales abajo | API interna |
| Workflows RBD (01–09) | ✅ Instalados por tu snapshot (published). Revisión abajo | snapshot |
| Plantillas WhatsApp (T01–T05) | ✋ **Manual** — enviar a Meta (no hay API). Texto listo abajo | UI + Meta |
| Prompt del Bot (Conversation AI) | ✋ **Manual** — pegar 3 partes (listas abajo) | UI |
| Forms + Survey (RBD) | ✋ **Manual** — spec abajo | UI |

Leyenda: ✅ hecho en la cuenta · ⏳ pendiente/automatizable · ✋ requiere hacerse a mano (la plataforma no lo expone por API).

---

## 📇 REFERENCIA EN VIVO (IDs reales de la cuenta)

### Pipelines
**Ventas** · `tdJDN8gzjuhTAHm2htjU`
| # | Etapa | Stage ID |
|---|---|---|
| 0 | Nuevo Lead | `541fac76-03b3-454e-bf3b-3045a341c404` |
| 1 | En conversación humana | `7d59b568-1660-460f-af32-25a44f61e60b` |
| 2 | Pre-reserva | `02de8371-8f48-4526-9138-d99ad69a8d05` |
| 3 | Cita Reservada | `1c3ef98b-db7e-4752-915b-6f6328507298` |
| 4 | Cita Confirmada (señal validada) | `507447d6-91a6-46a0-abbd-c3ef294b9a04` |
| 5 | Servicio Realizado *(WON)* | `ae4bd9f4-efd2-4ff3-b714-41ba21b45cfd` |
| 6 | No Reservó / No Asistió *(LOST)* | `b10e4a4d-a2a2-4c69-8785-6a4416e70d40` |

**Reactivación / Reseñas** · `39zSRuGjENJx3ajHI9Bu`
| # | Etapa | Stage ID |
|---|---|---|
| 0 | Mensaje enviado | `9d1f124e-06a9-445f-9ca4-15e47098dbad` |
| 1 | WhatsApp inválido | `49570010-908c-42d2-8048-1aea71997abd` |
| 2 | Respondió | `d08c996c-27ae-4a12-88e4-52cc36509075` |
| 3 | Dio clic | `c58e0322-e13a-41b9-86f8-355dd68baef6` |
| 4 | Votó 1-3 | `2fff69de-96f6-4e57-8d2f-34d6ef43ab40` |
| 5 | Votó 4-5 | `4c3377d0-b933-4909-8f12-6d48b8258add` |
| 6 | Dejó reseña en Google *(WON)* | `cbcf9b9f-86e3-4430-bd5c-36885fb169f9` |
| 7 | Estancada 30 días | `86ea10d5-f527-4894-a451-39c5f81b7ac8` |

### Custom Fields (⚠️ el `key` conserva el slug original aunque renombramos el display)
| Display | dataType | fieldKey (merge / referencia en WF) |
|---|---|---|
| Canal de primer contacto | SINGLE_OPTIONS | `contact.canal_de_primer_contacto` |
| Servicio de interés | TEXT (Single Line) | `contact.servicio_de_interes` |
| Fecha de primer contacto | DATE | `contact.fecha_de_primer_contacto` |
| Estado del lead | SINGLE_OPTIONS | `contact.estado_en_la_conversacin` |
| Tipo de cliente | SINGLE_OPTIONS | `contact.es_primera_vez` |
| Señal pagada | CHECKBOX | `contact.abono_pagado` |
| Fecha de cita | DATE | `contact.fecha_ltima_cita` |
| Servicio realizado | TEXT (Single Line) | `contact.servicio_realizado` |
| UTM Source | TEXT | `contact.utm_source` |
| UTM Medium | TEXT | `contact.utm_medium` |
| UTM Campaign | TEXT | `contact.utm_campaign` |
| Ad / Anuncio | TEXT | `contact.ad__anuncio` |
| Resumen de conversación | LARGE_TEXT | `contact.resumen_de_conversacin` *(extra, conservado)* |

- Opciones **Estado del lead**: Nuevo · En conversación · Pre-reserva · Cita reservada · Cita confirmada
- Opciones **Tipo de cliente**: Nuevo · Recurrente
- Opciones **Canal de primer contacto**: Instagram DM · WhatsApp directo · Facebook · Referido · Organico web

### Custom Values (39) — merge `{{custom_values.KEY}}`
`nombre_negocio` · `nombre_bot` · `nombre_responsable` · `localidad` · `direccion` · `link_maps` · `whatsapp_negocio` · `instagram` · `facebook` · `tiktok` · `web` · `link_agenda` · `moneda` (=€) · `politica_privacidad` · `horario_atencion` · `faq` · `email_negocio` · `link_resena_google` · `pide_senal` (=no) · `monto_senal` · `metodo_pago` · `datos_pago` · `nombre_pago` · `tolerancia` · `cancelacion` · `servicio_1..6` · `precio_1..6` · `info_servicios` · `promo_activa`

### Tags (24)
`lead-nuevo` · `pre-reserva` · `pre-reserva-pendiente-agendar` · `cita-agendada` · `senal-pagada` · `cita-cancelada` · `no-reservo` · `solicitud-asesor-humano` · `canal-whatsapp` · `canal-instagram` · `canal-facebook` · `baja-marketing` · `recordatorio-24h-pendiente` · `wf01-procesado` · `reactivacion-bd` · `dio-clic-review` · `respondio-reactivacion` · `voto-1-3` · `voto-4-5` · `link-directo-google` · `dejo-resena-google` · `estancada-30-dias` · `no-dio-respuesta` · `whatsapp-invalido`

### Calendario
`Studio Bellas - Citas` · `nCLhsHp0skr2IJOTKf6S` — **inactivo**, falta config (slot/duración/disponibilidad/zona Europe/Madrid) y activar en UI.

---

## 🤖 PROMPT DEL BOT (3 partes — pegar en AI Agents → Conversation AI)

### PERSONALIDAD
```
Eres {{custom_values.nombre_bot}}, la asistente virtual de {{custom_values.nombre_negocio}}, en {{custom_values.localidad}}.
Tono: cálido, cercano, profesional y respetuoso. Hablas siempre en español de España, tuteando al cliente de forma natural. Usas emojis con moderación. Te diriges al cliente por su nombre. No mencionas de forma proactiva que eres una IA, pero si el cliente te pregunta directamente si eres un bot, lo confirmas con naturalidad: eres la asistente virtual de {{custom_values.nombre_negocio}}. Nunca afirmas ser una persona real. Nunca presionas ni eres agresiva. Si el cliente dice que necesita pensarlo, lo respetas y le ofreces ayuda adicional.
```

### GOAL (Objetivo)
```
Tu objetivo es atender a cada cliente con empatía, ayudarle a identificar el servicio que mejor se ajusta a lo que busca, y RESERVARLE la cita directamente en el calendario. Si el negocio pide señal, el equipo la valida después para confirmar oficialmente.

ROL Y LÍMITES:
- Tú RESERVAS la cita en el calendario (acción Appointment Booking).
- Tú NO confirmas oficialmente cuando hay señal: la confirmación final la da el equipo tras validar el pago.
- Si recibes un comprobante de pago, NUNCA digas "tu cita está confirmada": agradece, indica que el equipo lo validará, y deriva.

DERIVA a un humano (acción HUMAN HANDOVER) cuando:
- Recibas un comprobante de pago (imagen o PDF)
- El cliente pida hablar con una persona
- El cliente pregunte por contraindicaciones, condiciones médicas o casos clínicos
- El cliente quiera negociar precio o pedir descuento
- Lleves 3+ mensajes sin avanzar

MANEJO DE OBJECIONES (adapta el tono, mantén la idea):
PRECIO / "ES CARO": "Te entiendo perfectamente. El precio refleja la calidad: atención personalizada, materiales profesionales y un resultado seguro y duradero ✨ ¿Quieres que te cuente nuestra promoción vigente?"
MIEDO / DUDA / PRIMERA VEZ: "Es completamente normal tener dudas cuando es algo nuevo 💕 Por eso te acompañamos en todo el proceso. ¿Te gustaría ver resultados o testimonios reales?"
"ME LO TENGO QUE PENSAR": "Por supuesto 😊 ¿Hay alguna duda concreta que te gustaría resolver antes de decidir?"
"YA TE DIGO ALGO": "Sin problema. Solo te comento que las plazas son limitadas; si quieres, puedo dejarte una pre-reserva mientras lo decides ✨"
DISTANCIA: "Muchos clientes vienen desde zonas alejadas porque priorizan la calidad del resultado ✨ ¿Buscamos un día y una hora que te vengan bien?"
```

### ADDITIONAL INFORMATION
```
CONSENTIMIENTO RGPD: La primera vez que pidas datos personales, incluye: "Para gestionar tu cita necesito un par de datos. Al facilitármelos, aceptas nuestra política de privacidad: {{custom_values.politica_privacidad}} 🤍"

FLUJO (consultivo, UNA pregunta por mensaje): 1) Saludo cálido. 2) Necesidad (1 pregunta). 3) Recomendación del servicio. 4) Precio + cierre ofreciendo reservar. Nunca dos preguntas en un mensaje.

CAPTURA DEL SERVICIO: cuando el cliente confirme qué quiere, responde "Perfecto, entonces te interesa [SERVICIO] ✨" y usa la acción CONTACT INFO para guardar ese texto en el campo "Servicio de interés" (contact.servicio_de_interes). El WF-05 lo normaliza luego.

SERVICIOS Y PRECIOS (borra las líneas de servicios no usados):
- {{custom_values.servicio_1}}: {{custom_values.precio_1}}{{custom_values.moneda}}
- {{custom_values.servicio_2}}: {{custom_values.precio_2}}{{custom_values.moneda}}
- {{custom_values.servicio_3}}: {{custom_values.precio_3}}{{custom_values.moneda}}
- {{custom_values.servicio_4}}: {{custom_values.precio_4}}{{custom_values.moneda}}
- {{custom_values.servicio_5}}: {{custom_values.precio_5}}{{custom_values.moneda}}
- {{custom_values.servicio_6}}: {{custom_values.precio_6}}{{custom_values.moneda}}
INFO: {{custom_values.info_servicios}}
PROMO: {{custom_values.promo_activa}}

DATOS DEL NEGOCIO: Instagram {{custom_values.instagram}} · Facebook {{custom_values.facebook}} · TikTok {{custom_values.tiktok}} · Dirección {{custom_values.direccion}}, {{custom_values.localidad}} · WhatsApp {{custom_values.whatsapp_negocio}} · Web {{custom_values.web}} · Mapa {{custom_values.link_maps}} · Horario {{custom_values.horario_atencion}}
FAQ (si no está aquí, deriva): {{custom_values.faq}}
OPT-OUT: si dice "BAJA"/"STOP", confírmalo con amabilidad y no insistas.

RECOGIDA DE DATOS SEGÚN CANAL:
- WhatsApp (tag canal-whatsapp, o sin canal-instagram/canal-facebook): el número YA está → NO lo pidas, solo confirma nombre.
- Instagram/Facebook (tag canal-instagram/canal-facebook): NO hay número → pide nombre completo Y WhatsApp con prefijo (ej. +34 600 123 456) y guárdalo en Phone.

ETAPA 1 — DATOS (uno por mensaje): 1) Nombre y apellidos 2) Teléfono (solo IG/FB) 3) Localidad (opcional) 4) Servicio. Usa CONTACT INFO.
ETAPA 2 — RESERVA: ofrece fecha/hora y RESERVA con APPOINTMENT BOOKING. Confirma: "¡Listo! ✨ Te he reservado para el [fecha] a las [hora]. En un momento recibes la confirmación 💕". La confirmación formal y la señal las envía el sistema (WF-02b). NO recites la señal.
ETAPA 3 — COMPROBANTE (solo si {{custom_values.pide_senal}} = "sí"): "¡Recibido! 💕 Le pasamos tu comprobante al equipo para validar la señal..." NO digas "confirmada". Deriva con Human Handover.

POLÍTICAS (solo si tienen valor): tolerancia {{custom_values.tolerancia}} · reagendar con {{custom_values.cancelacion}}.
LÍMITES: no inventes precios/promos; nunca confirmes cita oficialmente; no des indicaciones médicas → deriva.
FECHAS: "Vie 8 de mayo – 17:00" (sin año, sin zona horaria).
```

### Config del Bot
| Campo | Valor |
|---|---|
| Bot Name | {{custom_values.nombre_bot}} |
| Status | Auto-Pilot |
| Channels | WhatsApp, Instagram DM, Facebook Messenger |
| Respond to Images / Voice | ON / ON |
| Wait Time | 8 s |
| Max messages | 25 |
> ⚠️ Todo WF con Send Message debe terminar en **Update Conversation AI → Status On + Reset message limit** (si no, el bot queda dormido).

---

## 💬 PLANTILLAS WHATSAPP (enviar a Meta — categorías indicadas)

**T01 · Marketing · Bienvenida**
```
Hola {{1}}, te damos la bienvenida a {{custom_values.nombre_negocio}}. Soy {{custom_values.nombre_bot}}, tu asistente. ¿Qué servicio te gustaría consultar?
```
**T02-a · Utility · Confirmación CON señal**
```
Hola, hemos registrado tu cita para el {{1}} a las {{2}} en {{custom_values.nombre_negocio}}. Para asegurar tu plaza, realiza la señal de {{custom_values.monto_senal}}{{custom_values.moneda}} mediante {{custom_values.metodo_pago}}: {{custom_values.datos_pago}}.
📍 {{custom_values.direccion}}  🗺️ {{custom_values.link_maps}}
```
**T02-b · Utility · Confirmación SIN señal** *(por defecto, pide_senal=no)*
```
Hola, hemos registrado tu cita para el {{1}} a las {{2}} en {{custom_values.nombre_negocio}}.
📍 {{custom_values.direccion}}  🗺️ {{custom_values.link_maps}}  Te esperamos.
```
**T03 · Utility · Recordatorio 24h**
```
Hola, te recordamos que mañana tienes tu cita a las {{1}} en {{custom_values.nombre_negocio}}. 📍 {{custom_values.direccion}}
```
**T04 · Marketing · Remarketing 1**
```
Hola {{1}}, queríamos retomar tu consulta sobre nuestros servicios en {{custom_values.nombre_negocio}}. Tenemos disponibilidad esta semana. ¿Te gustaría reservar tu cita?
```
**T05 · Marketing · Remarketing 2**
```
Hola {{1}}, seguimos a tu disposición para ayudarte con el servicio que te interesaba. Si quieres, puedo proponerte algunas fechas disponibles.
```

---

## 🔁 WORKFLOWS — Spec de construcción (referencia los IDs/keys de arriba)

> Crear como **draft**. Marcadas con 🔒 las que dependen de plantillas Meta aprobadas (constrúyelas después de T0x).

### WF-01 · Bienvenida + Activación del Bot
- **Trigger:** 3× Customer Replied (WhatsApp / Instagram / Facebook) · filtro *Doesn't Have Tag* `lead-nuevo`
- **Settings:** Allow re-entry OFF · Allow multiple opportunities OFF
- **Pasos:** Update `contact.canal_de_primer_contacto` (según canal) → IF/Else por canal: Add Tag `canal-whatsapp`/`canal-instagram`/`canal-facebook` → Update `contact.fecha_de_primer_contacto` = Date Created → Update `contact.es_primera_vez` = Nuevo → Update UTM (`utm_source/utm_medium/utm_campaign/ad__anuncio`) → **Crear oportunidad** pipeline Ventas etapa `Nuevo Lead` → Add Tag `lead-nuevo` → Update Conversation AI On+Reset
- *Nota:* ya existe `SB-WF-01` con ~80% de esto (split por canal + opp + conversation_ai). Opción A: ampliarlo. Opción B: rehacer.

### WF-02 · Pre-reserva *(opcional, solo modelo "humano agenda")*
Tag Added `pre-reserva` → Add `pre-reserva-pendiente-agendar` → Remove `lead-nuevo` → mover opp a `Pre-reserva` → Internal Notification → Conversation AI On+Reset

### WF-02b · Cita Reservada 🔒
Trigger Customer Booked Appointment (filtro calendario) → Add `cita-agendada` → Remove `lead-nuevo` → opp `Cita Reservada` → **Send WhatsApp T02-b** (o T02-a si pide_senal=sí) → si señal: Wait + instrucciones de pago → Conversation AI On+Reset

### WF-03 · Recordatorio 24h 🔒
Customer Booked Appointment → Add `recordatorio-24h-pendiente` → Wait Until `contact.fecha_ltima_cita` −1 día → IF `cita-cancelada` End → **Send WhatsApp T03** → Remove `recordatorio-24h-pendiente` → Conversation AI On+Reset

### WF-04 · Remarketing 🔒
Tag Added `lead-nuevo` + *Doesn't Have* `pre-reserva` + *Doesn't Have* `baja-marketing` → Wait 24h → IF `pre-reserva` End → **Send T04** → Conversation AI On+Reset → Wait 24h → IF `pre-reserva` End → **Send T05** → mover opp `No Reservó / No Asistió` + Add `no-reservo`

### WF-05 · Normalización de Servicio de interés
Trigger Contact Changed → `contact.servicio_de_interes` *has changed* · Allow re-entry OFF → **Condition con 1 rama por servicio** (Contains sinónimos) → Update `contact.servicio_de_interes` = `{{custom_values.servicio_N}}`

### WF-06 · Confirmación de Señal *(crear DESACTIVADO; activar solo si pide_senal=sí)*
Tag Added `senal-pagada` → Update `contact.abono_pagado` = Si → opp `Cita Confirmada (señal validada)` → Send WhatsApp confirmación → Conversation AI On+Reset

### WF-07 · Handoff a Humano
Trigger Human Handover (o Tag `solicitud-asesor-humano`) → opp `En conversación humana` → Internal Notification a {{custom_values.nombre_responsable}} → (bot queda en Sleep, NO reactivar)

### WF-08 · Opt-out / Baja
Customer Replied + Contains "BAJA"/"STOP"/"no quiero recibir" → Add `baja-marketing` → Set DND (Marketing) ON → Send WhatsApp confirmación de baja → (opcional) Internal Notification

### WF-09 · Solicitud de Reseña
Opportunity Stage Changed → `Servicio Realizado` → Wait 1 día → Add `reactivacion-bd` (entra al módulo RBD)

### Módulo RBD (RBD 01–09)
Pipeline **Reactivación / Reseñas**. RBD 01 motor (dedup → opp `Mensaje enviado` → drip 4/10 → A/B 50/50 → SMS + link survey → 2 recordatorios). RBD 02 Dio clic → `Dio clic`. RBD 03 Respondió → `Respondió`. RBD 04 Votó 1-3 → `Votó 1-3`. RBD 05 Votó 4-5 → `Votó 4-5`. RBD 06 WhatsApp inválido → `WhatsApp inválido` + DND + sale de flujos. RBD 07 link directo. RBD 08 Dejó reseña → `Dejó reseña en Google` (WON). RBD 09 Estancada 30 días → `Estancada 30 días`. (Detalle completo en el blueprint, secciones 15.3–15.5.)

---

## 📝 FORMS / SURVEY (RBD — crear en UI)
| Pieza | Campos | Lógica |
|---|---|---|
| Form "Registro Cliente" | Nombre · WhatsApp · Correo | entra a RBD 01 |
| Form "Comentarios 1-3" | Nombre · WhatsApp · Correo · Comentarios (`comentarios`) | buzón privado → RBD 04 |
| Survey "Valoración 1-5" | Nombre · WhatsApp · Correo · radio `calificacion_1_5` | 1-3 → Disqualify (no Google) · 4-5 → redirige a {{custom_values.link_resena_google}} → RBD 05 |
> ⚠️ Al clonar RBD de otra cuenta: cambiar emails de notificación a {{custom_values.email_negocio}}, marca/imágenes, Google Place ID, localizar a castellano, y corregir el key del campo survey a `calificacion_1_5`.

---

## 🔁 WORKFLOWS DE VENTAS — construidos (drafts) y qué falta a mano

Todos creados en la carpeta **"WF Ventas (blueprint)"**. Regla aplicada: **los envíos de WhatsApp son nodos con el nombre de su plantilla** (tipo placeholder `add_notes`, NO envían) — reemplazá cada uno por la acción **WhatsApp** real y elegí la plantilla cuando tengas suscripción/aprobación Meta.

| WF | Trigger | Pasos hechos | Te toca a mano |
|---|---|---|---|
| WF-01 · Bienvenida + Activación | ✅ Customer Replied ×3 canal + branch | ✅ 18 pasos (reusado, intacto) | Revisar; opcional añadir tags `canal-*`, Tipo cliente, UTM |
| WF-02 · Pre-reserva | ✅ Tag `pre-reserva` | ✅ 5 | — (opcional, solo modelo "humano agenda") |
| WF-02b · Cita Reservada | ⚠️ **poner trigger** Customer Booked Appointment | ✅ 5 (incl. nodo WhatsApp T02-b) | Trigger + acción WhatsApp |
| WF-03 · Recordatorio 24h | ⚠️ **poner trigger** Booked Appointment | ✅ 5 | Trigger + cambiar Wait por **Wait Until** (Fecha de cita −1d) + WhatsApp T03 |
| WF-04 · Remarketing | ✅ Tag `lead-nuevo` | ✅ 7 (T04+T05) | Filtros *Doesn't Have* `pre-reserva`/`baja-marketing` + IF pre-reserva→End + WhatsApp |
| WF-05 · Normalización servicio | ✅ Contact Changed (reusado SB-WF-03) | ✅ existente | Revisar ramas por servicio |
| WF-06 · Confirmación Señal | ✅ Tag `senal-pagada` | ✅ 3 | Dejar **OFF** salvo `pide_senal=sí` + WhatsApp |
| WF-07 · Handoff a Humano | ✅ Tag `solicitud-asesor-humano` | ✅ 2 | — |
| WF-08 · Opt-out / Baja | ⚠️ **poner trigger** Customer Replied + "BAJA/STOP" | ✅ 3 | Trigger + WhatsApp confirmación |
| WF-09 · Solicitud de Reseña | ⚠️ **poner trigger** Opp Stage → "Servicio Realizado" | ✅ 2 (enrola con `campana de reactivación` → RBD 01) | Trigger |

> Todos quedan en **draft**: revisá, completá los triggers/WhatsApp marcados, y **publicá** uno a uno.
>
> **Nodos de oportunidad:** se usa la acción **"Create or update opportunity"** (`create_opportunity`) en todos — pipeline **Ventas** + la etapa correspondiente. Es la verificada y da menos fallos. *(GHL muestra un aviso de deprecación a favor de "Create Opportunity"/"Update Opportunity" por separado; si en el futuro querés migrar, es un swap en UI.)*

## 🔎 REVISIÓN DEL MÓDULO RBD (lo instaló tu snapshot — published)

Lo que está bien: usa **SMS** (no depende de Meta), 9 workflows + 2 forms + survey + pipeline ya conectados. **WF-09 ya lo alimenta** (tag `campana de reactivación`).

⚠️ **Adaptar a mano (blueprint §15.5 — viene clonado de otra cuenta):**
- 🔴 **Emails de notificación de los 2 forms** → cambiá a `{{custom_values.email_negocio}}`. La API devuelve 401 en la config de forms, así que **revisá en UI** (Sites → Forms → Settings/Notifications) que no apunten a correos de terceros (Agencia GarLey / La Guadalupana). *Riesgo de fuga de datos.*
- 🔴 **Google Place ID / enlace de reseña** → poné el del cliente en la survey y en `{{custom_values.link_resena_google}}`.
- 🔴 **Marca/imágenes** de forms y survey → reemplazar por las del cliente.
- 🟠 **RBD 07** tiene la **rama duplicada** (pasos 1-4 y 5-8 idénticos) → borrá una en UI.
- 🟠 **SMS en español latino** → adaptar a castellano de España.
- 🟡 **Tags duplicados**: el snapshot usa `campana de reactivación`, `voto 1-3`, `votó 4-5`, `dejó reseña en google`, `dio clic trigger link google review`, `respondió a campana reactivacion bd`, `link directo google`, `no dio respuesta`, `google_review`, `test a/b`. Conviven con mis kebab-case (`reactivacion-bd`, `voto-1-3`…). El módulo **funciona con los suyos**; estandarizar a kebab-case implicaría editar los 9 workflows publicados (hazlo solo si querés limpieza total).
- 🟡 **Campo survey** `Califícanos del 1 al 5` (RADIO) → el blueprint pide key `calificacion_1_5`; verificá que RBD 02/05 lo lean bien.

## ✅ CHECKLIST PARA TERMINAR EL 100%
- [ ] Rellenar Custom Values del cliente (negocio, servicios, precios, política, FAQ…)
- [ ] Decidir `pide_senal` por cliente (hoy = "no"); si "sí": rellenar señal + activar WF-06 + usar T02-a
- [ ] Configurar y **activar** el calendario (Europe/Madrid, duración, disponibilidad)
- [ ] Enviar T01–T05 a Meta (12–48h de aprobación → hacerlo primero)
- [ ] Construir WF-01…09 (specs arriba) — empezar por WF-01/05/07/08 (no dependen de plantillas)
- [ ] Construir módulo RBD (forms + survey + RBD 01–09)
- [ ] Pegar las 3 partes del prompt del bot + conectar acciones (Contact Info, Human Handover, Appointment Booking → calendario)
- [ ] Añadir filtro *Doesn't Have Tag* `baja-marketing` a workflows de Marketing
- [ ] Prueba end-to-end: lead → bot reserva → confirmación → (señal) → validación → reseña

---

## 🔁 AUTOMATIZACIÓN "Actualizacion de CV" (form → custom values) — construida 2026-06-24

WF `188c2d5e-44a3-479c-a109-7534cb6f50f7` (loc `c8FNGEjTOUL3VfR43w7e`). Trigger **Form Submitted** → form **"Onboarding y CV"** (`IYiB5VuHfT8dDTM1uYot`). **41 nodos** `update_custom_value`: cada campo de contacto del alta vuelca a su Custom Value de cuenta. Incluye 2 CV nuevos: `logo_vertical` (`kUNEIeHXwRLJzmYVakYb`) y `logo_horizontal` (`brD9RWy7QlwatNyf0XqJ`).

### ⚠️ Estructura VERIFICADA del action `update_custom_value` (memorizar)
La UI de GHL lee `custom_value_id` + `new_value`. Un nodo con SOLO `fields` **se guarda pero sale en blanco + ⚠️**. Hacen falta las 4 claves:
```json
{
  "type": "update_custom_value",
  "name": "CV · <nombre>",
  "attributes": {
    "type": "update_custom_value",
    "fields": [{ "field": "<cvId>", "value": "{{contact.<campo>}}" }],
    "custom_value_id": "<cvId>",
    "new_value": "{{contact.<campo>}}",
    "current_value": "<valor actual del CV>"
  }
}
```
Builder listo: `workflow_builder.custom_value_step(cv_id, cv_name, value, current_value)`.

> Nota merge tags: los campos del form de alta tienen key con doble "contact" (`contact.contactlocalidad`) → el tag correcto es `{{contact.contactlocalidad}}`. Los 2 logos tienen key limpia (`contact.logo_vertical_9_16`, `contact.logos_horizontal_16_9`).

> Nota entorno: el shell exporta `GHL_LOCATION_ID=30fL2DR9K58StO46WN4Y` (OTRA subcuenta). El `.env` apunta a `c8FN…` (snapshot). Cargar el `.env` con **override**, no `setdefault`, o se trabaja en la cuenta equivocada.
