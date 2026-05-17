# Revisión preliminar de seguridad - TechNova

## Contexto

Se realizó una revisión preliminar del módulo Clientes de la aplicación TechNova, utilizando una versión inicial vulnerable del archivo `clientes/views.py`.

## Hallazgos preliminares

| Código | Hallazgo | Descripción | Riesgo | Herramienta / evidencia |
|---|---|---|---|---|
| H-01 | Consulta SQL por concatenación | El parámetro `dni` se concatena directamente dentro de una consulta SQL. | Crítico | Código vulnerable / Bandit |
| H-02 | Falta de validación de entradas | El valor recibido por GET no valida tipo, longitud ni formato. | Alto | Código vulnerable |
| H-03 | Registro mediante GET | El registro de clientes recibe datos por URL. | Alto | Código vulnerable |
| H-04 | Reporte sin autenticación | El reporte de clientes puede ser consultado sin login. | Alto | Código vulnerable |
| H-05 | Construcción manual de HTML | La salida se construye concatenando cadenas. | Medio | Código vulnerable / Pylint |
| H-06 | Dependencias por revisar | Se revisan paquetes instalados mediante pip-audit. | Medio/Alto | pip-audit |

## Conclusión preliminar

La revisión inicial evidencia debilidades críticas en el módulo Clientes, principalmente por el uso de consultas SQL construidas mediante concatenación de parámetros, ausencia de validación de entradas y falta de control de acceso en rutas sensibles. Estos hallazgos justifican la aplicación de técnicas de codificación segura en una segunda fase.
