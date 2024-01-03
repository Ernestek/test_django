from django.shortcuts import render
from app.models import Item


def item_list(request):
    items = Item.objects.all()
    return render(request, 'app/item_list.html', {'items': items})
