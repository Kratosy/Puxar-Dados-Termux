#Kratosy/Somos uma legião. 2021 ©

import requests, time, re, json
import os
import platform

def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

clear()

#Kratosy/Somos uma legião. 2021 ©

def main():
  clear()
  print("\n" + code_info + "BIN.")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Consultar BIN.
[{G}2{C}] Voltar.
[{G}3{C}] {R}Sair.{C}
''')
tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool=='1':
    bin=input(f'{C}[{G}*{C}] Informe a BIN a ser consultada: {B}')
    consultar(bin)
  elif tool=='2':
    clear()
    import consulta
    consulta.main()
  elif tool=='3':
    clear()
    print(f'\n{G}Somos uma legião.{C}\n')
    exit()
  else:
    clear()
    print(f'{C}[{R}-{C}] Seleção inválida.')
    time.sleep(0.2)
    main()

def consultar(num):
   url = requests.get(f"https://binlist.io/lookup/{num}/")
   res = url.content
   bin = json.loads(res)
   clear()
if bin["success"] == True:
      print("\n" + code_info + "Resultado:\n")
      print(f"{C}BIN: {B}" + bin["number"]["iin"])
      print(f"{C}NOME: {B}" + bin["bank"]["name"])
      print(f"{C}BANDEIRA: {B}" + bin["scheme"])
      print(f"{C}CATEGORIA: {B}" + bin["category"])
      print(f"{C}TIPO: {B}" + bin["type"])
      print(f"{C}PAÍS: {B}" + bin["country"]["name"] + f'({bin["country"]["alpha2"]})')
      print(f"{C}TELEFONE: {B}" + bin["bank"]["phone"])
      print(f"{C}URL: {B}" + bin["bank"]["url"] + f"{C}")
   else:
print("\n" + code_error + "BIN inválida.")
   again()

def again():
    opt = input(f'\n{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        clear()
        main()
else:
        print(f"\n{G}Somos uma legião.{C}\n")
        exit()

main()
