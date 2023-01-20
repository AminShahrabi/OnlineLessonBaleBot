from bale import Bot, Chat, InlineKeyboard, Keyboard, Message, EventType, Components, CallbackQuery


bot = Bot("294509772:QXsPKzqg5VLlo1iqihInPHUhXwjQKVRoRejmPLgH")
import admin
logined = False
taklif = False
filetype = ""
timer = 1
nohom = "nohom/"
jozve = "jozvat/"
soal = "soal/"
fiziksim = "fiziksim/"
defaei = "defaei/"
takif = "takif/"
zist = "zist.txt"
ghoran = "ghoran.txt"
azmayesh = "azmayesh.txt"



doros =  Components(keyboards= [ 
                [Keyboard("اجتماعی"),Keyboard("دفاعی"),Keyboard("فیزیک شیمی")],
                [Keyboard("عربی"), Keyboard("قرآن"), Keyboard("زیست")],
                [Keyboard("ادبیات"), Keyboard("دفاعی"), Keyboard("آزمایشگاه")],
                [Keyboard("رایانه"), Keyboard("حساب"), Keyboard("خانه")],
                    ])
    
@bot.listen(EventType.MESSAGE)
# async def when_receive_message(message: Message):
#     global filetype, path



#     if not  message.content in ["/start", "📎 اپدیت ربات", "خانه"]:
#         await admin.check_logined(message, bot, is_logined, is_taklif, not_logined, not_taklif)
#     with open("database/log.txt", "a", encoding="utf-8") as f:
#         if message.document == None:
#             f.write("\n" + message.content + message.author.username)
#         else:
#             pass

#         # start message




#     await admin.admin(message, bot, is_logined, is_taklif, main_menu)

        
                
            
#     def check(m):
#         return message.author == m.author	
	
#     if logined:
#         if message.content == "📝 ارسال فایل":
#             if taklif:
#                 await message.reply("نوع فایل مورد نظر را انتخاب کنید",  

#                 components=
#                 Components(keyboards= [ 
#                     [Keyboard("جزوه"),Keyboard("نمونه سوال"),Keyboard("تکلیف")],
#                     [Keyboard("خانه")]

#                         ]))

#             else:
#                 await message.reply("نوع فایل مورد نظر را انتخاب کنید",  

#                 components=
#                 Components(keyboards= [ 
#                     [Keyboard("جزوه"),Keyboard("نمونه سوال")],
#                     [Keyboard("خانه")]

#                         ]))
#         if message.content == "جزوه":
#             await message.reply("لطفا درس مورد نظر را ارسال کنید",  

#             components= doros)
           



#             s = await bot.wait_for(event_name= "message", check = check)
#             if s.content == "خانه":
#                 return

#             lesson = s.content



#             await message.reply('''لطفا عنوان جزوه مورد نظر را ارسال کنید
#     یک عنوان متناسب انتخاب کنید 😉
#     مثال های مناسب 📗
#     جزوه عربی درس 2
#     جزوه ریاضی مبحث توان
#     و .....''', components=        Components(keyboards= [ Keyboard("خانه")

#                     ]))

#             s = await bot.wait_for(event_name= "message", check = check)
#             onvan = s.content

#             if onvan == "خانه":
#                 return
                
#             await message.reply('''
#     لطفا فایل مورد نظر را ارسال کنید 😎
#     فایل های پشتیبانی شده : هرفايلي که به عنوان داکیومنت (فایل بله ) ارسال شود ✔''')
#             s = await bot.wait_for(event_name= "message", check = check)
#             try:
#                 d = s.document.file_id

#                 with open("database/jozve.txt", "a", encoding="utf-8")as f:
#                     f.write(f"\n{d} + {lesson +' ' + onvan}" )
#             except:
#                 await message.reply('''
#     یک اخطار برای شما ثبت شد لطفا از مسخره بازی دست بردارید''')
#                 return


#             await message.reply("ممنون از همکاری شما بعد از بررسی صحت جزوه شما شما به ربات اضافه خواهد شد ",  

#                 components=
#                     main_menu)
        
#         if message.content == "تکلیف":
#             if taklif:
#                 await message.reply("لطفا درس مورد نظر را ارسال کنید",  

#                 components=
#                 doros)



#                 s = await bot.wait_for(event_name= "message", check = check)
#                 if s.content == "خانه":
#                     return

#                 lesson = s.content



#                 await message.reply('''لطفا عنوان تکلیف مورد نظر را ارسال کنید
#         یک عنوان متناسب انتخاب کنید 😉
#         مثال های مناسب 📗
#         تکلیف عربی درس 2
#         و .....''', components=        Components(keyboards= [ Keyboard("خانه")

#                         ]))

#                 s = await bot.wait_for(event_name= "message", check = check)
#                 onvan = s.content

#                 if onvan == "خانه":
#                     return
                    
#                 await message.reply('''
#         لطفا فایل مورد نظر را ارسال کنید 😎
#         فایل های پشتیبانی شده : هرفايلي که به عنوان داکیومنت (فایل بله ) ارسال شود ✔''')
#                 s = await bot.wait_for(event_name= "message", check = check)
#                 try:
#                     d = s.document.file_id

#                     with open("database/taklif.txt", "a", encoding="utf-8")as f:
#                         f.write(f"\n{d} + {lesson +' ' + onvan}" )
#                 except:
#                     await message.reply('''
#         یک اخطار برای شما ثبت شد لطفا از مسخره بازی دست بردارید''')
#                     return


#                 await message.reply("ممنون از همکاری شما بعد از بررسی صحت جزوه شما شما به ربات اضافه خواهد شد ",  

#                     components=
#                         main_menu)

#             else:
#                 await message.reply("شما به این بخش دسترسی ندارید ❌")


#         if message.content == "نمونه سوال":
#             await message.reply("لطفا درس مورد نظر را ارسال کنید",  

#             components=
#             doros)



#             s = await bot.wait_for(event_name= "message", check = check)
#             if s.content == "خانه":
#                 return

#             lesson = s.content



#             await message.reply('''لطفا عنوان نمونه سوال مورد نظر را ارسال کنید
#     یک عنوان متناسب انتخاب کنید 😉
#     مثال های مناسب 📗
#     20 تست عربی درس 5
#     امتحان میان نوبت ریاضی نهم
#     و .....''', components=        Components(keyboards= [ Keyboard("خانه")

#                     ]))

#             s = await bot.wait_for(event_name= "message", check = check)
#             onvan = s.content

#             if onvan == "خانه":
#                 return
#             try:
#                 await message.reply('''
#         لطفا فایل مورد نظر را ارسال کنید 😎
#         فایل های پشتیبانی شده : هرفايلي که به عنوان داکیومنت (فایل بله ) ارسال شود ✔''')
#                 s = await bot.wait_for(event_name= "message", check = check)
#                 try:
#                     d = s.document.file_id

#                     with open("database/nemone_soal.txt", "a", encoding="utf-8")as f:
#                         f.write(f"\n{d} + {lesson +' ' + onvan}" )
#                 except:
#                     await message.reply('''
#         یک اخطار برای شما ثبت شد لطفا از مسخره بازی دست بردارید''')
#                     return

#             except Exception as e:
#                 print(e)


#             await message.reply("ممنون از همکاری شما بعد از بررسی صحت جزوه شما شما به ربات اضافه خواهد شد ",  

#                 components=
#                         main_menu)
                
  

#         if message.content == "📃 نمونه سوالات و جزوات":
#             if taklif:
#                 await message.reply("نوع فایل مورد نظر را انتخاب کنید",  

#                 components=
#                 Components(keyboards= [ 
#                     [Keyboard("جزوات"),Keyboard("نمونه سوالات"),Keyboard("تکالیف")], 
#                     [Keyboard("خانه")],

#                         ]))

#             else:
#                 await message.reply("نوع فایل مورد نظر را انتخاب کنید",  

#                 components=
#                 Components(keyboards= [ 
#                     [Keyboard("جزوات"),Keyboard("نمونه سوالات")], 
#                     [Keyboard("خانه")],

#                         ]))


                        
#         if message.content == "تکالیف":
#             if taklif:
#                 filetype ="taklif"
#                 keyboardbuttons = []
#                 if onvan == "دفاعی":
#                     path = nohom + takif + "defaei.txt"

#                 elif onvan == "فیزیک شیمی":
#                     path = nohom + takif + "fish.txt"

#                 elif onvan == "taklif":
#                     path = nohom + takif + "ejtema.txt"


#                 else:
#                     path = "database/taklif.txt"

#                 with open(path, "r", encoding="utf-8")as f:
#                     l = f.readlines()
                
#                     for i in l:
#                         s = i.split("+")
#                         keyboardbuttons.append(InlineKeyboard(s[1], callback_data=s[0]))

#                 if keyboardbuttons == []:
#                     await message.reply('''تکلیفی موجود نیست''')
#                 else:  
#                     await message.reply('''تکالیف  :''',
                        
#                         components=
#                             Components(inline_keyboards= keyboardbuttons)

                        
#                     )

                        

#             else:
#                 await message.reply("شما به این بخش دسترسی ندارید ❌")

#         if message.content == "جزوات":
            
#             await message.reply("لطفا درس مورد نظر را ارسال کنید",  
#             components= doros)

#             s = await bot.wait_for(event_name= "message")
#             onvan = s.content
            
#             if onvan == "دفاعی":
#                 path = nohom + jozve + "defaei.txt"

#             elif onvan == "فیزیک شیمی":
#                 path = nohom + jozve + "fish.txt"

#             elif onvan == "زیست":
#                 path = nohom + jozve + zist

#             elif onvan == "ادبیات":
#                 path = nohom + jozve + "adabi.txt"

#             elif onvan == "قرآن":
#                 path = nohom + jozve + ghoran

#             elif onvan == "آزمایشگاه":
#                 path = nohom + jozve + azmayesh

#             else:
#                 path = "database/jozve.txt"




#             filetype = "jozve"
#             keyboardbuttons = []
#             with open(path, "r", encoding="utf-8")as f:
#                 l = f.readlines()
#                 for i in l:
#                     s = i.split("+")
#                     keyboardbuttons.append(InlineKeyboard(s[1], callback_data=s[0]))

#             if keyboardbuttons == []:
#                 await message.reply('''جزوه ای موجود نیست''')
#             else:  
#                 await message.reply('''جزوات : ''',
                    
#                     components=
#                         Components(inline_keyboards= keyboardbuttons)

                    
#                 ) 



#             await message.reply('''*به خانه بازگشتید*''',
                    
#                     components=
#                         main_menu

                    
#                 ) 

#         if message.content == "نمونه سوالات":
            
#             await message.reply("لطفا درس مورد نظر را ارسال کنید",  
#             components= doros)

#             s = await bot.wait_for(event_name= "message")
#             onvan = s.content
                    
#             if onvan == "دفاعی":
#                 path = nohom + soal + "defaei.txt"

#             elif onvan == "فیزیک شیمی":
#                 path = nohom + soal + "fish.txt"

#             elif onvan == "اجتماعی":
#                 path = nohom + soal + "ejtema.txt"

#             elif onvan == "ادبیات":
#                 path = nohom + soal + "adabi.txt"

#             elif onvan == "زیست":
#                 path = nohom + soal + zist

#             elif onvan == "قرآن":
#                 path = nohom + soal + ghoran

#             elif onvan == "آزمایشگاه":
#                 path = nohom + soal + azmayesh


#             else:
#                 path = "database/nemone_soal.txt"

#             filetype = "soal"

#             keyboardbuttons = []
#             with open(path, "r", encoding="utf-8")as f:
#                 l = f.readlines()
#                 for i in l:
#                     s = i.split("+")
#                     keyboardbuttons.append(InlineKeyboard(s[1], callback_data=s[0]))

    

#             if keyboardbuttons == []:
#                 await message.reply('''نمونه سوالی ای موجود نیست''')
#             else:  
#                 await message.reply('''نمونه سوالات : ''',
                    
#                     components=
#                         Components(inline_keyboards= keyboardbuttons)

                    
#                 )


#             await message.reply('''*به خانه بازگشتید*''',
                    
#                     components=
#                         main_menu

                    
#                 ) 

#         if message.content == "📋 تنظیمات":

#             if admin.get_notif(message.author) == True:
#                 s = "روشن"

#             if admin.get_notif(message.author) == False:
#                 s = "خاموش"

#             await message.reply(
#             f'''
#     نام شما : {message.author.first_name}
#     نام کاربری : {message.author.username}
#     ایدی عددی شما: {message.author.user_id}

#             ''',
#             components=
#             Components(inline_keyboards= [InlineKeyboard(f"اعلان ها : {s}", callback_data = "notifchange")
#             , InlineKeyboard(f"قوانین", callback_data = "rule")]))


#         if message.content == "📁 ارسال تیکت":
#             await message.reply(
#             f'''لطفا پیام خودتان را برای ارسال به ادمین ارسال کنید 😇
#             ''')
#             s = await bot.wait_for(event_name= "message")
#             onvan = s.content

#             with open("database/tiket.txt", "a", encoding="utf-8")as f:
#                 f.write(onvan)
                
#         if message.content == "📚 درخواست":
#             await message.reply("نوع عملیات مورد نظر را انتخاب کنید 📋",  

#                 components=
#                 Components(keyboards= [ 
#                     [Keyboard("درخواست ها"),Keyboard("ارسال درخواست")],
#                     [Keyboard("خانه")]

#                         ]))




#         if message.content == "درخواست ها":
#             keyboardbuttons = ''''''
#             with open("database/wanted.txt", "r", encoding="utf-8")as f:
#                 l = f.readlines()
#                 for i in l:
#                     keyboardbuttons += "\n" + i

#             if keyboardbuttons == '''''':
#                 await message.reply('''درخواستی موجود نیست''')
#             else:  
#                 await message.reply(f'''درخواست ها :
                
#                 {keyboardbuttons}''')


#         if message.content == "ارسال درخواست":
#                 await message.reply('''
# لطفا متن و توضیحات درخواست خود را بنویسید .  ✔
# برای مثال :
# دوستان کسی جزوه ریاضی فصل جدید رو داره؟ ✋ 
# امکانش هست نمونه سوال اجتماعی بفرستید؟ ✋


# ''',components=        Components(keyboards= [ Keyboard("خانه")

#                     ]))



#                 s = await bot.wait_for(event_name= "message", check = check)
#                 if s.content == "خانه":
#                     return

#                 dar = message.author.username + " : " + s.content
#                 with open("database/wanted.txt", "a", encoding="utf-8")as f:
#                     f.write("\n" + dar )




#                 await message.reply(" 😎 ممنون از همکاری شما درخواست ارسال شد و قابل مشاهده است ",  

#                 components=
#                         main_menu)



                


                

       
        

# @bot.listen(EventType.CALLBACK)
# async def when_receive_callback(callback: CallbackQuery):
#     if callback.data =="account":
#         await callback.message.reply("""
# درخواست شما تا حداکثر 24 ساعت دیگر بررسی و در صورت تایید ربات برای شما قابل استفاده میشود.
# برای بررسی وضیعت تاییدی خودتون میتوانید از دکمه زیر استفاده کنید .
# اگر بر روي وضيعت كليك كرديد و پاسخي نگرفتيد /start بفرستيد""", components = Components(inline_keyboards= [InlineKeyboard("وضیعت اکانت", callback_data = "test")]))

#         await admin.register(callback.user)

#     elif callback.data == "test":
#         await admin.check_logined2(callback, bot, is_logined, is_taklif, not_logined, not_taklif)





@bot.listen(EventType.READY)
async def when_bot_is_ready():
    print(bot.user, "is Ready!")
    await sendall()


async def sendall():
    for i in admin.get_id():
        if admin.get_notif_id(i):
            try:
                ss = Chat(i, title = i, username = i, first_name=i, last_name=i, _type = "pv")
                await bot.send_message(ss, '''
''')
            except Exception as e:
                print(e)


def run():
    bot.run()


def is_logined():
    global logined
    logined = True

def is_taklif():
    global taklif
    taklif = True

def not_logined():
    global logined
    logined = False

def not_taklif():
    global taklif
    taklif = False

run()