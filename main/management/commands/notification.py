from ._base import BotBase
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from main.models import RegionModel, TelegramUserModel
import asyncio

current_time = datetime.now().time()

class Command(BotBase):

    def handle(self, *args, **kwargs):
        app = self.application
        keyboard = [
            [
                InlineKeyboardButton("Ёпиш", callback_data='delete'),
            ],

        ]
        reply_markup = InlineKeyboardMarkup(keyboard) 
        # asyncio.run(app.bot.send_message(chat_id=920393608, text='salom', reply_markup=reply_markup))
        regions = RegionModel.objects.all()
        for region in regions:
            # TODO send saharlik time
            bomdod_time = region.solat_times.bomdod + timedelta(minutes=-5)  
            if current_time.hour == bomdod_time.hour and current_time.minute == bomdod_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Бомдод вақтига 5 дақиқа қолди\n\nОғиз ёпиш дуоси: Навайту ан асума совма шахри ' +
                                     'рамазона минал фажри илал '
                                     'мағриби, холисан лиллахи таъала. '
                                     'Аллоҳу акбар!\n\n'
                                     , reply_markup=reply_markup))

            # TODO send iftorlik time
            shom_time = region.solat_times.shom + timedelta(minutes=-5)  
            if current_time.hour == shom_time.hour and current_time.minute == shom_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Шом вақтига 5 дақиқа қолди\n\nОғиз очиш дуоси: Аллоҳумма лака сумту ва бика ' +
                                     'аманту ва ъалайка таваккалту ва ъала ризқика афтарту, '
                                     'фағфирли ва ғоффарума қоддамту ва ма аххорту. Амийн\n\n'
                                     , reply_markup=reply_markup))
                    
        
        # TODO Namoz vaqtlarini eslatish
        for region in regions:

            # BOMDOD
            keyboard = [[InlineKeyboardButton("Кейинрок укийман", callback_data='delete'),],
            [InlineKeyboardButton("Укидим", callback_data='del_bomdod')],]
            reply_markup = InlineKeyboardMarkup(keyboard) 
            bomdod_time = region.solat_times.bomdod
            if current_time.hour == bomdod_time.hour and current_time.minute == bomdod_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Бомдод вақти бўлди'
                                     , reply_markup=reply_markup))
                    qazo = user.qazo
                    qazo.bomdod +=1
                    qazo.save()

            # Peshin
            keyboard = [[InlineKeyboardButton("Кейинрок укийман", callback_data='delete'),],
            [InlineKeyboardButton("Укидим", callback_data='del_peshin')],]
            reply_markup = InlineKeyboardMarkup(keyboard) 
            peshin_time = region.solat_times.peshin
            if current_time.hour == peshin_time.hour and current_time.minute == peshin_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Пешин вақти бўлди'
                                     , reply_markup=reply_markup))
                    qazo = user.qazo
                    qazo.peshin +=1
                    qazo.save()

            # ASR
            keyboard = [[InlineKeyboardButton("Кейинрок укийман", callback_data='delete'),],
            [InlineKeyboardButton("Укидим", callback_data='del_asr')],]
            reply_markup = InlineKeyboardMarkup(keyboard) 
            asr_time = region.solat_times.asr
            if current_time.hour == asr_time.hour and current_time.minute == asr_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Аср вақти бўлди'
                                     , reply_markup=reply_markup))
                    qazo = user.qazo
                    qazo.asr +=1
                    qazo.save()
            
            # SHOM
            keyboard = [[InlineKeyboardButton("Кейинрок укийман", callback_data='delete'),],
            [InlineKeyboardButton("Укидим", callback_data='del_shom')],]
            reply_markup = InlineKeyboardMarkup(keyboard) 
            shom_time = region.solat_times.shom
            if current_time.hour == shom_time.hour and current_time.minute == shom_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Шом вақти бўлди'
                                     , reply_markup=reply_markup))
                    qazo = user.qazo
                    qazo.shom +=1
                    qazo.save()

            # XUFTON
            keyboard = [[InlineKeyboardButton("Кейинрок укийман", callback_data='delete'),],
            [InlineKeyboardButton("Укидим", callback_data='del_xufton')],]
            reply_markup = InlineKeyboardMarkup(keyboard) 
            xufton_time = region.solat_times.xufton
            if current_time.hour == xufton_time.hour and current_time.minute == xufton_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Хуфтон вақти бўлди'
                                     , reply_markup=reply_markup))
                    qazo = user.qazo
                    qazo.xufton +=1
                    qazo.save()
            