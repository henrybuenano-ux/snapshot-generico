# CONTRATO DE PRESTACIÓN DE SERVICIOS — Sistema Ads + CRM (omnia)

> **PLANTILLA GENÉRICA.** Rellenar los campos `{{…}}` por cliente (merge fields de GHL).
> **Aviso legal:** este documento es una plantilla orientativa y **no constituye asesoramiento jurídico**. Debe ser revisado y validado por asesoría legal antes de su uso. Adaptar a la legislación vigente (España / UE).

---

## Campos a rellenar (custom fields / custom values)
| Merge field | Significado |
|---|---|
| `{{custom_values.omnia_razon_social}}` · `{{custom_values.omnia_cif}}` · `{{custom_values.omnia_domicilio}}` · `{{custom_values.omnia_email}}` | Datos del prestador (omnia) |
| `{{contact.company_name}}` | Razón social del cliente |
| `{{contact.full_name}}` · `{{contact.email}}` · `{{contact.phone}}` | Representante y contacto del cliente |
| `{{custom_values.cliente_cif}}` · `{{custom_values.cliente_domicilio}}` | NIF/CIF y domicilio fiscal del cliente |
| `{{custom_values.plan_contratado}}` | Captación · Z / Crecimiento · S / Pro · P / Escala · T |
| `{{custom_values.canales_ads}}` | Google y/o Meta |
| `{{custom_values.cuota_activacion}}` | Activación única (ej. 290 €) |
| `{{custom_values.cuota_mensual}}` | Mensualidad (ej. 447 €) |
| `{{custom_values.desglose_mensual}}` | Ej.: 197 € sistema + 250 € gestión de ads |
| `{{custom_values.permanencia}}` · `{{custom_values.preaviso_baja}}` | Permanencia mínima y preaviso de baja |
| `{{custom_values.fecha_contrato}}` | Fecha de firma |

---

En `{{custom_values.omnia_domicilio}}`, a `{{custom_values.fecha_contrato}}`.

**REUNIDOS**

De una parte, **{{custom_values.omnia_razon_social}}** (en adelante, «**omnia**» o «el Prestador»), con CIF `{{custom_values.omnia_cif}}` y domicilio en `{{custom_values.omnia_domicilio}}`.

De otra parte, **{{contact.company_name}}** (en adelante, «el Cliente»), con NIF/CIF `{{custom_values.cliente_cif}}` y domicilio en `{{custom_values.cliente_domicilio}}`, representada por `{{contact.full_name}}`.

Ambas partes se reconocen capacidad legal suficiente para contratar y **ACUERDAN**:

---

## 1. Objeto
omnia prestará al Cliente el servicio **«Sistema Ads + CRM para Clínicas»**: la instalación y puesta en marcha de un sistema CRM preconfigurado (en adelante, el «Sistema») sobre la plataforma GoHighLevel, junto con la **gestión de campañas publicitarias** (Google/Meta) según el plan **`{{custom_values.plan_contratado}}`**.

## 2. Alcance del servicio (CAPACIDADES — QUÉ INCLUYE)

> El **Sistema CRM es idéntico en los cuatro planes** (Z / S / P / T). Lo único que varía entre planes es el **alcance de la gestión de publicidad** (cláusula 2.3).

**2.1. Sistema CRM «omnia para Clínicas» (instalación templatizada sobre GoHighLevel).** Se entrega tal y como está configurado en el snapshot estándar de omnia, e incluye:

- **Asistente virtual con IA** (1 asistente, en castellano): atención automatizada por chat, respuesta a preguntas frecuentes, cualificación de leads, **reserva de citas** y derivación a persona humana (*handoff*).
- **Embudo de ventas:** **1 pipeline de ventas** estándar con sus etapas (lead → contacto → cita → asistencia → ganado / perdido).
- **Automatizaciones estándar (workflows del snapshot):** bienvenida y activación del bot, pre-reserva, **recordatorio de cita (24 h)**, remarketing a leads sin reservar, normalización del servicio de interés, confirmación de señal/depósito (si aplica), *handoff* a humano, baja/opt-out y solicitud de reseña.
- **Módulo de reputación y reseñas de Google:** reactivación de base de datos, captación de reseñas de 5★, redirección a Google y gestión de valoraciones.
- **Formulario de alta (onboarding)** con **volcado automático** de los datos del negocio a la configuración del Sistema.
- **Calendario de citas:** **1 calendario** (zona horaria, duración y disponibilidad).
- **Catálogo de servicios:** hasta **6 servicios** con su precio.
- **Plantillas de mensajería estándar** (WhatsApp / email / SMS) del snapshot.
- **Personalización del snapshot** a partir del formulario de alta: logotipo (vertical y horizontal), colores, datos del negocio, catálogo de servicios y precios, horarios, FAQ, política de privacidad y textos.

> El Sistema entregado es el **snapshot estándar de omnia (producto MVP)**. La personalización se limita a **marca, datos y textos**; **no incluye** desarrollos, lógica, integraciones ni automatizaciones a medida fuera del snapshot (cláusula 3).

**2.2. Gestión de publicidad (`{{custom_values.canales_ads}}`):** configuración, puesta en marcha y optimización de las campañas, dentro de los límites del plan **`{{custom_values.plan_contratado}}`**.

**2.3. Alcance de publicidad por plan** (lo único que cambia entre planes):

| Plan | Gestión de ads incluida |
|---|---|
| **Captación · Z** | 1 canal (Google **o** Meta) |
| **Crecimiento · S** | 2 canales (Google **y** Meta) + analítica |
| **Pro · P** | Gestión avanzada + redistribución de presupuesto |
| **Escala · T** | Multi-sede / multi-campaña + reporting a medida |

**2.4. Soporte** de mantenimiento del Sistema en horario laboral (L-V).

## 3. Límites y exclusiones (QUÉ NO INCLUYE)

**3.1. Naturaleza del producto.** El Sistema es un **producto estándar (MVP)**: se entrega **tal cual**, con **ajustes limitados** (marca, datos, textos y catálogo). No se modifican los workflows, las etapas del pipeline ni la lógica del asistente más allá de la configuración estándar.

**3.2. Límites cuantitativos del Sistema** (ampliar cualquiera de ellos se rige por la cláusula 9):

| Elemento | Incluido en el estándar |
|---|---|
| Asistente virtual (IA) | 1, en castellano |
| Pipeline de ventas | 1 (estándar) |
| Calendario de citas | 1 |
| Catálogo de servicios | hasta 6 |
| Workflows / plantillas | los del snapshot estándar |
| Idiomas | 1 (castellano) |

**3.3.** Salvo pacto expreso por escrito, **NO** están incluidos:
- a) Desarrollos, automatizaciones (workflows) o funcionalidades **adicionales** a las del snapshot estándar.
- b) Integraciones con sistemas de terceros no contempladas en el Sistema.
- c) Diseño/desarrollo de páginas web, landing pages o funnels fuera de lo incluido en el plan.
- d) Creatividades, fotografía o **vídeos** para anuncios (servicio aparte).
- e) La **inversión publicitaria** (presupuesto que se paga a Google/Meta).
- f) Los **costes de comunicación y de terceros** (ver cláusula 5).
- g) Migraciones de datos, formaciones adicionales o consultoría fuera de alcance.
- h) Soporte fuera de horario, SLA premium o gestión de incidencias imputables a plataformas de terceros.
- i) Garantía de resultados comerciales concretos (nº de leads, citas o ventas).

**Cualquier requerimiento no listado en la cláusula 2 se considera fuera de alcance** y se regirá por la cláusula 9.

## 4. Precio y forma de pago
- **Activación (pago único):** `{{custom_values.cuota_activacion}}` + IVA, abonada al inicio para la puesta en marcha.
- **Cuota mensual:** `{{custom_values.cuota_mensual}}` + IVA (`{{custom_values.desglose_mensual}}`).
- **Primer mes:** activación + primera mensualidad. **A partir del segundo mes:** solo la mensualidad.
- Los precios se entienden **sin IVA**, que se repercutirá según normativa.
- El impago de cualquier cuota faculta a omnia a **suspender** el servicio hasta su regularización (cláusula 10).

## 5. Costes de terceros (operativos) — a cargo del Cliente
Los siguientes consumos se pagan **directamente a los proveedores** según el uso real y **no los factura omnia**; el Cliente mantiene la titularidad de dichas cuentas:
- **Licencia de Meta (WhatsApp Business):** cuota mensual fija del proveedor.
- **Conversaciones de WhatsApp** (plantillas por conversación iniciada).
- **Tokens de IA** del asistente: por volumen o plan ilimitado.
- **Envío de correos/SMS** y, en su caso, telefonía.
- La **inversión publicitaria** en Google/Meta.

omnia facilitará estimaciones orientativas, sin que constituyan importe garantizado.

## 6. Obligaciones del Cliente
- Aportar de forma veraz y en plazo los **datos y accesos** necesarios (formulario de alta, cuentas de WhatsApp/Meta/Google, dominios, etc.).
- Revisar y **aprobar** los contenidos y la configuración.
- Cumplir las **políticas** de Meta, Google y WhatsApp, así como la normativa aplicable.
- Realizar los pagos en los plazos pactados.

## 7. Obligaciones de omnia
- Instalar y poner en marcha el Sistema según la cláusula 2.
- Gestionar la publicidad dentro de los límites del plan.
- Prestar el soporte de mantenimiento acordado.

## 8. Duración, renovación y baja
- **Duración:** indefinida, con **permanencia mínima** de `{{custom_values.permanencia}}` desde la activación.
- **Renovación:** mensual automática salvo baja.
- **Baja:** cualquiera de las partes podrá resolver con un **preaviso** de `{{custom_values.preaviso_baja}}`. La activación no es reembolsable.

## 9. Modificaciones del alcance, nuevos trabajos y upsells
Toda solicitud de servicios, funcionalidades o cambios **no incluidos** en la cláusula 2 (ver exclusiones de la cláusula 3):
- a) Se **cotizará por separado** mediante presupuesto escrito (nuevo alcance) o se ofrecerá como **upsell**.
- b) **No se iniciará** ni se entenderá incluida hasta su **aceptación expresa por escrito** y, en su caso, pago.
- c) Podrá facturarse como pago único, como ampliación de la cuota mensual o como nuevo producto, según corresponda.

Ningún trabajo fuera de alcance se considera comprometido por el mero hecho de solicitarse.

## 10. Suspensión y resolución
omnia podrá **suspender o resolver** el contrato en caso de impago, uso indebido del Sistema, incumplimiento de las políticas de terceros o de las obligaciones del Cliente. La resolución no exime de los importes devengados.

## 11. Propiedad intelectual
- El **Sistema, el snapshot, las automatizaciones, las plantillas y la metodología** son propiedad de omnia; el Cliente recibe un **derecho de uso** mientras esté vigente el contrato y al corriente de pago.
- Los **datos, contactos, cuentas y contenidos** del Cliente son de su titularidad.
- A la finalización, cesa el derecho de uso del Sistema; el Cliente conserva sus datos y cuentas de terceros.

## 12. Protección de datos (RGPD)
- El Cliente es **Responsable del tratamiento** y omnia, **Encargado del tratamiento**, conforme al RGPD (UE 2016/679) y la LOPDGDD. Se suscribirá el correspondiente **contrato de encargo** (anexo).
- omnia tratará los datos solo para prestar el servicio y guardará **confidencialidad**.

## 13. Garantías y limitación de responsabilidad
- omnia presta el servicio con diligencia profesional, **sin garantizar resultados comerciales concretos** (leads, citas o ventas), por depender de factores ajenos (mercado, inversión, plataformas de terceros).
- omnia **no responde** de fallos, cambios de política, costes o suspensiones de plataformas de terceros (Meta, Google, GoHighLevel).
- La responsabilidad de omnia se limita, como máximo, al importe de las **cuotas del último mes** facturadas.

## 14. Confidencialidad
Ambas partes mantendrán confidencial la información a la que accedan con motivo del contrato.

## 15. Legislación y jurisdicción
El contrato se rige por la **legislación española**. Para cualquier controversia, las partes se someten a los **Juzgados y Tribunales** del domicilio de omnia, salvo norma imperativa en contrario.

---

**Y en prueba de conformidad, ambas partes firman el presente contrato.**

| Por omnia | Por el Cliente |
|---|---|
| {{custom_values.omnia_razon_social}} | {{contact.company_name}} |
| Firma: _______________ | Firma: _______________ |
| Fecha: {{custom_values.fecha_contrato}} | Fecha: {{custom_values.fecha_contrato}} |
