from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)  # Текст задачи (короткий)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания (автоматически)
    is_completed = models.BooleanField(default=False)  # Выполнено? (По умолчанию Нет)

    def __str__(self):
        return self.title
