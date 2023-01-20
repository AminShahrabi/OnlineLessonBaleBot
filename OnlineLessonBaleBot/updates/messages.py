from email import message
from bale import Components
from sympy import O
from tomlkit import date
from buttons import ButtonManager
from constants import *
from datetime import timedelta, datetime
from constants import *
from colorama import init, Fore, Back, Style

class MessageManger:
    def __init__(self, button, bot, database):
        self.db = database
        self.buttons = button
        self.bot = bot

    async def check_message(self, message):
        m = message.content
        if m == "📃 نمونه سوالات و جزوات":
            await self.jozve_menu(message)
        
        elif m == "📝 ارسال فایل":
            await self.get_send_files(message)

        elif m == "جزوات":
            await self.get_jozve(message)

        elif m == "نمونه سوالات":
            await self.get_nemonesoal(message)

        elif m == "نمونه سوال":
            await self.send_soal(message)

        elif m == "جزوه":
            await self.send_jozve(message)

        elif m == "📁 ارسال تیکت":
            await self.send_ticket(message)

        elif m == "📋 تنظیمات":
            await self.settings(message)

        elif m == "📚 نسخه ربات":
            await self.bot_version(message)




    async def send_jozve(self, message):
        await message.reply("لطفا درس مورد نظر را ارسال کنید",  
        components=
        self.buttons.return_doros())
        s = await self.bot.wait_for(event_name= "message")

        if s.content == "خانه":
            return
        lesson = s.content
        await message.reply('''لطفا عنوان جزوه مورد نظر را ارسال کنید
یک عنوان متناسب انتخاب کنید 😉
مثال های مناسب 📗
 جزوه عربی درس 5
جزوه میان نوبت ریاضی نهم
و .....''', components=self.buttons.home)

        s = await self.bot.wait_for(event_name= "message")
        onvan = s.content

        if onvan == "خانه":
            return

        await message.reply('''
لطفا فایل مورد نظر را ارسال کنید 😎
فایل های پشتیبانی شده : هرفايلي که به عنوان داکیومنت (فایل بله ) ارسال شود ✔''')
        s = await self.bot.wait_for(event_name= "message")
        try:
            d = s.document.file_id

            with open("database/jozve.txt", "a", encoding="utf-8")as f:
                f.write(f"\n{d} + {lesson +' ' + onvan}" )
        except:
            await message.reply(FALSE_FILE)
            return



        await message.reply("😇 ممنون از همکاری شما بعد از بررسی صحت جزوه شما شما به ربات اضافه خواهد شد ",  

            components=
                    self.buttons.return_menu())
    async def send_soal(self, message):
        await message.reply("لطفا درس مورد نظر را ارسال کنید",  
        components=
        self.buttons.return_doros())
        s = await self.bot.wait_for(event_name= "message")

        if s.content == "خانه":
            return
        lesson = s.content
        await message.reply('''لطفا عنوان نمونه سوال مورد نظر را ارسال کنید
یک عنوان متناسب انتخاب کنید 😉
مثال های مناسب 📗
20 تست عربی درس 5
امتحان میان نوبت ریاضی نهم
و .....''', components=self.buttons.home)

        s = await self.bot.wait_for(event_name= "message")
        onvan = s.content

        if onvan == "خانه":
            return
        await message.reply('''
لطفا فایل مورد نظر را ارسال کنید 😎
فایل های پشتیبانی شده : هرفايلي که به عنوان داکیومنت (فایل بله ) ارسال شود ✔''')
        s = await self.bot.wait_for(event_name= "message")
        try:
            d = s.document.file_id

            with open("database/nemone_soal.txt", "a", encoding="utf-8")as f:
                f.write(f"\n{d} + {lesson +' ' + onvan}" )
        except:
            await message.reply(FALSE_FILE)
            return




        await message.reply("😇 ممنون از همکاری شما بعد از بررسی صحت نمونه سوال شما به ربات اضافه خواهد شد ",  

            components=
                    self.buttons.return_menu())

    async def jozve_menu(self, message):
        # if taklif:
            # await message.reply(" نوع فایل مورد نظر را انتخاب کنید 💌",  

            #     components=
            #     Components(keyboards= [ 
            #         [Keyboard("جزوات"),Keyboard("نمونه سوالات"),Keyboard("تکالیف")], 
            #         [Keyboard("خانه")],

            #             ]))

        # else:
            await message.reply("نوع فایل مورد نظر را انتخاب کنید 💌",  
            components= self.buttons.return_choose_file())

    async def get_send_files(self, message):
        # if taklif:
            # await message.reply(" نوع فایل مورد نظر را انتخاب کنید 💌",  

            #     components=
            #     Components(keyboards= [ 
            #         [Keyboard("جزوات"),Keyboard("نمونه سوالات"),Keyboard("تکالیف")], 
            #         [Keyboard("خانه")],

            #             ]))

        # else:
            await message.reply("نوع فایل مورد نظر را انتخاب کنید 💌",  
            components= self.buttons.return_sends())

    async def get_jozve(self, message):

        await message.reply("لطفا درس مورد نظر را ارسال کنید",  
            components= self.buttons.return_doros())

        s = await self.bot.wait_for(event_name= "message")
        onvan = s.content
        
        if onvan == "دفاعی":
            self.path = NOHOM + JOZVE + DEFAEI

        elif onvan == "فیزیک شیمی":
            self.path = NOHOM + JOZVE + FISH

        elif onvan == "زیست":
            self.path = NOHOM + JOZVE + ZIST

        elif onvan == "ادبیات":
            self.path = NOHOM + JOZVE + ADABI

        elif onvan == "قرآن":
            self.path = NOHOM + JOZVE + GHORAN

        elif onvan == "آزمایشگاه":
            self.path = NOHOM + JOZVE + AZMAYESH

        elif onvan == "حساب":
            self.path = NOHOM + JOZVE + HESAB

        else:
            self.path = "database/jozve.txt"
        
        self.filetype = "jozve"
        self.keys = self.buttons.lessons_buttons(self.path)
        if self.keys != []:
            await message.reply('''
لطفا از لیست برای دریافت فایل انتخاب کنید 😎''', components = Components(inline_keyboards = self.keys))

        else:
            await message.reply('''
متاسفانه هیچ جزوه ای برای این درس موجود نیست 😒
نظرت چیه اولین نفری باشی که جزوت رو ارسال میکنی؟🤩''')



        



        await message.reply('''*به خانه بازگشتید*''',
                
                components=
                    self.buttons.return_menu()

                
            ) 

    async def get_nemonesoal(self, message):
        await message.reply("لطفا درس مورد نظر را ارسال کنید",  
            components= self.buttons.return_doros())

        s = await self.bot.wait_for(event_name= "message")
        onvan = s.content
        
        if onvan == "دفاعی":
            self.path = NOHOM + NEMONESOAL + DEFAEI

        elif onvan == "فیزیک شیمی":
            self.path = NOHOM + NEMONESOAL + FISH

        elif onvan == "زیست":
            self.path = NOHOM + NEMONESOAL + ZIST

        elif onvan == "ادبیات":
            self.path = NOHOM + NEMONESOAL + ADABI

        elif onvan == "قرآن":
            self.path = NOHOM + NEMONESOAL + GHORAN

        elif onvan == "آزمایشگاه":
            self.path = NOHOM + NEMONESOAL + AZMAYESH

        elif onvan == "حساب":
            self.path = NOHOM + NEMONESOAL + HESAB

        else:
            self.path = "database/nemone_soal.txt"
        
        self.filetype = "soal"
        self.keys = self.buttons.lessons_buttons(self.path)
        if self.keys != []:
            await message.reply('''
لطفا از لیست برای دریافت فایل انتخاب کنید 😎''', components = Components(inline_keyboards = self.keys))

        else:
            await message.reply('''
متاسفانه هیچ نمونه سوالی برای این درس موجود نیست 😒
نظرت چیه اولین نفری باشی که جزوت رو ارسال میکنی؟🤩''')



        



        await message.reply('''*به خانه بازگشتید*''',
                
                components=
                    self.buttons.return_menu()

                
            ) 


    async def send_ticket(self, message):
        await message.reply(
        f'''لطفا پیام خودتان را برای ارسال به ادمین ارسال کنید 😇
        ''')
        s = await self.bot.wait_for(event_name= "message")
        onvan = s.content

        self.db.add_ticket(message, onvan)

    async def settings(self, message):
        if self.db.get_notif(message.author) == True:
                s = "روشن"

        if  self.db.get_notif(message.author) == False:
                s = "خاموش"

        await message.reply(
            f'''
    نام شما : {message.author.first_name}
    نام کاربری : {message.author.username}
    ایدی عددی شما: {message.author.user_id}

            ''',
            components=self.buttons.retutn_setting_keys(s)
            )

    async def bot_version(self, m):
        await m.reply(F'''
🔆🔆🔆🔆🔆🔆🔆🔆🔆
نسخه ربات : {VERSION} 
نام ربات : {NAME}
تعداد کاربر : {USERS}
🔆🔆🔆🔆🔆🔆🔆🔆🔆
        ''')
    