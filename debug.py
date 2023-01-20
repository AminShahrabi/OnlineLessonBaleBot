from colorama import init, Fore, Back, Style

class Debug:
    def __init__(self):
        self.debug = True
        init(autoreset=True)


    def started(self):
        if self.debug:
            print(Fore.GREEN + f"BOT READY FOR USE ")

    def print_errors(self, error, author):
        if self.debug:
            print(Fore.RED + f"ERROR _ {error} to" + Fore.CYAN + f"{author}")

    def print_sent_file(self, message):
        if self.debug:
            print(Fore.CYAN + f"USER {message.author.username}" + Fore.YELLOW + f"SENT FILE ID {message.document.file_id}")

    def print_update(self, update):
        if self.debug:
            print(Fore.GREEN + f"Update type {update.type} ID {update.update_id}")

    def print_ticket(self, message):
        if self.debug:
            print(Fore.YELLOW + f"NEW TICKET FROM {message.author.username}")

