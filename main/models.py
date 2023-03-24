from django.db import models


class TelegramUserModel(models.Model):
    chat_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    region = models.ForeignKey('RegionModel', on_delete=models.CASCADE, null=True)
    qazo = models.OneToOneField('QazoModel', on_delete=models.CASCADE, null=True)


    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = 'TelegramUser'
        verbose_name_plural = 'TelegramUsers'


class RegionModel(models.Model):
    name = models.CharField(max_length=255)
    time_on_minute = models.IntegerField()
    solat_times = models.ForeignKey('TimeModel', on_delete=models.RESTRICT, null=True)
    

    class Meta:
        verbose_name = ("RegionModel")
        verbose_name_plural = ("RegionsModels")

    def __str__(self):
        return self.name


class TimeModel(models.Model):
    bomdod = models.DateTimeField(null=True)
    quyosh = models.DateTimeField(null=True)
    peshin = models.DateTimeField(null=True)
    asr = models.DateTimeField(null=True)
    shom = models.DateTimeField(null=True)
    xufton = models.DateTimeField(null=True)

    class Meta:
        verbose_name = ("TimeModel")
        verbose_name_plural = ("TimesModels")


class QazoModel(models.Model):
    bomdod = models.IntegerField(default=0)
    quyosh = models.IntegerField(default=0)
    peshin = models.IntegerField(default=0)
    asr = models.IntegerField(default=0)
    shom = models.IntegerField(default=0)
    xufton = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("QazoModel")
        verbose_name_plural = ("QazolarModels")
