from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


items = [
    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
    {"id": 7, "name": "Картофель фри" ,"quantity":0},
    {"id": 8, "name": "Кепка" ,"quantity":124},
]

# Create your views here.
def home(request):
    # text = """<h1>"Изучаем django"</h1>
    #         <strong>Автор</strong>: <i>Солнцева А.В.</i>"""
    # return HttpResponse(text)
    context = {
        "name": 'Петров Николай Иванович',
        "email": 'my_mail@mail.ru'
    }
    # return render(request, "index.html")
    return render(request, "index.html", context)

def info(request):
    author = {
        "name": "Алина",
        "middle_name": "Вадимовна",
        "surname": "Солнцева",
        "phone": "+7999999999",
        "mail": "a@mail.ru"
    }
    text = f"""<p>Имя: <strong>{author["name"]}</strong></p>
            <p>Отчество: <strong>{author["middle_name"]}</strong><p>
            <p>Фамилия: <strong>{author["surname"]}</strong><p>
            <p>Телефон: <strong>{author["phone"]}</strong><p>
            <p>email: <strong>{author["mail"]}</strong><p>
            <a href='/'>Home</a>"""
    return HttpResponse(text)

def item_info(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с {id=} не найден")
    else:
        context = {
            "item": item
        }
        return render(request, "item.html", context)
        
    # items_bd = Item.objects.all()
    # for item in items_bd:
    #     if item.id == id:
    # #         text = f"<b>{item['name']}</b> в количестве {item['quantity']} шт"
    # #         return HttpResponse(text)
    #         context = {
    #             "item": item
    #         }
    #         return render(request, "item.html", context)
    # return HttpResponseNotFound(f"Товар с {id=} не найден")

def get_items(request):
    # text = '<h2>Список товаров</h2><ol>'
    # for item in items:
    #     text += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    # text += '</ol>'
    # return HttpResponse(text)

    items_bd = Item.objects.all()
    context = {
        "items": items_bd
    }
    return render(request, "items-list.html", context)

