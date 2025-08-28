from django.db import models
from django.utils import timezone


class SyncResult(models.Model):
    sync_date = models.DateField(default=timezone.now, unique=True)
    new_events_count = models.PositiveIntegerField(default=0)
    updated_events_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sync {self.sync_date}: new {self.new_events_count}, updated {self.updated_events_count}"
