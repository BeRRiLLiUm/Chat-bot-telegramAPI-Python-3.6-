import os 
import telebot 
import logging
from telebot import types
import datetime 
bot = telebot.TeleBot('-');
import csv
import io



@bot.message_handler(commands=['start'])
def start_message(message):
     keyboard = telebot.types.ReplyKeyboardMarkup(True)
     keyboard.row('Поступление в РЭУ')
     keyboard.row('Почему в РЭУ?')
     keyboard.row('Где мы находимся?', 'Контакты')
     keyboard.row('Задай вопрос')
     keyboard.row('Социальные сети')
     bot.send_message(message.chat.id, message.from_user.first_name + ', привет! Это Telegram-бот ПИ(ф) РЭУ им. Г.В. Плеханова.\nЧтобы узнать больше о нас, выбери одну из опций в меню.', reply_markup=keyboard)
     REU = open('/usr/local/sbin/venvs/telebot/body/рэу.jpg', 'rb')
     bot.send_photo(message.chat.id, REU)
@bot.message_handler(commands=['help'])
def start_message(message):

    bot.send_message(message.from_user.id, "Выбери одну из опций в меню, чтобы узнать необходимую информацию.")
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Поступление в РЭУ')
    keyboard.row('Почему в РЭУ?')
    keyboard.row('Где мы находимся?', 'Контакты')
    keyboard.row('Задай вопрос')
    keyboard.row('Социальные сети')
@bot.message_handler(content_types=['text']) 
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, "+ message.from_user.first_name + "!")
    elif message.text == "Поступление в РЭУ":
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + message.from_user.first_name, message.from_user.id,"Поступление в РЭУ", file=botlogfile)
        botlogfile.close()
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Направления бакалавриата', callback_data=1))
        markup.add(telebot.types.InlineKeyboardButton(text='Программы магистратуры', callback_data=2))
        markup.add(telebot.types.InlineKeyboardButton(text='Специальности СПО', callback_data=3))
        markup.add(telebot.types.InlineKeyboardButton(text='Подача документов', callback_data=4))
        markup.add(telebot.types.InlineKeyboardButton(text='Приём на программы ВО', callback_data=5))
        markup.add(telebot.types.InlineKeyboardButton(text='Приём на программы СПО', callback_data=6))
        markup.add(telebot.types.InlineKeyboardButton(text='Назад в меню', callback_data=22))
        bot.send_message(message.chat.id, text="Выбери пункт, который тебя интересует: ", reply_markup=markup)
    elif message.text == "Почему в РЭУ?":
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + message.from_user.first_name, message.from_user.id,"Почему в РЭУ?", file=botlogfile)
        botlogfile.close()
        REU1 = open('/usr/local/sbin/venvs/telebot/body/wat.png', 'rb')
        bot.send_photo(message.chat.id, REU1)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад в меню', callback_data=22))
    elif message.text == "Где мы находимся?":
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + message.from_user.first_name, message.from_user.id,"Где мы находимся?", file=botlogfile)
        botlogfile.close()
        bot.send_message(message.from_user.id,message.from_user.first_name + "Адрес Пермского института (филиала) РЭУ им. Г.В. Плеханова: \n \n614070, г.Пермь, бульвар Гагарина, д. 57")
        bot.send_chat_action(message.chat.id, 'find_location')
        bot.send_location(message.chat.id, 58.008915, 56.283504)
    elif message.text == "Контакты":
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + message.from_user.first_name, message.from_user.id,"Контакты", file=botlogfile)
        botlogfile.close()
        bot.send_message(message.from_user.id, "Жданкова Ирина Викторовна\nОтветственный секретарь приемной комиссии \n \nГрафик работы приемной комиссии:\nПонедельник – пятница – с 9:30 до 17:00\nСуббота – с 10:00 до 14:00\nВоскресенье – выходной \n \nАдрес приемной комиссии: \n614070, г. Пермь, бульвар Гагарина, 57 \n \nтелефон: 8 (342) 294-56-92, \n8-912-88-44-050\n \nperm.pk@rea.ru")
    elif message.text == "Задай вопрос":
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + message.from_user.first_name, message.from_user.id ,"Задай вопрос", file=botlogfile)
        botlogfile.close()
        bot.send_message(message.from_user.id, "\n8-912-88-44-050 (Whatsapp / telegram)\n \nperm.pk@rea.ru")
    elif message.text == "Социальные сети":
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + message.from_user.first_name, message.from_user.id,"Социальные сети", file=botlogfile)
        botlogfile.close()
        markup = telebot.types.InlineKeyboardMarkup()
        vk= telebot.types.InlineKeyboardButton(text='VK', url='https://vk.com/rea_perm')
        inst= telebot.types.InlineKeyboardButton(text='Instagram', url='http://instagram.com/plekhanovka_perm')
        yt= telebot.types.InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/channel/UC4J0RDdkIv6C1JsopbWDfyQ?view_as=subscriber')
        markup.add(vk, inst, yt)
        bot.send_message(message.chat.id, message.from_user.first_name + ", переходи в наши социальные сети, чтобы всегда быть в курсе наших новостей.", reply_markup = markup)
    else :
        bot.send_message(message.from_user.id,message.from_user.first_name + ", выбери одну из опций на клавиатуре, чтобы узнать необходимую информацию")
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == '1':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Менеджмент ', callback_data=7))
        markup.add(telebot.types.InlineKeyboardButton(text='Товароведение', callback_data=8))            
        markup.add(telebot.types.InlineKeyboardButton(text='Технология продукции и орг. обществ. питания', callback_data=9))
        markup.add(telebot.types.InlineKeyboardButton(text='Торговое дело', callback_data=10))
        markup.add(telebot.types.InlineKeyboardButton(text='Экономика', callback_data=11))
        markup.add(telebot.types.InlineKeyboardButton(text='Прикладная информатика ', callback_data=12))
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back"))
        bot.send_message(call.message.chat.id, text="Направления бакалавриата", reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"Направления бакалавриата", file=botlogfile)
        botlogfile.close()
    elif call.data == '2':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Экономика ', callback_data=13))
        markup.add(telebot.types.InlineKeyboardButton(text='Менеджмент ', callback_data=14))
        markup.add(telebot.types.InlineKeyboardButton(text='Торговое дело ', callback_data=15))
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back"))
        bot.send_message(call.message.chat.id, text="Программы магистратуры", reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"Программы магистратуры", file=botlogfile)
        botlogfile.close()
    elif call.data == '3' :
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Банковское дело', callback_data=16))
        markup.add(telebot.types.InlineKeyboardButton(text='Страховое дело', callback_data=17))
        markup.add(telebot.types.InlineKeyboardButton(text='Товароведение и экспертиза кач-ва потр. тов.', callback_data=18))
        markup.add(telebot.types.InlineKeyboardButton(text='Экономика и бух. учёт', callback_data=19))
        bot.send_message(call.message.chat.id, text="Торгово-технологическое отделение", reply_markup=markup)

        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"Торгово-технологическое отделение", file=botlogfile)
        botlogfile.close()

        markup = telebot.types.InlineKeyboardMarkup()

    elif call.data == '4' :
        bot.send_message(call.message.chat.id, "Документы необходимые для подачи заявления \n \n1. Документ об образовании (подлинник или копия);\n2. Четыре фотографии 3х4 см (для поступающих на программы СПО); Две фотографии 3х4 см (для поступающих на программы ВО);\n3. Копия свидетельства о браке (в случае изменения фамилии); \n4. Копия паспорта;\n5. Справка о состоянии здоровья при поступлении на направление «Технология продукции и организация общественного питания» \n6. СНИЛС")
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back"))
        bot.send_message(call.message.chat.id, text= "Выбери пункт назад, чтобы перейти в меню. " , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"Документы необходимые для подачи заявления", file=botlogfile)
        botlogfile.close()

    elif call.data == '5' :
        bot.send_message(call.message.chat.id, "ПРИЕМ НА НАПРАВЛЕНИЯ И ПРОГРАММЫ ВО")
        markup = telebot.types.InlineKeyboardMarkup()
        vo1= telebot.types.InlineKeyboardButton(text='приём бакалавриат', url='https://www.rea.ru/ru/org/managements/priem/Documents/Normativ_Dokuments/2021/%D0%91%D0%B0%D0%BA_%D0%A0%D0%AD%D0%A3/%D0%A0%D0%AD%D0%A3_%D0%91%D0%B0%D0%BA_%D0%9F%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2011_2021.pdf')
        markup.add(vo1)
        bot.send_message(call.message.chat.id, "Ссылка на документы приёма на специальности бакалаврита.", reply_markup = markup)
        markup = telebot.types.InlineKeyboardMarkup()
        vo2= telebot.types.InlineKeyboardButton(text='приём магистратура', url='https://www.rea.ru/ru/org/managements/priem/Documents/Normativ_Dokuments/2021/%D0%9C%D0%B0%D0%B3_%D0%A0%D0%AD%D0%A3/%D0%A0%D0%AD%D0%A3_%D0%9C%D0%B0%D0%B3_%D0%9F%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%206_2021.pdf')
        markup.add(vo2)
        bot.send_message(call.message.chat.id, "Ссылка на документы приёма на программы магитратуры.", reply_markup = markup)
        markup = telebot.types.InlineKeyboardMarkup()
        vo= telebot.types.InlineKeyboardButton(text='ссылка', url='http://rea.perm.ru/?page_id=759')
        markup.add(vo)
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back"))
        bot.send_message(call.message.chat.id, "Нажмите на ссылку ниже, чтобы получить дополнительную информацию о приёме на программы и специальности ВО", reply_markup = markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"ПРИЕМ НА НАПРАВЛЕНИЯ И ПРОГРАММЫ ВО", file=botlogfile)
        botlogfile.close()

    elif call.data == '6' :
        bot.send_message(call.message.chat.id, "ПРИЁМ НА ПРОГРАММЫ СПО")
        markup = telebot.types.InlineKeyboardMarkup()
        spo1= telebot.types.InlineKeyboardButton(text='приём СПО', url='http://rea.perm.ru/images/Download/4Abiturientu/12PravilaSPO/PravilaSPO.pdf')
        markup.add(spo1)
        bot.send_message(call.message.chat.id, "Ссылка на документы приёма на специальности СПО.", reply_markup = markup)
        markup = telebot.types.InlineKeyboardMarkup()
        spo= telebot.types.InlineKeyboardButton(text='ссылка', url='http://rea.perm.ru/?page_id=761')
        markup.add(spo)
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back"))
        bot.send_message(call.message.chat.id, "Нажмите на ссылку ниже, чтобы получить дополнительную иформацию о приёме на программу СПО", reply_markup = markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"ПРИЁМ НА ПРОГРАММЫ СПО", file=botlogfile)
        botlogfile.close()

#бакалавр 7-12 назад вызов колл 1
    elif call.data == '7' :
        bot.send_message(call.message.chat.id, "МЕНЕДЖМЕНТ")
        MN1 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/MN/мн1.PNG', 'rb')
        bot.send_photo(call.message.chat.id, MN1)
        MN2 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/MN/мн2.PNG', 'rb')
        bot.send_photo(call.message.chat.id, MN2)
        MN3 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/MN/мн3.PNG', 'rb')
        bot.send_photo(call.message.chat.id, MN3)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back1"))
        bot.send_message(call.message.chat.id, text= "Выбери пункт назад, чтобы перейти к выбору направления." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"МЕНЕДЖМЕНТ БАКАЛАВРИАТ", file=botlogfile)
        botlogfile.close()

    elif call.data == '8' :
        bot.send_message(call.message.chat.id, "ТОВАРОВЕДЕНИЕ")
        TV1 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/TV/тв1.PNG', 'rb')
        bot.send_photo(call.message.chat.id, TV1) 
        TV2 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/TV/тв2.PNG', 'rb')
        bot.send_photo(call.message.chat.id, TV2) 
        TV3 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/TV/тв3.PNG', 'rb')
        bot.send_photo(call.message.chat.id, TV3) 
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back1"))
        bot.send_message(call.message.chat.id, text= "Выбери пункт назад, чтобы перейти к выбору направления." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"ТОВАРОВЕДЕНИЕ БАКАЛАВРИАТ", file=botlogfile)
        botlogfile.close()

    elif call.data == '9' :
        bot.send_message(call.message.chat.id, "ТЕХНОЛОГИЯ ПРОДУКЦИИ И ОРГАНИЗАЦИЯ ОБЩЕСТВЕННОГО ПИТАНИЯ") 
        TP1 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/TP/тп1.PNG', 'rb')
        bot.send_photo(call.message.chat.id, TP1)
        TP2 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/TP/тп2.PNG', 'rb')
        bot.send_photo(call.message.chat.id, TP2)
        TP3 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/TP/тп3.PNG', 'rb')
        bot.send_photo(call.message.chat.id, TP3)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back1"))
        bot.send_message(call.message.chat.id, text= "Выбери пункт назад, чтобы перейти к выбору направления." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"ТЕХНОЛОГИЯ ПРОДУКЦИИ И ОРГАНИЗАЦИЯ ОБЩЕСТВЕННОГО ПИТАНИЯ БАКАЛАВРИАТ", file=botlogfile)
        botlogfile.close()

    elif call.data == '10' :
        bot.send_message(call.message.chat.id, "ТОРГОВОЕ ДЕЛО") 
        TD1 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/TD/тд1.PNG', 'rb')
        bot.send_photo(call.message.chat.id, TD1)
        TD2 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/TD/тд2.PNG', 'rb')
        bot.send_photo(call.message.chat.id, TD2)
        TD3 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/TD/тд3.PNG', 'rb')
        bot.send_photo(call.message.chat.id, TD3)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back1"))
        bot.send_message(call.message.chat.id, text= "Выбери пункт назад, чтобы перейти к выбору направления." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"ТОРГОВОЕ ДЕЛО БАКАЛАВРИАТ", file=botlogfile)
        botlogfile.close()

    elif call.data == '11' :
        bot.send_message(call.message.chat.id, "ЭКОНОМИКА") 
        AK1 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/AK/эк1.PNG', 'rb')
        bot.send_photo(call.message.chat.id, AK1)
        AK2 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/AK/эк2.PNG', 'rb')
        bot.send_photo(call.message.chat.id, AK2)
        AK3 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/AK/эк3.PNG', 'rb')
        bot.send_photo(call.message.chat.id, AK3)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back1"))
        bot.send_message(call.message.chat.id, text= "Выбери пункт назад, чтобы перейти к выбору направления." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"ЭКОНОМИКА БАКАЛАВРИАТ", file=botlogfile)
        botlogfile.close()

    elif call.data == '12' :
        bot.send_message(call.message.chat.id, "ПРИКЛАДНАЯ ИНФОРМАТИКА") 
        PR1 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/PR/пр1.PNG', 'rb')
        bot.send_photo(call.message.chat.id, PR1)
        PR2 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/PR/пр2.PNG', 'rb')
        bot.send_photo(call.message.chat.id, PR2)
        PR3 = open('/usr/local/sbin/venvs/telebot/body//bakalavr/PR/пр3.PNG', 'rb')
        bot.send_photo(call.message.chat.id, PR3)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back1"))
        bot.send_message(call.message.chat.id, text= " Выбери пункт назад, чтобы перейти к выбору направления." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"ПРИКЛАДНАЯ ИНФОРМАТИКА БАКАЛАВРИАТ", file=botlogfile)
        botlogfile.close()

#магистратура 2 кол
    elif call.data == '13' :
        bot.send_message(call.message.chat.id, "ЭКОНОМИКА") 
        AK11 = open('/usr/local/sbin/venvs/telebot/body/magistr/AK/эк11.PNG', 'rb')
        bot.send_photo(call.message.chat.id, AK11)
        AK11 = open('/usr/local/sbin/venvs/telebot/body/magistr/AK/эк11.PNG', 'rb')
        bot.send_photo(call.message.chat.id, AK11)
        AK11 = open('/usr/local/sbin/venvs/telebot/body/magistr/AK/эк11.PNG', 'rb')
        bot.send_photo(call.message.chat.id, AK11)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back2"))
        bot.send_message(call.message.chat.id, text= " Выбери пункт назад, чтобы перейти к выбору программы." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"ЭКОНОМИКА магистратуры", file=botlogfile)
        botlogfile.close()

    elif call.data == '14' :
        bot.send_message(call.message.chat.id, "ТОРГОВОЕ ДЕЛО") 
        TD11 = open('/usr/local/sbin/venvs/telebot/body/magistr/TD/тд1.PNG', 'rb')
        bot.send_photo(call.message.chat.id, TD11)
        TD12 = open('/usr/local/sbin/venvs/telebot/body/magistr/TD/тд2.PNG', 'rb')
        bot.send_photo(call.message.chat.id, TD12)
        TD13 = open('/usr/local/sbin/venvs/telebot/body/magistr/TD/тд3.PNG', 'rb')
        bot.send_photo(call.message.chat.id, TD13)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back2"))
        bot.send_message(call.message.chat.id, text= "Выбери пункт назад, чтобы перейти к выбору программы." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"ТОРГОВОЕ ДЕЛО магистратуры", file=botlogfile)
        botlogfile.close()

    elif call.data == '15' :
        bot.send_message(call.message.chat.id, "МЕНЕДЖМЕНТ") 
        MN11 = open('/usr/local/sbin/venvs/telebot/body/magistr/MN/мн1.PNG', 'rb')
        bot.send_photo(call.message.chat.id, MN11)
        MN12 = open('/usr/local/sbin/venvs/telebot/body/magistr/MN/мн2.PNG', 'rb')
        bot.send_photo(call.message.chat.id, MN12)
        MN13 = open('/usr/local/sbin/venvs/telebot/body/magistr/MN/мн3.PNG', 'rb')
        bot.send_photo(call.message.chat.id, MN13)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back2"))
        bot.send_message(call.message.chat.id, text= "Выбери пункт назад, чтобы перейти к выбору программы." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"МЕНЕДЖМЕНТ магистратуры", file=botlogfile)
        botlogfile.close()

#tto картинки на сайте кол 3
    elif call.data == '16' :
        bot.send_message(call.message.chat.id, "БАНКОВСКОЕ ДЕЛО") 
        SBD31 = open('/usr/local/sbin/venvs/telebot/body/SPO/BD/бд31.png', 'rb')
        bot.send_photo(call.message.chat.id, SBD31)
        SBD1 = open('/usr/local/sbin/venvs/telebot/body/SPO/BD/бд1.png', 'rb')
        bot.send_photo(call.message.chat.id, SBD1)
        SBD2 = open('/usr/local/sbin/venvs/telebot/body/SPO/BD/бд2.png', 'rb')
        bot.send_photo(call.message.chat.id, SBD2)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back3"))
        bot.send_message(call.message.chat.id,text= "Выбери пункт назад, чтобы перейти к выбору специальности." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"БАНКОВСКОЕ ДЕЛО СПО", file=botlogfile)
        botlogfile.close()

    elif call.data == '17' :
        bot.send_message(call.message.chat.id, "СТРАХОВОЕ ДЕЛО") 
        SSD31 = open('/usr/local/sbin/venvs/telebot/body/SPO/SD/сд31.png', 'rb')
        bot.send_photo(call.message.chat.id, SSD31)
        SSD1 = open('/usr/local/sbin/venvs/telebot/body/SPO/SD/сд1.png', 'rb')
        bot.send_photo(call.message.chat.id, SSD1)
        SSD2 = open('/usr/local/sbin/venvs/telebot/body/SPO/SD/сд2.png', 'rb')
        bot.send_photo(call.message.chat.id, SSD2)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back3"))
        bot.send_message(call.message.chat.id,text= "Выбери пункт назад, чтобы перейти к выбору специальности." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"СТРАХОВОЕ ДЕЛО СПО", file=botlogfile)
        botlogfile.close()

    elif call.data == '18' :
        bot.send_message(call.message.chat.id, "ТОВАРОВЕДЕНИЕ И ЭКСПЕРТИЗА КАЧЕСТВА ПОТРЕБИТЕЛЬСКИХ ТОВАРОВ") 
        STV31 = open('/usr/local/sbin/venvs/telebot/body/SPO/TV/тв31.png', 'rb')
        bot.send_photo(call.message.chat.id, STV31)
        STV1 = open('/usr/local/sbin/venvs/telebot/body/SPO/TV/тв1.png', 'rb')
        bot.send_photo(call.message.chat.id, STV1)
        STV2 = open('/usr/local/sbin/venvs/telebot/body/SPO/TV/тв2.png', 'rb')
        bot.send_photo(call.message.chat.id, STV2)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back3"))
        bot.send_message(call.message.chat.id,text= " Выбери пункт назад, чтобы перейти к выбору специальности." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"ТОВАРОВЕДЕНИЕ И ЭКСПЕРТИЗА КАЧЕСТВА ПОТРЕБИТЕЛЬСКИХ ТОВАРОВ СПО", file=botlogfile)
        botlogfile.close()

    elif call.data == '19' :
        bot.send_message(call.message.chat.id, "ЭКОНОМИКА И БУХГАЛТЕРСКИЙ УЧЁТ (ПО ОТРАСЛЯМ)")
        SAK31 = open('/usr/local/sbin/venvs/telebot/body/SPO/AK/эк31.png', 'rb')
        bot.send_photo(call.message.chat.id, SAK31) 
        SAK1 = open('/usr/local/sbin/venvs/telebot/body/SPO/AK/эк1.png', 'rb')
        bot.send_photo(call.message.chat.id, SAK1) 
        SAK2 = open('/usr/local/sbin/venvs/telebot/body/SPO/AK/эк2.png', 'rb')
        bot.send_photo(call.message.chat.id, SAK2) 
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back3"))
        bot.send_message(call.message.chat.id,text= "Выбери пункт назад, чтобы перейти к выбору специальности." , reply_markup=markup) 
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"ЭКОНОМИКА И БУХГАЛТЕРСКИЙ УЧЁТ (ПО ОТРАСЛЯМ) СПО", file=botlogfile)
        botlogfile.close()

    elif call.data == '20' :
        bot.send_message(call.message.chat.id, "ПРОГРАММИРОВАНИЕ И ИНФОРМАЦИОННЫЕ СИСТЕМЫ") 
        SPR1 = open('/usr/local/sbin/venvs/telebot/body/SPO/PR/пр1.png', 'rb')
        bot.send_photo(call.message.chat.id, SPR1) 
        SPR2 = open('/usr/local/sbin/venvs/telebot/body/SPO/PR/пр2.png', 'rb')
        bot.send_photo(call.message.chat.id, SPR2) 
        SPR3 = open('/usr/local/sbin/venvs/telebot/body/SPO/PR/пр3.png', 'rb')
        bot.send_photo(call.message.chat.id, SPR3) 
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back3"))
        bot.send_message(call.message.chat.id,text= "Выбери пункт назад, чтобы перейти к выбору специальности." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M ") + call.message.from_user.first_name, call.message.from_user.id,"ПРОГРАММИРОВАНИЕ И ИНФОРМАЦИОННЫЕ СИСТЕМЫ СПО", file=botlogfile)
        botlogfile.close()

    elif call.data == '21' :
        bot.send_message(call.message.chat.id, "ПОВАРСКОЕ ДЕЛО") 
        SPD1 = open('/usr/local/sbin/venvs/telebot/body/SPO/PD/пд1.png', 'rb')
        bot.send_photo(call.message.chat.id, SPD1)
        SPD2 = open('/usr/local/sbin/venvs/telebot/body/SPO/PD/пд2.png', 'rb')
        bot.send_photo(call.message.chat.id, SPD2)
        SPD3 = open('/usr/local/sbin/venvs/telebot/body/SPO/PD/пд3.png', 'rb')
        bot.send_photo(call.message.chat.id, SPD3)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back3"))
        bot.send_message(call.message.chat.id,text= "Выбери пункт назад, чтобы перейти к выбору специальности." , reply_markup=markup)
        dtn = datetime.datetime.now()
        botlogfile = open('TestBot.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M") + call.message.from_user.first_name, call.message.from_user.id,"ПОВАРСКОЕ ДЕЛО СПО", file=botlogfile)
        botlogfile.close()

    elif call.data == 'back' :
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Направления бакалавриата', callback_data=1))
        markup.add(telebot.types.InlineKeyboardButton(text='Программы магистратуры', callback_data=2))
        markup.add(telebot.types.InlineKeyboardButton(text='Специальности СПО', callback_data=3))
        markup.add(telebot.types.InlineKeyboardButton(text='Подача документов', callback_data=4))
        markup.add(telebot.types.InlineKeyboardButton(text='Сроки приёма на ВО', callback_data=5))
        markup.add(telebot.types.InlineKeyboardButton(text='Сроки приёма на СПО', callback_data=6))
        markup.add(telebot.types.InlineKeyboardButton(text='Назад в меню', callback_data=22))
        bot.send_message(call.message.chat.id, text="Поступление в РЭУ", reply_markup=markup) 
    elif call.data == 'back1' :
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Менеджмент ', callback_data=7))
        markup.add(telebot.types.InlineKeyboardButton(text='Товароведение', callback_data=8))            
        markup.add(telebot.types.InlineKeyboardButton(text='Технология продукции и орг. обществ. питания', callback_data=9))
        markup.add(telebot.types.InlineKeyboardButton(text='Торговое дело', callback_data=10))
        markup.add(telebot.types.InlineKeyboardButton(text='Экономика', callback_data=11))
        markup.add(telebot.types.InlineKeyboardButton(text='Прикладная информатика ', callback_data=12))
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back"))
        bot.send_message(call.message.chat.id, text="Направления бакалавриата", reply_markup=markup)
    elif call.data == 'back2' :
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Экономика ', callback_data=13))
        markup.add(telebot.types.InlineKeyboardButton(text='Менеджмент ', callback_data=14))
        markup.add(telebot.types.InlineKeyboardButton(text='Торговое дело ', callback_data=15))
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back"))
        bot.send_message(call.message.chat.id, text="Программы магистратуры", reply_markup=markup)
    elif call.data == 'back3' :
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Банковское дело', callback_data=16))
        markup.add(telebot.types.InlineKeyboardButton(text='Страховое дело', callback_data=17))
        markup.add(telebot.types.InlineKeyboardButton(text='Товароведение и экспертиза кач-ва потр. тов.', callback_data=18))
        markup.add(telebot.types.InlineKeyboardButton(text='Экономика и бух. учёт', callback_data=19))
        markup.add(telebot.types.InlineKeyboardButton(text='Поварское дело', callback_data=21))
        bot.send_message(call.message.chat.id, text="Торгово-технологическое отделение", reply_markup=markup)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Программирование и информационные системы', callback_data=20))
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data="back"))
        bot.send_message(call.message.chat.id, text="Информационно-коммуникативные технологии", reply_markup=markup)
    elif call.data == '22' :
        bot.send_message(call.message.chat.id, call.message.chat.first_name +", выбери одну из опций в меню, чтобы узнать необходимую информацию.")
    jls_extract_var = bot
bot.polling()
 

