import bale, asyncio
from colorama import init, Fore, Back, Style

class ADMINMessageManger:
    def __init__(self, db, bot):
        self.db = db
        self.bot = bot

    async def check_msg(self, mg : bale.Message):
        if mg.content.startswith("/sendall"):
            for i in self.db.get_ids():
                if self.db.get_notif_id(i):
                    try:
                        ss = bale.Chat(i, title = i, username = i, first_name=i, last_name=i, _type = "pv")
                        await self.bot.send_message(ss, '''
کلی جزوه و نمونه سوال ریاضی جالب جمع اوری و اپلود شد ، یه نگاه بنداز 😉

        با /start شروع کنید.
        ''')    
                    except:
                        try:
                            print(Fore.WHITE + f"ERROR SENDING MESSAGE TO {ss.username}")

                        except:
                            print(Fore.WHITE +f"CANT FIND CHAT ID USERNAME WITH {i}")

        if mg.content.startswith("/reload"):
            await mg.reply("بات در حال ریلود است 😉")
            await asyncio.sleep(5)
            self.db.close_database()
            await self.bot.close()

    