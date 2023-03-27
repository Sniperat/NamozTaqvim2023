from django.contrib import admin
from .models import TelegramUserModel, RegionModel, TimeModel, QazoModel


class DetailAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'username', 'is_active',)
    
admin.site.register(TelegramUserModel, DetailAdmin)
admin.site.register(RegionModel)
admin.site.register(TimeModel)
admin.site.register(QazoModel)
