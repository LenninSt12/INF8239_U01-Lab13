# Incident Runbook — complete after LAB13

1. Detection and classification:
   - **Detección:** El sistema monitorea continuamente las compuertas de gobernanza (`min_recall >= 0.68`, `max_recall_gap <= 0.16`, `max_fpr_gap <= 0.16`, latencia < 500 ms).
   - **Clasificación:**
     - *Incidente Menor:* Incremento transitorio de latencia o alerta preventiva de deriva en datos de entrada.
     - *Incidente Crítico:* Ruptura de compuertas de equidad (recall_gap > 0.16 o FPR_gap > 0.16), degradación de recall < 0.68, o identificación de datos personales/prohibidos en inferencia.

2. Containment authority:
   - **Autoridad:** El **Institutional Owner** y el **Especialista de Riesgos** cuentan con autoridad ejecutiva delegada para detener el servicio predictivo de inmediato sin previa consulta si se violan las compuertas críticas.

3. Evidence preservation:
   - Congelar y aislar los logs del DSS, los archivos de entrada asociados al incidente, la matriz de confusión del lote observado, y el archivo `reports/lab13/deployment_decision.json` con su checksum SHA-256. Prohibido reiniciar los contenedores o limpiar la memoria antes del volcado forense.

4. Internal and affected-party communication:
   - **Interno:** Notificación automática en menos de 1 hora al equipo técnico (Data Scientist, ML Engineer) y al Comité de Riesgos/Legal vía canales dedicados de emergencia.
   - **Afectados:** Comunicación formal a las unidades auditadas si las decisiones del DSS generaron revisiones desproporcionadas durante el intervalo del incidente.

5. Rollback or safe baseline:
   - Si el sistema emite una decisión `STOP` o se activa contención:
     1. Desconectar el servicio del modelo en producción.
     2. Retorno inmediato al **Baseline Seguro** (reglas heurísticas deterministas / muestreo manual estático sin inferencia de machine learning).
     3. Notificar a los analistas para continuar las revisiones de forma manual no asistida.

6. Postmortem, owner and due date:
   - **Responsable del Postmortem:** ML Engineer y Data Scientist, con revisión de Legal y Compliance.
   - **Plazo de entrega (*Due date*):** Máximo 5 días hábiles posteriores a la contención del incidente.
   - **Entregables:** Análisis de causa raíz (RCA), plan de remediación en código/datos y recalibración de pruebas automatizadas.