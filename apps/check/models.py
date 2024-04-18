from django.db import models


class ChecksModel(models.Model):
    class Meta:
        verbose_name = 'Check'
        verbose_name_plural = 'Checks'
        db_table = 'check_checks'

    json_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
