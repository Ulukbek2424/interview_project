from django.db.models import F

from apps.advertisement.models import Advert


class AdvertisementService:
    """Сервис по работе с объявлениями"""

    def get_all_adverts_info(self) -> list[dict]:
        """Отдает информацию об объявлениях"""
        adverts_info = []

        adverts_qs = Advert.objects.select_related('category', 'city').all()
        for advert in adverts_qs:
            adverts_info.append(advert.to_dict())

        return adverts_info

    def get_advert_info(self, advert_id: str) -> dict:
        """Отдает информацию об одном объявлении"""
        advert = Advert.objects.select_related('category', 'city').filter(pk=advert_id).first()
        if advert:
            self._increment_views(advert)
            return advert.to_dict()
        return {}

    def _increment_views(self, advert: Advert) -> None:
        """Увеличивает счетчик просмотров объявления"""
        advert.views = F('views') + 1 # операция исполняется атомарно, чтобы избежать проблем с конкурентностью на уровне БД
        advert.save(update_fields=['views'])
