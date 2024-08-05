import uuid

from django.db.models import (
    PROTECT,
    CharField,
    DateField,
    ForeignKey,
    Model,
    TextField,
    UUIDField,
    PositiveIntegerField
)

table_prefix = __package__.split('.')[1]


class Category(Model):
    id = UUIDField('Идентификатор', primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField('Название', max_length=256)

    class Meta:
        db_table = f'{table_prefix}_category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class City(Model):
    id = UUIDField('Идентификатор', primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField('Название', max_length=256)

    class Meta:
        db_table = f'{table_prefix}_city'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Advert(Model):
    id = UUIDField('Идентификатор', primary_key=True, default=uuid.uuid4, editable=False)
    created = DateField('Дата создания', auto_now_add=True)
    title = CharField('Название', max_length=256)
    description = TextField('Описание')
    category = ForeignKey(Category, PROTECT, related_name='adverts', verbose_name='Категория')
    city = ForeignKey(City, PROTECT, related_name='adverts', verbose_name='Город')
    views = PositiveIntegerField('Просмотры', blank=True, default=0)

    def to_dict(self, views_count: int | None = None):
        return {
            'identifier': str(self.pk),
            'created': self.created,
            'title': self.title,
            'description': self.description,
            'category': self.category.name if self.category else '',
            'city': self.city.name if self.city else '',
            'views': views_count if views_count else self.views
        }

    class Meta:
        db_table = f'{table_prefix}_advert'
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
