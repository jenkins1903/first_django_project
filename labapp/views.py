from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.shortcuts import get_object_or_404

user_info = {
    'first_name': 'Евгения',
    'middle_name': 'Станиславовна',
    'last_name': 'Ралдугина',
    'phone': '8-921-633-26-19',
    'email': 'evgeniya_raldugina@vk.com',
}

# def home(request):
#     author_name = "Ралдугина Е. С."  
#     html_content = f'<h1>"Изучаем django"</h1><strong>Автор</strong>: <i>{author_name}</i>'
#     return HttpResponse('<h1>Добро пожаловать на главную страницу!</h1><a href="/items/">Список товаров</a>')
#     return HttpResponse(html_content)

def home(request):
    html_content = '<h1>"Изучаем django"</h1><strong>Автор</strong>: <i>Ралдугина Е. С.</i><br><a href="/items/">Список товаров</a>'
    return HttpResponse(html_content)

# def about(request):
#     info = "<br>".join([f"{key}: {value}" for key, value in user_info.items()])
#     return HttpResponse(f"<div>{info}</div>")

def about(request):
    info = "<br>".join([f"{key}: {value}" for key, value in user_info.items()])
    return HttpResponse(f"<div>{info}</div>")

# items = [
#     {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#     {"id": 2, "name": "Куртка кожаная", "quantity": 4},
#     {"id": 3, "name": "Coca-cola 1 литр", "quantity": 3},
#     {"id": 4, "name": "Картофель фри", "quantity": 2},
#     {"id": 5, "name": "Кепка", "quantity": 1},
# ]


# def item_list(request):
#     html = "<ol>" + "".join([f"<li>{item['name']}</li>" for item in items]) + "</ol>"
#     return HttpResponse(html)

# def items_list(request):
#     items = Item.objects.all()
#     return render(request, 'items_list.html', {'items': items})


def items_list(request):
    items = Item.objects.all()
    return render(request, 'items_list.html', {'items': items})


# def item_detail(request, item_id):
#     item = next((item for item in items if item['id'] == item_id), None)
#     if item is not None:
#         return render(request, 'item.html', {'item': item})
#     else:
#         return HttpResponse(f"Товар с id={item_id} не найден", status=404)


    
# def item_list(request):
#     html = "<ol>" + "".join([f"<li><a href='/item/{item['id']}/'>{item['name']}</a></li>" for item in items]) + "</ol>"
#     return HttpResponse(html)


# def item_detail(request, item_id): 
#     item = get_object_or_404(Item, pk=item_id)
#     return render(request, 'item_detail.html', {'item': item})

def item_detail(request, item_id): 
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item_detail.html', {'item': item})