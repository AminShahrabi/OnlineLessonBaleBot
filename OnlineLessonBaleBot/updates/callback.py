class CallbackManager:
    def __init__(self):
        pass

    async def get_files(self, path, callback):
        with open(path, "r", encoding="utf-8")as f:
            l = f.readlines()
            for i in l:
                s = i.split("+")
                if callback.data == s[0]:
                    await callback.message.reply_document(s[0], caption='''
ممنون از اینکه از ربات ما استفاده میکنید 🧡
حتما لینک ربات رو با دوستاتون به اشتراک بگذارید 😎''')


