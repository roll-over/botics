from mtranslate import translate


def get_adapted_message(language, user):
    messages = {
        'en': f"Hello, {translate(user, language).capitalize()}! "
              f"We're in progress of the development. We'll keep you in touch!",
        'ru': f"{translate(user, language).capitalize()}, привет! "
              f"Мы находимся в процессе разработки. Мы будем держать вас на связи!"
    }

    return messages.get(language, 'en')
