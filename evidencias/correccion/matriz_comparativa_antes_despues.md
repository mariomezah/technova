# Matriz comparativa antes/después - TechNova

| Código | Hallazgo preliminar | Evidencia preliminar | Corrección aplicada | Evidencia posterior | Estado |
|---|---|---|---|---|---|
| H-01 | Consulta SQL por concatenación | views_vulnerable.py / SonarQube / Bandit | Uso de ORM de Django | views_corregido.py / prueba de búsqueda segura | Mitigado |
| H-02 | Falta de validación del parámetro DNI | views_vulnerable.py | Validación con expresión regular y longitud permitida | evidencia_bloqueo_inyeccion_sql.html | Mitigado |
| H-03 | Registro mediante método GET | urls_vulnerable.py / views_vulnerable.py | Uso de método POST | views_corregido.py | Mitigado |
| H-04 | Reporte sin autenticación | views_vulnerable.py | Uso de login_required | views_corregido.py | Mitigado |
| H-05 | Manejo débil de errores | views_vulnerable.py | Uso de logging y mensajes genéricos | views_corregido.py | Mitigado |
| H-06 | Dependencias por evaluar | pip-audit / Dependency-Check preliminar | Revisión posterior de dependencias | pip-audit corregido / Dependency-Check corregido | En revisión según reporte |
| H-07 | Calidad de código mejorable | Pylint preliminar | Ajustes de estructura y validación | Pylint corregido | Mejorado / sujeto a observaciones |
| H-08 | Revisión de repositorio pendiente | GitHub Advanced Security | Activación de Dependabot, Code scanning y Secret Protection | Capturas GitHub Security | Revisado |
