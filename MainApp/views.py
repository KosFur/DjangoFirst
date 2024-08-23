from django.shortcuts import render
from django.http import HttpResponse

author= {
"Имя": "Иван",
"Отчество": "Петрович",
"Фамилия": "Иванов",
"телефон": "8-923-600-01-02",
"email": "vasya@mail.ru",
}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]
def home (request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
     """
    return HttpResponse(text)

def about(request):
    text=f"""
    Имя: <b>{author["Имя"]}</b><br>
    Отчество: <b>{author["Отчество"]}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(text)

def item_detail(request, item_id):
    
    item = next((item for item in items if item["id"] == item_id), None)

    
    if item is None:
        return HttpResponse("Item not found", status=404)

    
    return render(request, 'item_detail.html', {'item': item})
    