from django.contrib import admin
from .models import TelegramUserModel, RegionModel, TimeModel, QazoModel


admin.site.register(TelegramUserModel)
admin.site.register(RegionModel)
admin.site.register(TimeModel)
admin.site.register(QazoModel)
