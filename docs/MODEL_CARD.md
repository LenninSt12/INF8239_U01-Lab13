# Model Card — complete after LAB13

## Intended use
El modelo opera como un Sistema de Soporte a Decisiones (DSS) para priorizar casos sintéticos en auditorías y revisiones de control interno. Su función es clasificar casos sospechosos o con anomalías para que sean inspeccionados por analistas humanos, asistiendo pero nunca reemplazando el juicio profesional.

## Out-of-scope use
- Intervenciones directas o sanciones disciplinarias automatizadas.
- Decisiones automáticas de elegibilidad crediticia, contractual o laboral sin mediación humana.
- Declaraciones de emergencia o activación autónoma de protocolos de contingencia crítica.
- Uso del modelo sobre variables de identidad directa o sin previo consentimiento informado.

## Data and split
- **Dataset:** Muestra sintética territorial y operacional de 640 registros y 9 variables.
- **Distribución de clases:** 55.2% clase positiva (1) y 44.8% clase negativa (0).
- **Grupos protegidos:** G1 (396 observaciones) y G2 (244 observaciones).
- **Corte temporal estricto:** 
  - Entrenamiento finalizado el `2026-09-24 00:00:00`.
  - Prueba / Evaluación a partir del `2026-09-25 00:00:00`.
- **Variables excluidas del modelado:** `case_id`, `received_date`, `protected_group`, `target`.

## Global and subgroup evaluation
Evaluación sobre conjunto de prueba auditada con Fairlearn:
- **Baseline (Regresión Logística):**
  - **Global:** Recall global superior a 0.68, cumpliendo el umbral mínimo del governance.
  - **Subgrupo G1 (n=101):** Accuracy = 0.703, Selection Rate = 0.446, Recall = 0.653, Precision = 0.711, FPR = 0.250.
  - **Subgrupo G2 (n=59):** Accuracy = 0.746, Selection Rate = 0.678, Recall = 0.791, Precision = 0.850, FPR = 0.375.
  - **Disparidades:** Recall gap de 0.138 y FPR gap de 0.125, manteniéndose por debajo de la compuerta máxima permitida (0.16).
- **Modelo Alternativo (Árbol de Decisión):** Mayor disparidad en FPR (0.169), lo cual justifica el descarte frente a la regresión logística.

## Green AI evidence
- **Tiempo de entrenamiento:** 0.297 segundos.
- **Tamaño del artefacto serializado:** 3.56 KB (ampliamente inferior al límite estricto de 1024 KB).
- **Latencia promedio:** Inferior a 50 ms por lote (límite: 500 ms).
- **Huella de cómputo:** Mínima huella de carbono, ejecutable en entornos locales estándar sin GPU.

## Limitations, human oversight and appeal
- **Limitaciones:** El modelo muestra una ligera sobreestimación en el subgrupo G2. Requiere calibración periódica de umbrales para mitigar sesgos de selección.
- **Supervisión Humana (*Human Oversight*):** Todas las alertas emitidas son recomendaciones (*REVIEW*). Ningún caso se cierra sin la firma o aprobación del analista de riesgos.
- **Mecanismo de apelación:** Las unidades operacionales auditadas pueden solicitar una segunda revisión manual no asistida en caso de discrepancias en la calificación.

## Owner and review date
- **Owner:** Institutional Owner / Propietario Institucional de Riesgo Operacional.
- **Review Date:** 2026-10-31 (Ciclo de auditoría trimestral).