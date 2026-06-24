# Formulario de alta (onboarding) — para construir en GoHighLevel

> El cliente rellena este formulario; sus respuestas se usan para completar los **Custom Values** del snapshot.
> Tipos en nomenclatura GHL: **Text Box** (Single Line) · **Text Area** (Multi Line) · **Single Options** (Dropdown) · **Radio** · **Number** · **Phone** · **Email**.
> La columna **→ Custom Value** indica a qué `{{custom_values.x}}` va cada respuesta.

---

## 0 · Datos de contacto (estándar GHL — crean/identifican el contacto)
| Etiqueta | Tipo GHL | Obligatorio |
|---|---|---|
| Nombre | First Name | ✅ |
| Apellidos | Last Name | — |
| Email de contacto | Email | ✅ |
| Teléfono de contacto | Phone | ✅ |

---

## 1 · Datos del negocio
| Etiqueta (pregunta) | Tipo GHL | → Custom Value | Oblig. | Notas |
|---|---|---|---|---|
| Nombre del negocio | Text Box | `nombre_negocio` | ✅ | |
| Nombre del asistente virtual (bot) | Text Box | `nombre_bot` | — | Ej.: Sofía |
| Persona responsable / a quién derivar | Text Box | `nombre_responsable` | — | Ej.: Dra. Martín |
| Localidad / ciudad | Text Box | `localidad` | ✅ | |
| Dirección completa | Text Box | `direccion` | ✅ | |
| Enlace de Google Maps | Text Box | `link_maps` | — | URL |
| WhatsApp del negocio | Phone | `whatsapp_negocio` | ✅ | Con prefijo (+34…) |
| Instagram | Text Box | `instagram` | — | Usuario o URL |
| Facebook | Text Box | `facebook` | — | Dejar vacío si no aplica |
| TikTok | Text Box | `tiktok` | — | Dejar vacío si no aplica |
| Web | Text Box | `web` | — | URL |
| Enlace del calendario / agenda | Text Box | `link_agenda` | — | URL del calendario (si lo tiene) |
| Horario de atención | Text Box | `horario_atencion` | ✅ | Ej.: L-V 9:00–20:00, S 10:00–14:00 |
| Email del negocio (notificaciones) | Email | `email_negocio` | ✅ | |
| Enlace de política de privacidad (RGPD) | Text Box | `politica_privacidad` | — | URL |
| Enlace para dejar reseña en Google | Text Box | `link_resena_google` | — | URL directa a reseña |
| Preguntas frecuentes | Text Area | `faq` | — | "P: ¿Hay parking? R: …" |
| Moneda | Single Options | `moneda` | — | Opciones: `€` (def.) · `$` · `£` |

---

## 2 · Servicios y precios
> Rellenar **solo los servicios que ofrece** (los vacíos se ignoran).

| Etiqueta | Tipo GHL | → Custom Value | Notas |
|---|---|---|---|
| Servicio 1 | Text Box | `servicio_1` | |
| Precio servicio 1 | Number | `precio_1` | Solo el número |
| Servicio 2 | Text Box | `servicio_2` | |
| Precio servicio 2 | Number | `precio_2` | |
| Servicio 3 | Text Box | `servicio_3` | |
| Precio servicio 3 | Number | `precio_3` | |
| Servicio 4 | Text Box | `servicio_4` | |
| Precio servicio 4 | Number | `precio_4` | |
| Servicio 5 | Text Box | `servicio_5` | |
| Precio servicio 5 | Number | `precio_5` | |
| Servicio 6 | Text Box | `servicio_6` | |
| Precio servicio 6 | Number | `precio_6` | |
| Info adicional de servicios | Text Area | `info_servicios` | Duración, sesiones, garantías… |
| Promoción vigente | Text Area | `promo_activa` | Opcional |

---

## 3 · Señal / depósito
| Etiqueta | Tipo GHL | → Custom Value | Oblig. | Notas |
|---|---|---|---|---|
| ¿Pides señal/depósito para reservar? | Radio / Single Options | `pide_senal` | ✅ | Opciones: `sí` · `no` |
| Importe de la señal | Number | `monto_senal` | — | Solo si "sí". Solo el número |
| Método de pago | Text Box | `metodo_pago` | — | Bizum / transferencia |
| Datos para el pago | Text Box | `datos_pago` | — | Bizum al 600… / IBAN ES… |
| Titular de la cuenta | Text Box | `nombre_pago` | — | |

> **Lógica condicional (opcional):** mostrar los 4 campos de pago solo si `pide_senal` = **sí** (con la condición de visibilidad de GHL).

---

## 4 · Políticas (opcional)
| Etiqueta | Tipo GHL | → Custom Value | Notas |
|---|---|---|---|
| Tolerancia de llegada | Text Box | `tolerancia` | Ej.: 10 minutos |
| Antelación para cancelar / reagendar | Text Box | `cancelacion` | Ej.: 24 horas |

---

## Notas de construcción
- **Total:** 4 campos de contacto + **39 campos** que mapean 1:1 a los Custom Values del snapshot.
- Tras recibir la respuesta, esos valores se **vuelcan a Settings → Custom Values** (a mano, o por n8n con `Update Custom Value` vía API).
- Sugerencia: usa **Text Area** para `faq`, `info_servicios` y `promo_activa`; el resto Text Box salvo los precios (**Number**), WhatsApp (**Phone**), emails (**Email**) y los desplegables (`moneda`, `pide_senal`).
- Si construyes los campos como **Custom Fields de contacto**, nómbralos igual que el Custom Value destino para que el volcado sea directo.
