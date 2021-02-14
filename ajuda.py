#Kratosy/Somos uma legião. 2021 ©

import requests, time
import os
from selenium import webdriver
import webbrowser
import platform

def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

def youtube():
   if platform.system() == "Windows":
      webbrowser.open_new_tab("https://youtube.com/channel/UCskiioiBLlpv3djn1rah3qg")
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

def menu():
  opt = input(f'\n{C}[{G}+{C}] Deseja ir para o menu inicial?[{G}s{C}/{R}n{C}]: ')
  if opt == 's':
        clear()
        import consulta
        consulta.main()
  else:
        main()

def ip():
  clear()
  print("\n" + code_info + "Dúvidas: IP.\n")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Por que o IP encontrado não é o meu?
[{G}2{C}] Por que o IP dá inválido?
[{G}3{C}] Por que não consigo consultar?
[{G}4{C}] Nenhuma dessas.
[{G}5{C}] Voltar.
[{G}6{C}] {R}Sair.{C}
''')
too=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if too == "1":
     print(code_info + "Verifique se você está fazendo uso de VPN.")
     menu()
  elif too == "2":
     print(code_info + "Verifique se há pontos ou acentos no endereço de IP. Retire-os.")
     menu()
  elif too == "3":
     print(code_info + "Verifique sua conexão com a internet, pois as consultas fazem uso de API.")
     menu()
  elif too == "4":
     print(code_info + "Mande um comentário diretamente no canal de comunicação do proprietário")
     time.sleep(1.5)
     youtube()
     menu()
  elif too == "5":
     main()
  elif too == "6":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     ip()


def nome():
  clear()
  print("\n" + code_info + "Dúvidas: nome.\n")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Por que não tem os nomes que eu quero?
[{G}2{C}] Por que não compra um banco maior?
[{G}3{C}] Por que uns vem sem data de nascimento?
[{G}4{C}] Por que não consigo consultar?
[{G}5{C}] Nenhuma dessas.
[{G}6{C}] Voltar.
[{G}7{C}] {R}Sair.{C}
''')
too=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if too == "1":
     print(code_info + "Infelizmente o banco é muito limitado e necessita de mais dados. Bancos de dados não são vendidos ou divulgados legalmente.")
     menu()
  elif too == "2":
     print(code_info + "Não há meios legais para se comprar um banco de dados. Mesmo ilegal, são absurdamente caros.")
     menu()
  elif too == "3":
     print(code_info + "Realmente o trabalho no pôde ser executado com excelência. Não é uma falha, mas a ausência dos mesmos.")
     menu()
  elif too == "4":
     print(code_info + "Verifique se está digitando corretamente os nomes, ou se há caracteres especiais.")
     menu()
  elif too == "5":
     print(code_info + "Mande um comentário diretamente no canal de comunicação do proprietário")
     time.sleep(1.5)
     youtube()
     menu()
  elif too == "6":
     main()
  elif too == "7":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     nome()

def cpf():
  clear()
  print("\n" + code_info + "Dúvidas: CPF.\n")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Por que o CPF dá inválido?
[{G}2{C}] É seguro testar o meu CPF?
[{G}3{C}] Por que não consigo consultar?
[{G}4{C}] Nenhuma dessas.
[{G}5{C}] Voltar.
[{G}6{C}] {R}Sair.{C}
''')

too=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if too == "1":
     print(code_info + "Verifique se está digitando corretamente (sem traços e pontos). O erro também pode ser devido as séries de requisições feitas simultaneamente, o que tira as consultas por CPF temporariamente do ar.")
     menu()
  elif too == "2":
     print(code_info + "Sim. Não há nada interceptando. Você está seguro.")
     menu()
  elif too == "3":
     print(code_info + "Verifique sua conexão com a internet, pois as consultas fazem uso de API.")
     menu()
  elif too == "4":
     print(code_info + "Mande um comentário diretamente no canal de comunicação do proprietário")
     time.sleep(1.5)
     youtube()
     menu()
  elif too == "5":
     main()
  elif too == "6":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     cpf()

def cep():
  clear()
  print("\n" + code_info + "Dúvidas: CEP.\n")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Onde posso encontrar o meu CEP?
[{G}2{C}] Por que o CEP está inválido?
[{G}3{C}] Por que não consigo consultar?
[{G}4{C}] Nenhuma dessas.
[{G}5{C}] Voltar.
[{G}6{C}] {R}Sair.{C}
''')
too=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if too == "1":
     print(code_info + "No site dos correios, no link abaixo.\n")
     print(code_result + "https://buscacepinter.correios.com.br/app/endereco/index.php?t")
     menu()
  elif too == "2":
     print(code_info + "Verifique se há pontos, acentos ou caracteres especiais. Retire-os.")
     menu()
  elif too == "3":
     print(code_info + "Verifique sua conexão com a internet, pois as consultas fazem uso de API.")
     menu()
  elif too == "4":
     print(code_info + "Mande um comentário diretamente no canal de comunicação do proprietário")
     time.sleep(1.5)
     youtube()
     menu()
  elif too == "5":
     main()
  elif too == "6":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     cep()

def cnpj():
  clear()
  print("\n" + code_info + "Dúvidas: CNPJ.\n")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] O que é CNPJ?
[{G}2{C}] Onde posso encontrar?
[{G}3{C}] Por que não consigo consultar?
[{G}4{C}] Nenhuma dessas.
[{G}5{C}] Voltar.
[{G}6{C}] {R}Sair.{C}
''')
too=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if too == "1":
     print(code_info + "Fonte: Google\n")
     print(code_result + "O CNPJ substituiu o antigo CGC (Cadastro Geral do Contribuinte). ... O número do CNPJ é a forma como você identifica uma empresa. Funciona, por exemplo, como o CPF para as pessoas físicas. Mas, além de grandes empresas, profissionais autônomos, que prestam serviços, também precisam abrir CNPJ.")
     menu()
  elif too == "2":
     print(code_info + "É possível descobrir o CNPJ de uma empresa pelo nome no site Redesim, um portal de serviços do governo federal para pessoas jurídicas.")
     menu()
  elif too == "3":
     print(code_info + "Verifique sua conexão com a internet, pois as consultas fazem uso de API.")
     menu()
  elif too == "4":
     print(code_info + "Mande um comentário diretamente no canal de comunicação do proprietário")
     time.sleep(1.5)
     youtube()
     menu()
  elif too == "5":
     main()
  elif too == "6":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     cnpj()

def placa():
  clear()
  print("\n" + code_info + "Dúvidas: placa.\n")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] É seguro consultar?
[{G}2{C}] Posso consultar placa roubadas?
[{G}3{C}] Por que não consigo consultar?
[{G}4{C}] Nenhuma dessas.
[{G}5{C}] Voltar.
[{G}6{C}] {R}Sair.{C}
''')
too=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if too == "1":
     print(code_info + "Sim. Não há nada interceptando. Você está seguro.")
     menu()
  elif too == "2":
     print(code_info + "Sim. Entre outras informações sobre o veículo.")
     menu()
  elif too == "3":
     print(code_info + "Verifique sua conexão com a internet, pois as consultas fazem uso de API.")
     menu()
  elif too == "4":
     print(code_info + "Mande um comentário diretamente no canal de comunicação do proprietário")
     time.sleep(1.5)
     youtube()
     menu()
  elif too == "5":
     main()
  elif too == "6":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     placa()

def telefone():
  clear()
  print("\n" + code_info + "Dúvidas: telefone.\n")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Por que o número dá inválido?
[{G}2{C}] Encontra CPF?
[{G}3{C}] Por que não consigo consultar?
[{G}4{C}] Nenhuma dessas.
[{G}5{C}] Voltar.
[{G}6{C}] {R}Sair.{C}
''')
too=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if too == "1":
     print(code_info + "Você deve retirar traço, espaços e parênteses. E respectivamente:\nDDD do país + DDD do estado + 9 + número (8 dígitos)\nExemplo: +552186867321")
     menu()
  elif too == "2":
     print(code_info + "Infelizmente não. Banco de dados não são vendidos e nem divulgados. Essas informações são encontradas por meio de mecanismos não gratuitos.")
     menu()
  elif too == "3":
     print(code_info + "Verifique sua conexão com a internet, pois as consultas fazem uso de API.")
     menu()
  elif too == "4":
     print(code_info + "Mande um comentário diretamente no canal de comunicação do proprietário")
     time.sleep(1.5)
     youtube()
     menu()
  elif too == "5":
     main()
  elif too == "6":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     telefone()

def main():
  clear()
  print("\n" + code_info + "Ajuda.\n")
  print(f'''
[{Y}?{C}] Qual sua dúvida?
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] IP.
[{G}2{C}] Nome.
[{G}3{C}] CPF.
[{G}4{C}] CEP.
[{G}5{C}] CNPJ.
[{G}6{C}] Placa.
[{G}7{C}] Telefone.
[{G}8{C}] Voltar.
[{G}9{C}] {R}Sair.{C}
''')
tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool == "1":
     ip()
  elif tool == "2":
     nome()
  elif tool == "3":
     cpf()
  elif tool == "4":
     cep()
  elif tool == "5":
      cnpj()
  elif tool == "6":
     placa()
  elif tool == "7":
     telefone()
  elif tool == "8":
     import consulta
     consulta.main()
  elif tool == "9":
     clear()
     print(f'\n{G}Somos uma legião.{C}\n')
     exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     main()

main()
