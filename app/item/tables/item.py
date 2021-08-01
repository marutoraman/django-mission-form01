import django_tables2 as tables

from ..models.item import *


class ItemTable(tables.Table):
    
    thumbnail_url = tables.TemplateColumn(
        """
        <div><img src="{{ record.thumbnail_url }}"></div>        
        """)

    class Meta:
        model = ItemModel
        template_name = 'django_tables2/bootstrap4.html'
        orderable = False
        fields = ('thumbnail_url', 'name', 'price', 'description')  
