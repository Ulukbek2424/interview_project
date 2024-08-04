from rest_framework.exceptions import ValidationError
from rest_framework.fields import UUIDField
from rest_framework.serializers import Serializer

from apps.advertisement.models import Advert


class AdvertisementIDSerializer(Serializer):
    advert_id = UUIDField(label='UUID Объявления', help_text='ID объявления')

    def validate_advert_id(self, value):
        is_exist = Advert.objects.filter(pk=value).exists()

        if is_exist is False:
            raise ValidationError(f'Объявления с данным ID не существует, ID={value}.')
        return value
