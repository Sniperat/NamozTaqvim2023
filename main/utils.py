from .models import TelegramUserModel, RegionModel, QazoModel
from asgiref.sync import sync_to_async
from django.db.models import F

@sync_to_async
def user_func(update):
    try:
        user = TelegramUserModel.objects.get(chat_id=update.effective_user.id, is_active=True)
    except Exception as e:
        user = TelegramUserModel(
            chat_id=update.effective_user.id, 
            username=update.effective_user.username,
            full_name=update.effective_user.full_name,
            is_active=True
        )
        qazo = QazoModel.objects.create()
        user.qazo = qazo
        user.save()
    return user

@sync_to_async
def get_regions():
    return list(RegionModel.objects.all())

@sync_to_async
def save_region_to_user(user, region_id):
    user.region = RegionModel.objects.get(id=region_id)
    user.save()
    return True

@sync_to_async
def get_region_and_times(user):
    data = {
        'region': user.region.name,
        'bomdod': user.region.solat_times.bomdod.time(),
        'peshin': user.region.solat_times.peshin.time(),
        'asr': user.region.solat_times.asr.time(),
        'shom':user.region.solat_times.shom.time(),
        'xufton': user.region.solat_times.xufton.time()
    }
    return data

@sync_to_async
def get_saharlik_and_region(user):
    data = {
        'region': user.region.name,
        'bomdod': user.region.solat_times.bomdod.time(),
        'shom':user.region.solat_times.shom.time(),
    }
    return data


@sync_to_async
def decrease_qazo(user, name_namaz):
    qazo = user.qazo
    if qazo.__dict__[name_namaz] > 0:
        qazo.__dict__[name_namaz] -= 1
        qazo.save()
        return True
    else:
        return 1

@sync_to_async
def get_qazo(user):
    if user.qazo != None:
        qazo_count = QazoModel.objects.get(id=user.qazo.id)  
        return {
            'bomdod': qazo_count.bomdod,
            'peshin': qazo_count.peshin,
            'asr': qazo_count.asr,
            'shom': qazo_count.shom,
            'xufton': qazo_count.xufton
        }  
    else:
        qazo_count = QazoModel()
        qazo_count.save()
        user.qazo = qazo_count
        user.save()
        return {
            'bomdod': 0,
            'peshin': 0,
            'asr': 0,
            'shom': 0,
            'xufton': 0
        }

