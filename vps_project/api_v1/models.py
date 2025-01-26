from django.db import models


class VPS(models.Model):
    '''Объект VPS включают следующие параметры:
    uid — уникальный идентификатор сервера.  
    cpu — количество процессорных ядер.  
    ram — объем оперативной памяти.  
    hdd — объем дискового пространства.  
    status — текущий статус сервера (например, started, blocked, stopped).'''

    STATUSES = {
        "started": "Запущен",
        "blocked": "Заблокирован",
        "stopped": "Остановлен",
    }
    uid = models.CharField("Идентификатор сервера", unique=True)
    cpu = models.SmallIntegerField("Количество процессорных ядер", default=0)
    ram = models.DecimalField(
        "Объем оперативной памяти (Мб)", default=0.0, decimal_places=2, max_digits=8)
    hdd = models.DecimalField(
        "Объем дискового пространства (Гб)", default=0.0, decimal_places=2, max_digits=8)
    status = models.CharField("Статус сервера", choices=STATUSES)

    def __str__(self):
        return self.uid

    class Meta:
        verbose_name = "Объект VPS"
        verbose_name_plural = "Объекты VPS"
