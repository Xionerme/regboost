# regboost ©

import winreg
import os
import wget


def logo():
    print("                    __                     __ ")
    print("   ________  ____ _/ /_  ____  ____  _____/ /_")
    print("  / ___/ _ \/ __ `/ __ \/ __ \/ __ \/ ___/ __/")
    print(" / /  /  __/ /_/ / /_/ / /_/ / /_/ (__  ) /_  ")
    print("/_/   \___/\__, /_.___/\____/\____/____/\__/ ® ")
    print("          /____/                              ")
    print("")
    print('                       Сredits: Xionerme#8006')


def clear():
    os.system('cls')


def reg():
    registry_key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Control\PriorityControl", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, "Win32PrioritySeparation",
                      0, winreg.REG_QWORD, 38)
    clear()


def regg():
    registry_key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, "NetworkThrottlingIndex",
                      0, winreg.REG_QWORD, 16)
    clear()


def reggg():
    registry_key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, "SystemResponsiveness",
                      0, winreg.REG_QWORD, 10)
    clear()


def ccleaner():
    wget.download(
        'https://drive.google.com/uc?export=download&confirm=no_antivirus&id=12jmj_H-WHV0vApa7-VI8GroEt_apGnlw')
    os.startfile('Clear Cache Files.bat')
    probel()
    print("Ожидайте.")


def cmdd():
    wget.download(
        'https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1UQlyApTohaVX4ILI_4sEHWkx-NQapgUc')
    os.startfile('Latency reducer.bat')
    probel()
    print("Ожидайте.")


def probel():
    print(" ")
    print(" ")
    print(" ")
    print(" ")


def regs():
    reg()
    regg()
    reggg()


logo()
print(" ")
input('Нажми любую кнопку чтобы начать!\n')
clear()

while True:
    logo()
    print(" ")
    print("Готово!\n")
    print("1. Regedit (+30 FPS).\n")
    print("2. CMD Setting (+50 FPS).\n")
    print("3. Cleaner (Delete Cache +10 FPS).\n")
    print("0. Выйти из программы.\n")
    cmd = input("Выберите пункт: ")

    if cmd == "1":
        regs()
    elif cmd == "2":
        cmdd()
    elif cmd == "3":
        ccleaner()
    elif cmd == "0":
        os.remove("Clear Cache Files.bat")
        os.remove("Latency reducer.bat")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        break
    else:
        print("Вы ввели не правильное значение\n")
