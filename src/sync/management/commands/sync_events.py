# import requests
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

# from src.sync.models import SyncResult
# from src.events.models import Event


class Command(BaseCommand):
    help = "Synchronize events from events-provider"

    def add_arguments(self, parser):
        parser.add_argument(
            "--date",
            type=str,
            help="Date of events to sync in YYYY-MM-DD format. Defaults to yesterday if not provided.",
        )
        parser.add_argument(
            "--all", action="store_true", help="Sync all events regardless of date."
        )

    def handle(self, *args, **options):
        # Вычисляем дату синхронизации
        if options["all"]:
            sync_date = None
        else:
            if options["date"]:
                try:
                    sync_date = datetime.strptime(options["date"], "%Y-%m-%d").date()
                except ValueError:
                    raise CommandError("Invalid date format. Use YYYY-MM-DD.")
            else:
                sync_date = timezone.now().date() - timedelta(days=1)

        self.stdout.write(f"Starting synchronization for date: {sync_date or 'ALL'}")

        # URL API
        # base_url = "https://events.k3scluster.tech/api/events/"
        params = {}

        if sync_date:
            params["changed_at"] = sync_date.isoformat()

        # Пока API не работает - логируем и заканчиваем
        self.stdout.write(
            "NOTE: events-provider API currently not available, no synchronization performed."
        )
        # Ниже пример кода, который будет выполняться после исправления API
        # FIXME можно вынести в отдельный модуль

        # try:
        #     response = requests.get(base_url, params=params, timeout=10)
        #     response.raise_for_status()
        #     events_data = response.json()
        # except Exception as e:
        #     raise CommandError(f"Failed to fetch events: {e}")

        # new_count, updated_count = 0, 0
        # for event_item in events_data:
        #     event_id = event_item.get("id")
        #     if not event_id:
        #         continue

        #     # Пример обновления или создания ивента
        #     obj, created = Event.objects.update_or_create(
        #         id=event_id,
        #         defaults={
        #             "name": event_item.get("name"),
        #             "event_time": event_item.get("event_time"),
        #             "status": event_item.get("status"),
        #             # Добавить обработку площадки, если есть
        #         }
        #     )
        #     if created:
        #         new_count += 1
        #     else:
        #         updated_count += 1

        # # Записываем результат синхронизации
        # sync_record, _ = SyncResult.objects.update_or_create(
        #     sync_date=sync_date or timezone.now().date(),
        #     defaults={
        #         "new_events_count": new_count,
        #         "updated_events_count": updated_count,
        #     }
        # )
        # self.stdout.write(f"Synchronization complete: {new_count} new, {updated_count} updated.")
