from bale import Components, InlineKeyboard
from bale import Keyboard

class ButtonManager:
    def __init__(self, users):
        self.users = users

        self.menu_button = Components(keyboards= [[Keyboard("📝 ارسال فایل"),Keyboard("📃 نمونه سوالات و جزوات")],
                        [Keyboard("📁 ارسال تیکت"), Keyboard("📎 اپدیت ربات")],
                        [Keyboard("📋 تنظیمات"), Keyboard("📚 نسخه")]])

        self.admin_button =  Components(keyboards= [[Keyboard("📝 ارسال فایل"),Keyboard("📃 نمونه سوالات و جزوات")],
                        [Keyboard("📁 ارسال تیکت"), Keyboard("📎 اپدیت ربات")],
                        [Keyboard("📋 تنظیمات"), Keyboard("📚 ادمین هستید")]])
        self.register_button = Components(inline_keyboards = [[InlineKeyboard("ثبت نام", callback_data = "register")]])

        self.choose_file_button = Components(keyboards= [
                    [Keyboard("جزوات"),Keyboard("نمونه سوالات")],
                    [Keyboard("خانه")]])

        self.doros_button = Components(keyboards= [
                [Keyboard("اجتماعی"),Keyboard("دفاعی"),Keyboard("فیزیک شیمی")],
                [Keyboard("عربی"), Keyboard("قرآن"), Keyboard("زیست")],
                [Keyboard("ادبیات"), Keyboard("دفاعی"), Keyboard("آزمایشگاه")],
                [Keyboard("رایانه"), Keyboard("حساب"), Keyboard("خانه")]])
        self.send_menu = Components(keyboards= [
                    [Keyboard("جزوه"),Keyboard("نمونه سوال")],
                    [Keyboard("خانه")]

                        ])

        self.home = Components(keyboards= [ Keyboard("خانه")
                ])


        self.settings_key = None

    def return_admin(self):
        return self.admin_button
            
    def return_menu(self):
        return self.menu_button
    
    def return_registers(self):
        return self.register_button

    def return_choose_file(self):
        return self.choose_file_button

    def return_doros(self):
        return self.doros_button

    def return_sends(self):
        return self.send_menu

    def lessons_buttons(path):
        try:
            keyboardbuttons = []
            with open(path, "r", encoding="utf-8")as f:
                l = f.readlines()
                for i in l:
                    s = i.split("+")
                    keyboardbuttons.append(InlineKeyboard(s[1], callback_data=s[0]))
            return keyboardbuttons

        except Exception:
            print("COUDNT ADD FILE BUTTONS (MAY BE CAUSE OF ENTER)", "")


    def retutn_setting_keys(self, s):
        self.settings_key = Components(inline_keyboards= [InlineKeyboard(f"اعلان ها : {s}", callback_data = "notifchange")
            , InlineKeyboard("قوانین", callback_data = "rule")])

        return self.settings_key
