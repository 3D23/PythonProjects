import Analyser
print('Введите что-нибудь (off - выключить)')
request = input()
while (request.lower() != 'off'):
    Analyser.main(request)
    request = input('Введите что-нибудь (off - выключить)')
