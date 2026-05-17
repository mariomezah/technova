# OWASP Dependency-Check - Revisión final TechNova

Se ejecutó OWASP Dependency-Check sobre las dependencias del proyecto TechNova, utilizando la carpeta persistente de datos ubicada en `/opt/dependency-check-data`.

## Resultado de ejecución

El análisis finalizó correctamente y generó los reportes:

- `dependency-check-report.html`
- `dependency-check-report.json`

## Resultado de seguridad

No se identificaron vulnerabilidades CVE confirmadas en las dependencias analizadas.

## Observación técnica

Durante la ejecución se mostró una advertencia indicando que el analizador Sonatype OSS Index estaba deshabilitado por falta de credenciales. Esta advertencia no impidió la ejecución del análisis, ya que Dependency-Check completó la revisión usando las fuentes disponibles, incluyendo NVD CVE Analyzer, RetireJS Analyzer y Known Exploited Vulnerability Analyzer.

## Estado

Verificado sin hallazgos críticos.
