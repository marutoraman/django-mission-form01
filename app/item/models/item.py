from django.db import models

from django.http import request
from django.utils import timezone
from common.utility import get_ulid

class ItemModel(models.Model):
    
    id = models.CharField(max_length=32, default=get_ulid, primary_key=True, editable=False)
    name = models.CharField('商品名', max_length=64, null=False)
    price = models.IntegerField('価格', null=False, default=0)
    thumbnail_url = models.TextField('サムネイルURL', null=True)
    description = models.TextField('説明文', null=True)

    created_at = models.DateTimeField('作成日時',auto_now_add=True)
    updated_at = models.DateTimeField('更新日時',auto_now=True)
    
    class Meta():
        db_table='item'
        