def send_email(message, recipient, sender = 'university.help@gmail.com'):
    symbols = ('.com', '.ru', '.net')
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender,  'на адрес', recipient)
    elif '@' in recipient and sender:
        if recipient.endswith(symbols) and sender.endswith(symbols):
            print('Письмо успешно отправленно с адреса ', sender,  'на адрес',  recipient)
        else:
            print('Невозможно отправить письмо с адреса ', sender, 'на адрес', recipient)
    else:
        print('Невозможно отправить письмо с адреса ', sender,  'на адрес', recipient)


send_email('Hi', 'vasyok1337@gmail.com')
send_email('Hi', 'vasyok1337@gmail.com', sender = 'urban.info@gmail.com' )
send_email('Hi', 'vasyok1337@gmail.com', sender = 'vasyok1337@gmail.com')
send_email('Hi', 'vasyok1337.gmail.com')
send_email('Hi', 'vasyok1337@gmail.rak')