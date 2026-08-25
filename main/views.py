from django.http import HttpResponse
from datetime import datetime,time
from .models import Task
from django.shortcuts import render, redirect


def home(request):
    tasks = Task.objects.all()
    return render(request, 'main/home.html', {'tasks': tasks})

def add_task(request):
     # Проверяем, пришел ли текст в запросе (через GET параметры)
    task_text = request.GET.get('task_text')

    if task_text:  # Если текст есть
        Task.objects.create(title=task_text)  # Создаем задачу в базе
        return redirect('/')  # Перенаправляем на главную

    # Если текст не ввели — показываем форму для ввода
    return HttpResponse('''
        <h1>Добавить задачу</h1>
        <form method="get">
            <input type="text" name="task_text" placeholder="Напишите задачу...">
            <button type="submit">Сохранить</button>
        </form>
        <p><a href="/">Назад к списку</a></p>
    ''')


def время_сейчас(request):
    время=datetime.now()
    return HttpResponse(время)
def обомне(request):
    время=datetime.now()
    часы=время.hour
    минуты=время.minute
    секунды=время.second
    return HttpResponse(f"<h1>Время сейчас: {часы}:{минуты}:{секунды}</h1>")
def info(request):
    время=datetime.now()
    новый_год=datetime(2026,12,31,23,59)
    до_нового_года1=новый_год-время
    до_нового_года_дней=до_нового_года1.days
    до_нового_года_часов=до_нового_года1.seconds//3600
    до_нового_года_минут=(до_нового_года1.seconds%3600)//60
    до_нового_года_секунд=(до_нового_года1.seconds%3600)%60
    return HttpResponse(f"<h1>До нового года осталось дней: {до_нового_года_дней}    Часов: {до_нового_года_часов} Минут:  {до_нового_года_минут}   Секунд:  {до_нового_года_секунд}</h1> ")

# Create your views here.
