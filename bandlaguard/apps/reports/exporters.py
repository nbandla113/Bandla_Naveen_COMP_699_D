# apps/reports/exporters.py

import os
from django.conf import settings


def export_to_file(report):
    filename = f"report_{report.id}.txt"
    filepath = os.path.join(settings.MEDIA_ROOT, 'reports', filename)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w') as f:
        f.write("BandlaGuard Report\n")
        f.write("====================\n\n")
        f.write(f"Type: {report.report_type}\n")
        f.write(f"Generated: {report.generated_at}\n\n")
        f.write("Data:\n")
        f.write(report.data_snapshot)

    report.file_path = f"reports/{filename}"
    report.save()

    return report.file_path