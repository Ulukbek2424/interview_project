from uuid import UUID

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from rest_framework.viewsets import ViewSet

from apps.advertisement.api.serializers import AdvertisementIDSerializer
from apps.advertisement.service import AdvertisementService


@extend_schema(tags=['Объявления'])
class AdvertisementViewSet(ViewSet):
    service = AdvertisementService()

    @extend_schema(
        operation_id='Список объявлений',
        description='Отображение списка объявлений'
    )
    @action(url_path='advert-list', detail=False, methods=['GET'])
    def advert_list(self, request: Request):
        adverts_info = self.service.get_all_adverts_info()
        return Response({'info': adverts_info}, HTTP_200_OK)

    @extend_schema(
        operation_id='Детали объявления',
        description='Получение данных об объявлении по его ID',
    )
    @action(url_path='advert/(?P<advert_id>[^/.]+)', detail=False, methods=['GET'])
    def advert_detail(self, request: Request, advert_id: UUID):
        serializer = AdvertisementIDSerializer(data={'advert_id': advert_id})
        serializer.is_valid(raise_exception=True)

        advert_info = self.service.get_advert_info(str(advert_id))
        return Response({'info': advert_info}, status=HTTP_200_OK)
