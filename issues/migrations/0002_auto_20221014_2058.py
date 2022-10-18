from django.db import migrations, models


def populate_status(apps, schemaeditor):
    statuses = {
        "to do": "An issue that has not been started yet",
        "in progress": "An issue that is actively being worked on",
        "done": "an issue that has successfully been completed"
    }
    Status = apps.get_model("issues", "Status")
    for key, desc in statuses.items():
        status_obj = Status(name=key, description=desc)
        status_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [migrations.RunPython(populate_status)]