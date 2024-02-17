from mtranslate import translate


async def get_welcome_message(language, user):
    messages = {
        'en': f"Hello, {translate(user, language).capitalize().strip()}! "
              f"\nWe're in progress of the development functionality. We'll keep in touch!",
        'ru': f"{translate(user, language).capitalize().strip()}, привет! "
              f"\nМы находимся в процессе разработки функционала! Будем держать в курсе!"
    }

    return messages.get(language, 'ru')


async def get_unacceptable_message(language):
    messages = {
        'en': "Sorry, I don't understand the request. "
              "\nThe list of available commands can be obtained with the command /help",
        'ru': "Извините, не понимаю запрос. "
              "\nСписок доступных команд можно получить командой /help"
    }

    return messages.get(language, 'ru')


async def get_help_message(language):
    messages = {
        'en': "We're working about adding new features ot our bot. "
              "\nIn the meantime, you can choose a team from the available ones.",
        'ru': "Мы работаем над добавлением новых функций нашего бота. "
              "\nПока же можно выбрать команду из доступных."
    }

    return messages.get(language, 'ru')


async def get_support_message(language):
    messages = {
        'en': "Thank you for support! ❤️",
        'ru': "Спасибо за поддержку! ❤️"
    }

    return messages.get(language, 'ru')
