# Matriz de Riesgos - TechNova

| Código | Vulnerabilidad | Probabilidad | Impacto | Nivel de riesgo | Evidencia | Mitigación aplicada |
|---|---|---|---|---|---|---|
| R-01 | Inyección SQL por concatenación de parámetros | Alta | Alto | Crítico | views vulnerable | Uso del ORM de Django y validación estricta del DNI |
| R-02 | Falta de validación de entradas | Alta | Alto | Crítico | Parámetro dni sin validación | Validación de tipo, longitud y formato |
| R-03 | Registro mediante método GET | Media | Alto | Alto | registrar_cliente vulnerable | Cambio a método POST y autenticación requerida |
| R-04 | Reporte sin control de acceso | Media | Alto | Alto | reporte_clientes público | Uso de login_required |
| R-05 | Exposición de errores técnicos | Media | Medio | Medio | Manejo directo de excepción | Uso de logging interno y mensaje genérico |
| R-06 | Dependencias vulnerables | Media | Alto | Alto | pip-audit | Auditoría con pip-audit y actualización controlada |
