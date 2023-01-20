from bale import Bot, Chat, InlineKeyboard, Keyboard, ChatType, Message, EventType, Components, User, CallbackQuery, RemoveComponents
import sqlite3

id = 1
document = open("database/ban.txt", "r")
listtt = []
l = document.readlines()
for i in l:
    listtt.append(int(i))
    
async def admin(message, bot, is_logined, is_taklif, menu):
    global bots
    bots = bot
    if message.author.user_id in listtt and  message.content in ["/start", "📎 اپدیت ربات", "خانه"]:
            await message.reply("شما از استفاده از بات منع شده اید",

            components=
                Components(keyboards= [Keyboard("غلط کردم")]))
    elif message.author.user_id == id and message.content in ["/start", "📎 اپدیت ربات", "خانه"]:
        await message.reply('''
        سلام به ربات تجارت علم نوین خوش اومدی اگه تو هم از تکالیف زیاد و ظالمانه استادان رنج میبرید میتونید به
        راحتی تکلیف های  نوشته شده رو به اشتراک بزارید و تکالیفی که نتونستید رو از بچه های دیگر دریافت کنید
        """""به دلیل سرعت بسیار بالای نت ممکن است برخی مواقع بات در ارسال فایل با کمی کندی مواجه شود ، لطفا بعد از مدت کوتاهی مجدد اقدام کنید """
        #اینجانب هیچ مسیولیتی نسب به طرز استفاده این ربات ندارد .''',

                    components=
                        menu)

    elif message.content in ["/start", "📎 اپدیت ربات", "خانه"]:
        ac = 0
        connection = sqlite3.connect("database/user.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM users")
        s = cursor.fetchall()
        for i in s:
            if message.author.user_id == i[0]:
                ac += 1
                if i[2] == "Yes":
                    is_logined()
                    await message.reply('''
*سلام و وقت بخیر به شما دوست عزیز*
به ربات تجارت علم نوین خوش اومدید .
با خیال راحت و به سادگی جزوات و نمونه سوالاتتون رو با دوستاتون به اشتراک بزارید و خودتون هم از اونها استفاده کنید
بدون هیچ دردسری و براحتی فقط با چند کلیک !
بهتره با استفاده از دکمه های زیر کارت رو شروع کنی 💚.
اگر مشکلی داشتید یا از طریق ارسال تیکت با ما در ارتباط باشید یا ایدی @im_not_amin''',

			components=
				menu)

                if i[2] == "None":
                    await message.reply('''
درخواست شما هنور بررسی نشده است 😒''')

                if i[2] == "No":

                    await message.reply('''
درخواست شما رد شده است ❌''',)

                if i[3] == "Yes":
                    is_taklif()

        if ac == 0:
            await message.reply("قبل از ادامه استفاده از ربات بر روی دکمه ساخت اکانت کلیک کنید", components = Components(inline_keyboards= [InlineKeyboard("ساخت اکانت", callback_data = "account")]))
                

    


    if message.author.user_id == id and message.content in ["📝 بن کردن مخاطب"]:
        def check(m):
            return message.author == m.author	
        


        await message.reply("ایدی عددی مخاطب را وارد  کنید")
        s = await bot.wait_for(event_name= "message", check = check)
        l = s.content

        with open("database/ban.txt", "a", encoding="utf-8")as f:
            f.write(f"{l}" )

        await message.reply("کاربر با موفقیت بن شد ")


async def register(message):
    ac = 0
    connection = sqlite3.connect("database/user.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    s = cursor.fetchall()
    for i in s:
        if i[0] == message.user_id:
            ac += 1

    if ac == 0:
        cursor.execute(f"INSERT INTO users VALUES ('{message.user_id}', '{message.first_name}', 'None', 'No' , 1, 'Yes')")
    connection.commit()
    connection.close()



async def check_logined(message, bot, is_logined, is_taklif, not_logined, not_taklif):
    ac = 0
    connection = sqlite3.connect("database/user.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users")
    s = cursor.fetchall()
    for i in s:
        if message.author.user_id == i[0]:
            ac += 1

            if i[3] == "Yes":
                    is_taklif()
            
            else:
                not_taklif()

            if i[2] == "Yes":
                is_logined()

            else:
                not_logined()

            if i[2] == "None":
                await message.reply('''
درخواست شما هنور بررسی نشده است 😒''')

            if i[2] == "No":

                await message.reply('''
درخواست شما رد شده است ❌''',)
    if ac == 0:
        await message.reply("قبل از ادامه استفاده از ربات بر روی دکمه ساخت اکانت کلیک کنید", components = Components(inline_keyboards= [InlineKeyboard("ساخت اکانت", callback_data = "account")]))
            
async def check_logined2(message, bot, is_logined, is_taklif, not_logined, not_taklif):
    ac = 0
    connection = sqlite3.connect("database/user.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users")
    s = cursor.fetchall()
    for i in s:
        if message.user.user_id == i[0]:
            ac += 1
            if i[3] == "Yes":
                is_taklif()
            
            else:
                not_taklif()

            if i[2] == "Yes":
                is_logined()

            else:
                not_logined()

            if i[2] == "None":
                await message.message.reply('''
درخواست شما هنور بررسی نشده است 😒''')

            if i[2] == "No":

                await message.message.reply('''
درخواست شما رد شده است ❌''',)
    if ac == 0:
        await message.message.reply("قبل از ادامه استفاده از ربات بر روی دکمه ساخت اکانت کلیک کنید", components = Components(inline_keyboards= [InlineKeyboard("ساخت اکانت", callback_data = "account")]))
            

def get_id():
    ac = []
    connection = sqlite3.connect("database/user.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users")
    s = cursor.fetchall()
    for i in s:
        ac.append(i[0])
    return ac


def get_notif(c):
    connection = sqlite3.connect("database/user.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users")
    s = cursor.fetchall()
    for i in s:
        if i[5] == "Yes" and i[0] == c.user_id:
            print("e")
            return True

        elif i[5] == "No" and i[0] ==  c.user_id:
            return False

def get_notif_id(id):
    connection = sqlite3.connect("database/user.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users")
    s = cursor.fetchall()
    for i in s:
        if i[5] == "Yes" and i[0] == id:
            print("e")
            return True

        elif i[5] == "No" and i[0] ==  id:
            return False


