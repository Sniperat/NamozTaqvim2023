from ._base import BotBase
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
from main.utils import user_func, get_regions, save_region_to_user, get_region_and_times, get_saharlik_and_region, get_qazo, decrease_qazo

class Command(BotBase):

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = await user_func(update)
        regions = await get_regions()
        keyboar = []
        for region in regions:
            keyboar.append(
                [
                    InlineKeyboardButton(region.name, callback_data=f'region_{region.id}')
                ]
            )
        reply_markup = InlineKeyboardMarkup(keyboar)
        await update.message.reply_text('Илтимос, ўзингиз истиқомат қилаётган шаҳарни танланг\n\nШаҳар '
                                     'танлаганингиздан сўнг Тақвим автоматик тарзда шу шаҳар вақтига ўзгаради  '
                                     '\n\n*Эслатма: '
                                     'Танланган шаҳарни ўзгартиришингиз мумкин.', reply_markup=reply_markup)

    
    async def region(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = await user_func(update)
        query = update.callback_query
        region_id = query.data.split('_')[1]
        await save_region_to_user(user, region_id)
        keyboard = [
            [
                KeyboardButton('Намоз вактлари')
            ],
            [
                KeyboardButton('Сахарлик вакти'),
                KeyboardButton('Ифторлик вакти')

            ],
            [
                KeyboardButton('Шахарни узгартириш'),
                KeyboardButton('Казоларим')
            ]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard)

        await query.edit_message_text('Танлаган шахарингиз сакланди')
        await update._bot.send_message(chat_id=user.chat_id, text='Ассаламу алайкум ва рахматуллохи ва баракату Ушбу боьтимиз сизга намоз вактларини эслатиш Огыз очищ  ва Епиш вактларидан  5 дакика авваль огонлантириш  хамда окылмай колган намоз казоларини санаснга ёрдам беради', reply_markup=reply_markup)

    async def all_times(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = await user_func(update)
        data = await get_region_and_times(user)
        await update.message.reply_text(f'{data["region"]} шаҳрида бугунги намоз вақтлари' +
                                        '\n*Эслатма: ушбу намоз вактлари Islom.uz сайитидан олинган\n\n'
                                     f'🔹 Бомдод     {data["bomdod"]}\n\n'
                                     f'🔹 Пешин      {data["peshin"]}\n\n'
                                     f'🔹 Аср             {data["asr"]}\n\n'
                                     f'🔹 Шом          {data["shom"]}\n\n'
                                     f'🔹 Хуфтон      {data["xufton"]}')
        
    async def saharlik(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = await user_func(update)
        data = await get_saharlik_and_region(user)
        await update.message.reply_text(f'🏙 Саҳарлик: {data["bomdod"]}\n\nОғиз ёпиш дуоси: Навайту ан асума совма шахри ' +
                                     'рамазона минал фажри илал '
                                     'мағриби, холисан лиллахи таъала. '
                                     'Аллоҳу акбар!\n\n'
                                     f'🏡 Танланган шаҳар: {data["region"]}  ')

    async def iftorlik(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = await user_func(update)
        data = await get_saharlik_and_region(user)
        await update.message.reply_text(f'🌄 Ифторлик: {data["shom"]}\n\nОғиз очиш дуоси: Аллоҳумма лака сумту ва бика ' +
                                     'аманту ва ъалайка таваккалту ва ъала ризқика афтарту, '
                                     'фағфирли ва ғоффарума қоддамту ва ма аххорту. Амийн\n\n'
                                     f'🏡 Танланган шаҳар: {data["region"]}  ')
        
    
    async def qazo(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = await user_func(update)
        query = update.callback_query
        decrease = False
        
        if query != None:
            name_namaz = query.data.split('_')[1]

            decrease = await decrease_qazo(user, name_namaz)
        
        data = await get_qazo(user)

        keyboar = [
            [
                InlineKeyboardButton(f'Бомдод {data["bomdod"]} та казо', callback_data='0'),
                InlineKeyboardButton('Камайтириш', callback_data='qazo_bomdod')
            ],
            [
                InlineKeyboardButton(f'Пешин {data["peshin"]} та казо', callback_data='0'),
                InlineKeyboardButton('Камайтириш', callback_data='qazo_peshin')
            ],
            [
                InlineKeyboardButton(f'Аср {data["asr"]} та казо', callback_data='0'),
                InlineKeyboardButton('Камайтириш', callback_data='qazo_asr')
            ],
            [
                InlineKeyboardButton(f'Шом {data["shom"]} та казо', callback_data='0'),
                InlineKeyboardButton('Камайтириш', callback_data='qazo_shom')
            ],
            [
                InlineKeyboardButton(f'Хуфтон {data["xufton"]} та казо', callback_data='0'),
                InlineKeyboardButton('Камайтириш', callback_data='qazo_xufton')
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboar)

        if decrease:
            await query.edit_message_text('Укылмай колган намозлар', reply_markup=reply_markup)
        else:
            await update.message.reply_text('Укылмай колган намозлар', reply_markup=reply_markup)

    async def qazo_remove(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = await user_func(update)
        query = update.callback_query
        name_namaz = query.data.split('_')[1]
        await decrease_qazo(user, name_namaz)
        await query.delete_message()

    async def delete(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        query = update.callback_query
        await query.delete_message()

    def handle(self, *args, **kwargs):
        app = self.application 
        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(CallbackQueryHandler(self.delete, pattern="^(delete)$"))
        app.add_handler(CallbackQueryHandler(self.region, pattern="^(region_\d)$"))
        app.add_handler(CallbackQueryHandler(self.qazo, pattern="^(qazo_)"))
        app.add_handler(CallbackQueryHandler(self.qazo_remove, pattern="^(del_)"))
        app.add_handler(MessageHandler(filters.Regex('Намоз вактлари'), self.all_times))
        app.add_handler(MessageHandler(filters.Regex('Сахарлик вакти'), self.saharlik))
        app.add_handler(MessageHandler(filters.Regex('Ифторлик вакти'), self.iftorlik))
        app.add_handler(MessageHandler(filters.Regex('Шахарни узгартириш'), self.start))
        app.add_handler(MessageHandler(filters.Regex('Казоларим'), self.qazo))
        
        app.run_polling()
