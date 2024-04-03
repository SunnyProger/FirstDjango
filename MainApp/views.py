from django.http import HttpResponse
from django.shortcuts import render

author = {
    "name": "Алина",
    "middle_name": "Вадимовна",
    "surname": "Солнцева",
    "phone": "+7999999999",
    "mail": "a@mail.ru"
}

items = [
    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
    {"id": 7, "name": "Картофель фри" ,"quantity":0},
    {"id": 8, "name": "Кепка" ,"quantity":124},
]

# Create your views here.
def home(request):
    text = """<h1>"Изучаем django"</h1>
            <strong>Автор</strong>: <i>Солнцева А.В.</i>"""
    return HttpResponse(text)

def info(request):
    text = f"""<p>Имя: <strong>{author["name"]}</strong></p>
            <p>Отчество: <strong>{author["middle_name"]}</strong><p>
            <p>Фамилия: <strong>{author["surname"]}</strong><p>
            <p>Телефон: <strong>{author["phone"]}</strong><p>
            <p>email: <strong>{author["mail"]}</strong><p>"""
    return HttpResponse(text)

def item_info(request, id):
    for item in items:
        if item['id'] == id:
            text = f"<b>{item['name']}</b> в количестве {item['quantity']} шт"
            return HttpResponse(text)
    return HttpResponse(f"Товар с {id=} не найден")

def get_items(request):
    text = '<h2>Список товаров</h2><ol>'
    for item in items:
        text += f"<li>{item['name']}</li>"
    text += '</ol>'
    return HttpResponse(text)

