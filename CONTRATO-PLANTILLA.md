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

## 2. Alcance del servicio (QUÉ INCLUYE)
**2.1. Sistema CRM (instalación templatizada):**
- Asistente virtual con IA (chatbot) preconfigurado para atención y reserva de citas.
- Pipeline de ventas con sus etapas.
- Conjunto **estándar** de automatizaciones (workflows) del snapshot.
- Módulo de reputación / reseñas de Google.
- Calendario de citas y plantillas de mensajería estándar.
- **Personalización limitada** del snapshot: logotipo, colores, datos del negocio, catálogo de servicios/precios y textos, a partir de los datos aportados por el Cliente en el formulario de alta. *No incluye desarrollos ni lógica a medida fuera del snapshot estándar.*

**2.2. Gestión de publicidad (`{{custom_values.canales_ads}}`)** según el plan contratado: configuración, puesta en marcha y optimización de las campañas, en los límites del plan `{{custom_values.plan_contratado}}`.

**2.3. Soporte** de mantenimiento del Sistema en horario laboral.

## 3. Límites y exclusiones (QUÉ NO INCLUYE)
Salvo pacto expreso por escrito, **NO** están incluidos en este contrato:
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
