import requests
from bs4 import BeautifulSoup

text = ""
list_mail = ('@gmail.com','@yahoo.com','@outlook.com','@hotmail.com','@aol.com','@icloud.com','@mail.com','@live.com','@protonmail.com','@zoho.com','@mail.ru','@yandex.ru','@gmx.com','@inbox.com','@tutanota.com','@runbox.com')
list_url = []
https = input("https:")
def help():
    print("To use the parser, you can enter one or more URL links in the https field. Use the -h command for help and the -e command to exit.")
while True:
    try:
        for i in https.split(' '):
            if i != "":
                list_url.append(i)

        for l in list_url:
            get = requests.get(l)
            soup = BeautifulSoup(get.text, 'html.parser')

            if get.status_code == 200:
                body = soup.find('body')
                text = body.get_text()
            if text != "":
                for i in text.split(' '):
                    for k in range(len(list_mail)):
                        if list_mail[k] in i:
                            print(i)
        print("For help, use the -h command.")
        command = input('command: ')
        if command == "-e":
            break
        if command == '-h':
            help()
        else:
            print('command not found')
            break
    except:
        print("You received an error: invalid input or something else.")
        help()
        break