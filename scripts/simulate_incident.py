from datetime import datetime, timezone
from pathlib import Path

text = f"""# Incident simulation

- detected_at: {datetime.now(timezone.utc).isoformat()}
- signal: recall gap exceeded
- containment: REVIEW and safe baseline
- evidence: preserved report and model version
- communication: Notified Institutional Owner, Legal, and affected business units within 1 hour
- corrective actions, owners and dates: Data Scientist to recalibrate thresholds by 2026-11-05; ML Engineer to deploy monitor tests by 2026-11-06
"""

path = Path("reports/lab13/INCIDENT_POSTMORTEM.md")
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(text, encoding="utf-8")
print(path)