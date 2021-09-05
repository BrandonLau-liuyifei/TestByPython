# ！/usr/bin/env python
# -*- coding：utf-8 -*-

dict = {
    "reset": "reset what",
    "reset board": "board fault",
    "board add": "where to add",
    "board delete": "no board at all",
    "reboot backplane": "impossible",
    "backplane abort": "install first"
}

while True:
    try:
        command = input()
        if command in dict:
            print(dict[command])
        else:
            print("unknown command")
    except:
        break
