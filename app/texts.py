class Instruction:
    @staticmethod
    def get_ins():
        text = ('Всё довольно просто!\n'
                '1) Выберите нужную ссылку/текст;\n'
                '2) Скопируйте и вставьте в чат с ботом, примерно так:\n'
                '"имя для qr-code"  "ваша ссылка/текст"\n'
                '3) Бот отправляет вам QR-code! 😎')
        return text


class Example:
    @staticmethod
    def get_example():
        text = ('Разберем на примере\n'
                'Ютуб https://www.youtube.com/ \n'
                'Через пару секунд бот отправлят вам фото вашего qr-кода ✅')
        return text


class Help:
    @staticmethod
    def get_help():
        text = ('Есть проблема?😵‍💫 \n'
                'Спокойствие и только спокойствие! \n\n'

                'Проверьте, правильно ли вы написали: \n'
                '✅ без запятых, выглядит примерно так: "ютуб https://www.youtube.com/"\n\n'

                '❌ без пробела, запятые или другие символы - "ютуб,https://www.youtube.com"\n'
                '❌ нерабочая ссылка - "ютуб https://www.youtube"\n '
                '❌ лишние символы или буквы в ссылке — "ютуб https:/!/wwww.youtttube...com/"\n\n')
        return text


class APIException(Exception):
    pass


