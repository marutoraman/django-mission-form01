from django.shortcuts import render
from django.views import generic
from django.contrib import messages 

from ..forms.item_register import *
from ..models.item import *

class ItemRegisterView(generic.TemplateView):
    template_name = "item/register.html"

    def get(self, request, *args, **kwargs):
        form = ItemRegisterForm()
        context = {
            'form': form
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        '''
        登録ボタン押下時
        '''
        params = {'result': '', 'form': None}
        form = ItemRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': form
            }
            messages.success(request, "登録に成功しました。")
            return self.render_to_response(context)
        else:
            messages.warning(request, "登録に失敗しました。")


        
    
    

