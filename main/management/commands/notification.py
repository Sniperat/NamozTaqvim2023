from ._base import BotBase
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from main.models import RegionModel, TelegramUserModel
import asyncio
import trio
import time
current_time = datetime.now().time()

class Command(BotBase):

    async def sent_msg(self, chat_id, reply_markup, text_me):
        app= self.application
        await app.bot.send_message(chat_id=chat_id, text=text_me
                                     , reply_markup=reply_markup)
        time.sleep(0.1)

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
                    try:
                        text_me = 'Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'\
                                     'Бомдод вақтига 5 дақиқа қолди\n\nОғиз ёпиш дуоси: Навайту ан асума совма шахри ' \
                                     'рамазона минал фажри илал '\
                                     'мағриби, холисан лиллахи таъала. '\
                                     'Аллоҳу акбар!\n\n'
                        trio.run(self.sent_msg, user.chat_id, reply_markup, text_me)
                        # asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                        #              'Бомдод вақтига 5 дақиқа қолди\n\nОғиз ёпиш дуоси: Навайту ан асума совма шахри ' +
                        #              'рамазона минал фажри илал '
                        #              'мағриби, холисан лиллахи таъала. '
                        #              'Аллоҳу акбар!\n\n'
                        #              , reply_markup=reply_markup))
                    except:
                        user.is_active = False
                        user.save()

            # TODO send iftorlik time
            shom_time = region.solat_times.shom + timedelta(minutes=-5)  
            if current_time.hour == shom_time.hour and current_time.minute == shom_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    try:
                        text_me = 'Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n' \
                                     'Шом вақтига 5 дақиқа қолди\n\nОғиз очиш дуоси: Аллоҳумма лака сумту ва бика ' \
                                     'аманту ва ъалайка таваккалту ва ъала ризқика афтарту, '\
                                     'фағфирли ва ғоффарума қоддамту ва ма аххорту. Амийн\n\n'
                        trio.run(self.sent_msg, user.chat_id, reply_markup, text_me)
                        # asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                        #              'Шом вақтига 5 дақиқа қолди\n\nОғиз очиш дуоси: Аллоҳумма лака сумту ва бика ' +
                        #              'аманту ва ъалайка таваккалту ва ъала ризқика афтарту, '
                        #              'фағфирли ва ғоффарума қоддамту ва ма аххорту. Амийн\n\n'
                        #              , reply_markup=reply_markup))
                    except:
                        user.is_active = False
                        user.save()
                    
        
        # TODO Namoz vaqtlarini eslatish
        for region in regions:

            # BOMDOD
            keyboard = [[InlineKeyboardButton("Кейинрок укийман", callback_data='delete'),],
            [InlineKeyboardButton("Укидим", callback_data='del_bomdod')],]
            reply_markup = InlineKeyboardMarkup(keyboard) 
            bomdod_time = region.solat_times.bomdod
            if current_time.hour == bomdod_time.hour and current_time.minute == bomdod_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    try:
                        text_me = 'Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\nБомдод вақти бўлди'
                        trio.run(self.sent_msg, user.chat_id, reply_markup, text_me)
                        # asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                        #              'Бомдод вақти бўлди'
                        #              , reply_markup=reply_markup))
                        qazo = user.qazo
                        qazo.bomdod +=1
                        qazo.save()
                    except:
                        user.is_active = False
                        user.save()

            # Peshin
            keyboard = [[InlineKeyboardButton("Кейинрок укийман", callback_data='delete'),],
            [InlineKeyboardButton("Укидим", callback_data='del_peshin')],]
            reply_markup = InlineKeyboardMarkup(keyboard) 
            peshin_time = region.solat_times.peshin
            if current_time.hour == peshin_time.hour and current_time.minute == peshin_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    print(user.region.name)
                    try:
                        text_me = 'Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\nПешин вақти бўлди'
                        trio.run(self.sent_msg, user.chat_id, reply_markup, text_me)
                        # asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                        #              'Пешин вақти бўлди'
                        #              , reply_markup=reply_markup))
                        qazo = user.qazo
                        qazo.peshin +=1
                        qazo.save()
                    except:
                        print(user.region.name, 'musur')
                        user.is_active = False
                        user.save()

            # ASR
            keyboard = [[InlineKeyboardButton("Кейинрок укийман", callback_data='delete'),],
            [InlineKeyboardButton("Укидим", callback_data='del_asr')],]
            reply_markup = InlineKeyboardMarkup(keyboard) 
            asr_time = region.solat_times.asr
            if current_time.hour == asr_time.hour and current_time.minute == asr_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    try:
                        text_me = 'Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\nАср вақти бўлди'
                        trio.run(self.sent_msg, user.chat_id, reply_markup, text_me)
                        # asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                        #              'Аср вақти бўлди'
                        #              , reply_markup=reply_markup))
                        qazo = user.qazo
                        qazo.asr +=1
                        qazo.save()
                    except:
                        user.is_active = False
                        user.save()
            
            # SHOM
            keyboard = [[InlineKeyboardButton("Кейинрок укийман", callback_data='delete'),],
            [InlineKeyboardButton("Укидим", callback_data='del_shom')],]
            reply_markup = InlineKeyboardMarkup(keyboard) 
            shom_time = region.solat_times.shom
            if current_time.hour == shom_time.hour and current_time.minute == shom_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    try:
                        text_me = 'Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\nШом вақти бўлди'
                        trio.run(self.sent_msg, user.chat_id, reply_markup, text_me)
                        # asyncio.run(app.bot.send_message(chat_id=user.chat_id, text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                        #              'Шом вақти бўлди'
                        #              , reply_markup=reply_markup))
                        qazo = user.qazo
                        qazo.shom +=1
                        qazo.save()
                    except:
                        user.is_active = False
                        user.save()

            # XUFTON
            keyboard = [[InlineKeyboardButton("Кейинрок укийман", callback_data='delete'),],
            [InlineKeyboardButton("Укидим", callback_data='del_xufton')],]
            reply_markup = InlineKeyboardMarkup(keyboard) 
            xufton_time = region.solat_times.xufton
            if current_time.hour == xufton_time.hour and current_time.minute == xufton_time.minute:
                for user in TelegramUserModel.objects.filter(region=region):
                    try:

                        text_me = 'Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\nХуфтон вақти бўлди'
                        trio.run(self.sent_msg, user.chat_id, reply_markup, text_me)
                 
                        qazo = user.qazo
                        qazo.xufton +=1
                        qazo.save()
                    except:
                        print(user.username, 'falce')

                        user.is_active = False
                        user.save()

            