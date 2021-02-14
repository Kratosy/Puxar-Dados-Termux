#Kratosy/Somos uma legião. 2021 ©

import requests, time
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
 print("\n" + code_info + "CEP.")
 print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Consultar CEP.
[{G}2{C}] Voltar.
[{G}3{C}] {R}Sair.{C}
''')
tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
 if tool=='1':
    cep = input(f"{C}[{G}*{C}] Informe o CEP (sem traço): {B}")

    if len(cep) != 8:
        print(f"\n{R}CEP inválido/inexistente {C}\n")
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    address_data = request.json()

    if 'erro' not in address_data:
        clear()
        print()
        print(f"{C}[{G}i{C}] CEP encontrado.")
        print()
        print(f"CEP: {B}{address_data['cep']}{C}")
        print(f"ENDEREÇO: {B}{address_data['logradouro']}{C}")
        print(f"COMPLEMENTO: {B}{address_data['complemento']}{C}")
        print(f"BAIRRO: {B}{address_data['bairro']}{C}")
        print(f"CIDADE: {B}{address_data['localidade']}{C}")
        print(f"ESTADO: {B}{address_data['uf']}{C}")
        print(f"IBGE: {B}{address_data['ibge']}{C}")
        print(f"GIA: {B}{address_data['gia']}{C}")
        print(f"DDD: {B}{address_data['ddd']}{C}")
        print(f"SIAFI: {B}{address_data['siafi']}{C}")
        print()

else:
        print(f'\n{R}{cep} é CEP inválido/inexistente{C}\n')
    
    opt = input(f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ')
    if opt == 's':
        clear()
        main()
    else:
        print(f"\n{G}Somos uma legião.{C}\n")
        exito()
 elif tool == "2":
        clear()
        import consulta
        consulta.main()
 elif tool == "3":
        clear()
        print(f"\n{G}Somos uma legião.{C}\n")
        exit()
 else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     main()

if __name__== '__main__':
    main()

#Kratosy/Somos uma legião. 2021 ©
