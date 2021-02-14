#Kratosy/Somos uma legião. 2021 ©

import requests, time
import os
import platform
try:
   import requests
   import bs4
   import html5lib
   import phonenumbers
   import argparse
   import urllib3
   import colorama
except:
   os.system("python3 -m pip install --upgrade pip")
   os.system("pip install -r requirements.txt")
   clear()
   print(code_result + "Instalado com sucesso.\n")
   main()

def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

def youtube():
   if platform.system() == "Windows":
      import webbrowser
      webbrowser.open_new_tab("https://youtube.com/channel/UC3HJVMAGPQnL3EglFcaFsKg")
   else:
       os.system("termux-open-url https://youtube.com/channel/UCskiioiBLlpv3djn1rah3qg")

clear()
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

print(f'''{C}

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        ▓▓▓▓██░░░░░░░░░░░░░░░░▓▓██▓▓
      ██░░░░                    ░░░░▓▓
    ▓▓░░                            ░░▓▓
  ██░░                                ░░██
  ██    ░░░░▓▓░░░░      ░░░░░░░░░░░░    ▓▓
  ▓▓  ▓▓░░▒▒▓▓▓▓▓▓░░    ░░▓▓▓▓▓▓▒▒░░▓▓  ▓▓
  ▓▓██          ▓▓██    ████          ██▓▓
  ▓▓            ░░░░    ░░░░          ░░▓▓
  ▓▓▒▒  ▒▒▒▒▓▓▒▒░░░░    ░░░░▒▒▒▒▓▓▒▒  ▒▒▓▓
  ▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓░░    ░░▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓
  ▓▓░░  ░░░░░░░░  ▓▓    ██  ░░░░░░░░  ░░▓▓
  ▓▓  ░░░░        ▓▓    ██        ░░░░  ▓▓
  ▓▓░░░░░░░░      ▓▓    ██      ░░░░░░░░▓▓
  ▓▓░░░░░░░░            ▓▓        ░░░░  ██
  ▓▓░░▓▓        ▓▓        ▓▓        ▓▓░░▓▓
  ▓▓░░▓▓▓▓        ▓▓░░░░▓▓        ▓▓▓▓░░▓▓
  ▓▓░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░░▓▓
  ▓▓░░░░░░▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓
    ▒▒  ░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒░░░░▒▒
      ▓▓    ░░░░░░░░░░░░░░░░░░░░  ░░▓▓
      ▓▓░░    ░░░░░░██▓▓░░░░░░    ░░▓▓
        ▓▓░░        ▓▓▓▓        ░░▓▓
          ▓▓░░    ░░▓▓▓▓░░    ░░▓▓
            ▓▓░░  ░░▓▓▓▓░░  ░░▓▓
              ██░░  ▓▓▓▓  ░░▒▒
                ▓▓▓▓▓▓▓▓▓▓▓▓
             KRATOSY / ANONYMOUS
'''); time.sleep(1.5)
clear()

#Kratosy/Somos uma legião. 2021 ©


url = "https://raw.githubusercontent.com/Snuking/snuking/main/version.txt"
version = str(requests.get(url).text)

def main():
  clear()
  v = "1.0.3"
  print(f'''{G}
\n
.----.______
|           |
|    ___________
|   /          /
|  /          /
| /          /
|/__________/ {v}
{C}
 ''')
  print(f"{Y}Atual: {version}{C}")

  print("\n" + code_info + "Menu.")

  print(f'''
{C}[{G}i{C}] Formas de operação:
[{G}1{C}] IP.
[{G}2{C}] Nome.
[{G}3{C}] CPF.
[{G}4{C}] Vizinhos.
[{G}5{C}] CEP.
[{G}6{C}] CNPJ.
[{G}7{C}] Placa.
[{G}8{C}] Telefone.
[{G}9{C}] BIN.
[{G}10{C}] Gerador.
[{G}11{C}] YouTube.
[{G}44{C}] Atualizar.
[{G}55{C}] Novidades.
[{G}66{C}] Ajuda.
[{G}00{C}] {R}Sair.{C}
''')
tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool == "1":
     clear()
     import ip
     ip.main()
  elif tool == "2":
     clear()
     import nome
     nome.main()
  elif tool == "3":
     clear()
     import cpf
     cpf.main()
  elif tool == "4":
     clear()
     import vizinhos
     vizinhos.main()
  elif tool == "5":
     clear()
     import cep
     cep.main()
  elif tool == "6":
     clear()
     import cnpj
     cnpj.main()
  elif tool == "7":
     clear()
     import placa
     placa.main()
  elif tool == "8":
     clear()
     import telefone
     telefone.main()
  elif tool == "9":
     import bin
     bin.main()
  elif tool == "10":
     import gerador
     gerador.main()
  elif tool == "11":
     youtube()
     main()
  elif tool == "44":
         print(code_result + "Abrindo o tutorial de como atualizar no YouTube...")
         time.sleep(2)
         youtube()
         main()

elif tool == "55":
     import novidades
     novidades.main()
  elif tool == "66":
     import ajuda
     ajuda.main()
  elif tool == "00":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     main()
main()

#Kratosy/Somos uma legião. 2021 ©
