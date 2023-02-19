import bale
from user import Users
from constants import START_TEXT, MAKE_ACCOUNT_TEXT, RULES
from buttons import ButtonManager
from database.database import Database
from updates.messages import MessageManger
from updates.callback import CallbackManager
from updates.updater import CustomUpdater
from adminmessag import ADMINMessageManger
from debug import Debug

v1 = "294509772:aENXCNwTn92WItaohFVRgaPMiCQnNczwAbJKPcHP"
v2 = "754105565:qqpY8kOFoyhldX6Qi1J2zcd2l9GjpjYEZu36ZHt2"

class BaleBot(bale.Bot):
    def __init__(self):
        super().__init__(token= "754105565:qqpY8kOFoyhldX6Qi1J2zcd2l9GjpjYEZu36ZHt2", updater = CustomUpdater)
        self.bot = self
        self.Debuger = Debug()
        self.database = Database(self.Debuger)
        self.cm = CallbackManager()
        self.user_manager = Users(self.database)
        self.button_manager = ButtonManager(self.user_manager, self.Debuger)
        self.mg = MessageManger(self.button_manager, self.bot, self.database)
        self.Amg = ADMINMessageManger(self.database, self.bot)
        self.add_event(bale.EventType.READY, self.on_ready)
        self.add_event(bale.EventType.MESSAGE, self.on_message)
        self.add_event(bale.EventType.CALLBACK, self.on_callback)
        self.add_event(bale.EventType.UPDATE, self.on_update)
    async def on_ready(self):
        self.Debuger.started()

    async def on_message(self,  message: bale.Message):
        try:
            self.users_id = message.author.user_id
        except Exception:
            self.Debuger.print_errors("GETTING USER ID IN ON_MESSAGE", "NONE")

        if message.content in ["/start", "خانه", "📎 اپدیت ربات"]:
            self.database.open_database()
            if self.user_manager.is_active(self.users_id):
                if self.user_manager.is_admin(self.users_id):
                    await message.reply(START_TEXT, components=self.button_manager.return_admin())
                else:
                    await message.reply(START_TEXT, components=self.button_manager.return_menu())
            else:
                await message.reply(MAKE_ACCOUNT_TEXT, components= self.button_manager.return_registers())
        else:

            try:
                await self.mg.check_message(message)

            except Exception:
                try:
                    self.Debuger.print_errors("REPLY MESSAGE (MAY BE INTERNAL)", message.author.username)

                except Exception:
                    self.Debuger.print_errors("CANT FIND AUTHOR ID", message.author.user_id)


            try:
                if message.content.startswith("/"):
                    self.database.open_database()
                    if self.user_manager.is_admin(message.author.user_id):
                        await self.Amg.check_msg(message)
                    self.database.close_database()

            except Exception:
                self.Debuger.print_sent_file(message)
                
            
            if message.content:
                self.database.add_log(message)


            else:
                self.Debuger.print_sent_file(message)
        




    async def on_update(self, update):
        try:
            self.Debuger.print_update(update)
        except Exception:
            self.Debuger.print_errors("ERROR GETTING UPDATE (MAY BE INTERNAL)", "NONE")

    async def on_callback(self, callback: bale.CallbackQuery):
        try:
            if callback.data == "register":
                message = self.user_manager.register(callback)
                await callback.message.reply(message)

            elif callback.data == "rule":
                await callback.message.reply(RULES)
            

            elif callback.data =="notifchange":
                
                self.database.change_notif(callback.user)
                await callback.message.reply("عملیات انجام شد")


            else:
                await self.cm.get_files(self.mg.path, callback)

        except Exception:
            try:
                user = callback.user.username
                self.Debuger.print_errors("CALLBACK ERROR MAY BE INTERNAL", user)
            except Exception:
                self.Debuger.print_errors("CALLBACK USERNAME NOT FOUND", "NONE")

            
bot = BaleBot()
bot.run()
