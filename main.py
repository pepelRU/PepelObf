import os
import sys
import zlib
import time
import base64
import marshal
import py_compile

class Colors:
    HEADER = '\033[1;219m'
    MENU = '\033[1;34m'
    INPUT = '\033[1;37m'
    WARNING = '\033[1;33m'
    FAIL = '\033[1;31m'
    OK = '\033[1;32m'
    END = '\033[0m'
    BOLD = '\033[1m'
    LINE = '\033[1;36m'

if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit("\nВаша версия Python не поддерживается!")

zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))

note = "\x23\x20\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x70\x65\x70\x65\x6c\x4f\x42\x46\x0a\x23\x20\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x69\x74\x68\x75\x62\x2e\x63\x6f\x6d\x2f\x68\x74\x72\x2d\x74\x65\x63\x68\x0a\x23\x20\x54\x69\x6d\x65\x20\x3a\x20%s\n\x23\x20\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x0a" % time.ctime()

def banner():
    border = '═' * 35
    title = "PepelObf"
    author = "Автор : pepelRU"
    subtitle = "Obfuscator Python кода"
    github = "Github : github.com/pepelRU"

    print(f" {Colors.LINE}╔{border}╗{Colors.END}")
    print(f" {Colors.LINE}║{Colors.END}{title:^35}{Colors.LINE}║{Colors.END}")
    print(f" {Colors.LINE}║{Colors.END}{author:^35}{Colors.LINE}║{Colors.END}")
    print(f" {Colors.LINE}║{Colors.END}{subtitle:^35}{Colors.LINE}║{Colors.END}")
    print(f" {Colors.LINE}║{Colors.END}{github:^35}{Colors.LINE}║{Colors.END}")
    print(f" {Colors.LINE}╚{border}╝{Colors.END}\n")

def menu():
    menu_options = [
        "Закодировать с помощью Marshal",
        "Закодировать с помощью Zlib",
        "Закодировать с помощью Base16",
        "Закодировать с помощью Base32",
        "Закодировать с помощью Base64",
        "Закодировать с помощью Zlib, Base16",
        "Закодировать с помощью Zlib, Base32",
        "Закодировать с помощью Zlib, Base64",
        "Закодировать с помощью Marshal, Zlib",
        "Закодировать с помощью Marshal, Base16",
        "Закодировать с помощью Marshal, Base32",
        "Закодировать с помощью Marshal, Base64",
        "Закодировать с помощью Marshal, Zlib, Base16",
        "Закодировать с помощью Marshal, Zlib, Base32",
        "Закодировать с помощью Marshal, Zlib, Base64",
        "Простое кодирование",
        "Выход"
    ]
    for i, option in enumerate(menu_options, 1):
        print(f"{Colors.MENU}[{i:02}]{Colors.END} {option}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class FileSize:
    def datas(self, z):
        for x in ['Байт', 'КБ', 'МБ', 'ГБ']:
            if z < 1024.0:
                return f"{z:3.1f} {x}"
            z /= 1024.0
    def __init__(self, path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(f" {Colors.WARNING}[-] Размер закодированного файла : {self.datas(dts)}{Colors.END}\n")
            
def Encode(option, data, output):
    loop = int(eval(_input % f" {Colors.INPUT}[-] Количество кодирований : {Colors.END}"))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 7:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 8:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 9:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 10:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 11:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 12:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 13:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 14:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 15:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        sys.exit(f"\n{Colors.FAIL}Неверная опция!{Colors.END}")
    
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(f"\n{Colors.FAIL}Ошибка типа : {str(s)}{Colors.END}")
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()

def SEncode(data, output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output, output)

def MainMenu():
    try:
        clear_console()
        banner()
        menu()
        try:
            option = int(eval(input(f"\n{Colors.INPUT}[-] Опция : {Colors.END}")))
        except ValueError:
            sys.exit(f"\n{Colors.FAIL}Неверная опция!{Colors.END}")
        
        if option > 0 and option <= 17:
            if option == 17:
                sys.exit(f"\n{Colors.OK}Спасибо за использование этого инструмента{Colors.END}")
            clear_console()
            banner()
        else:
            sys.exit(f'\n{Colors.FAIL}Неверная опция!{Colors.END}')
        try:
            file = eval(_input % f"\n{Colors.INPUT}[-] Имя файла : {Colors.END}")
            data = open(file).read()
        except IOError:
            sys.exit(f"\n{Colors.FAIL}Файл не найден!{Colors.END}")
        
        output = file.lower().replace('.py', '') + '_OBF.py'
        if option == 16:
            SEncode(data, output)
        else:
            Encode(option, data, output)
        print(f"\n{Colors.OK}[-] Файл успешно зашифрован: {file}{Colors.END}")
        print(f"\n{Colors.OK}[-] Сохранено как: {output}{Colors.END}")
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    MainMenu()