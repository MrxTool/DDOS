#usr/bin/python
from datetime import datetime
import time
import socket
dt = datetime.now()
#LIST COLOR
class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
print(Color.GREEN+'#' *50)
print('\n')
print('                  HACKING TOLLS')
print('\n')
print('#' *50)
print('\n')
print('                   LIST TOOLS')
print(Color.GREEN+'-' *50)
#TOOLS LIST
print('[1] DDOS')
print('[2] SCANNING PORT')
print('[3] WEBSITE DEFACE')
print('[4] FINDING IP ADDRESS')
print('[5] EXIT')
print('-' *50)
print('\n')
print('TYPE: <NUMBER>')
try:
  select_list = int(input('SELECT=> '))
  if select_list == 1:
    time.sleep(3)
    website_url = input('Enter url: ')
    attacker = 'Attack: '
    time.sleep(3)
    limits = int(input('Limit: '))
    for i in range(limits):
      print(Color.RED,'Doing attack:',website_url,i,Color.END)
  elif select_list == 3:
    time.sleep(3)
    url = input('Enter url: ')
    time.sleep(3)
    print('SEARCHING:', url)
    time.sleep(30)
    print('Result: ', url,Color.END)
  elif select_list > 5:
    print('No package tools', Color.END)
  elif select_list == 4:
    time.sleep(3)
    txt_ip = input('Enter website: ')
    if txt_ip == '':
      exit(Color.END)
    IP = socket.gethostbyname(txt_ip)
    labelss = 'Search: '
    print(labelss+txt_ip)
    time.sleep(10)
    del(labelss)
    print(f'Ip address found: ({IP})',Color.END)
  elif select_list == 5:
    print(Color.END)
    exit()
  elif select_list == 2:
    urls = input('Enter url: ')
    time.sleep(3)
    print(f'Scanning: {urls}')
    time.sleep(3)
    ports = 80
    print(f'Port {ports}/TCP is open',Color.END)
except ValueError:
  print('ENTER NUMBER',Color.END)
