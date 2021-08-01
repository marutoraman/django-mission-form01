from django.views import generic

from ..models.item import *
from ..tables.item import *

class ItemTableView(generic.TemplateView):
    template_name = "item/table.html"

    def get(self, request, *args, **kwargs):
        items = ItemModel.objects.all()
        table = ItemTable(items)
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        return self.render_to_response({'table': table, 'count': items.count()})
