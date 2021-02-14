#Kratosy/Somos uma legião. 2021 ©

import requests, os, time, base64, json, re
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

a='aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA=='
a=a.encode('ascii')
a=base64.b64decode(a)
a=a.decode('ascii')

def main():
  clear()
  print("\n" + code_info + "CPF.")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Consultar CPF.
[{G}2{C}] Gerar CPF e consultar.
[{G}3{C}] Voltar.
[{G}4{C}] {R}Sair.{C}
''')
tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool=='1':
    cpf=input(f'{C}[{G}*{C}] Informe o CPF a ser consultado (sem pontos ou traços): {B}')
    consultar(cpf)
  elif tool=='2':
    gerarcpf()
  elif tool=='3':
    clear()
    import consulta
    consulta.main()
  elif tool=='4':
    clear()
    print(f'\n{G}Somos uma legião.{C}\n')
    exit()
  else:
    clear()
    print(f'{C}[{R}-{C}] Seleção inválida.')
    time.sleep(0.2)
    main()

#Kratosy/Somos uma legião. 2021 ©

def gerarcpf():
  print(f'{C}[{G}*{C}] Gerando CPF...')
  time.sleep(1)
  cpf=requests.request('GET','http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
  cpf2=cpf['data']['number_formatted']
  cpf=cpf['data']['number']
  print(f'{C}[{Y}i{C}] O CPF gerado foi: {B}'+cpf2)
  time.sleep(1)
  print(f'{C}[{G}*{C}] Consultando CPF gerado...')
  nova=input("\n" + f'{C}[{G}+{C}] Deseja consultar?[{G}s{C}/{R}n{C}]: ').lower()
  if nova=='s' or nova=='sim':
      clear()
      consultar(cpf)
  else:
      print(f'\n{G}Somos uma legião.{C}\n')
      exit()
  
def consultar(cpf):
  try:
    h={
    'Content-Type': "text/xml, application/x-www-form-urlencoded;charset=ISO-8859-1, text/xml; charset=ISO-8859-1",
    'Cookie': "ASPSESSIONIDSCCRRTSA=NGOIJMMDEIMAPDACNIEDFBID; FGTServer=2A56DE837DA99704910F47A454B42D1A8CCF150E0874FDE491A399A5EF5657BC0CF03A1EEB1C685B4C118A83F971F6198A78",
    'Host': "www.juventudeweb.mte.gov.br"
    }
    r=requests.post(a, headers=h, data=f'acao=consultar%20cpf&cpf={cpf}&nocache=0.7636039437638835').text
    clear()
    print(f'''
{C}CPF: {B}{re.search('NRCPF="(.*?)"', r).group(1)}
{C}Nome: {B}{re.search('NOPESSOAFISICA="(.*?)"', r).group(1).title()}
{C}Nascimento: {B}{re.search('DTNASCIMENTO="(.*?)"', r).group(1)}
{C}Nome da Mae: {B}{re.search('NOMAE="(.*?)"', r).group(1).title()}
{C}Endereco: {B}{re.search('NOLOGRADOURO="(.*?)"', r).group(1).title()}, {re.search('NRLOGRADOURO="(.*?)"', r).group(1)}
{C}Complemento: {B}{re.search('DSCOMPLEMENTO="(.*?)"', r).group(1).title()}
{C}Bairro: {B}{re.search('NOBAIRRO="(.*?)"', r).group(1).title()}
{C}Cidade: {B}{re.search('NOMUNICIPIO="(.*?)"', r).group(1).title()}-{re.search('SGUF="(.*?)"', r).group(1)}
{C}CEP: {B}{re.search('NRCEP="(.*?)"', r).group(1)}
''')
nova=input(f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()
    if nova=='s' or nova=='sim':
      clear()
      main()
    else:
      print(f'\n{G}Somos uma legião.{C}\n')
      exit()
  except(AttributeError):
    print(f'{R}CPF inexistente{C}' + "\n")
    nova=input(f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()
    if nova=='s' or nova=='sim':
      clear()
      main()
    else:
      clear()
      print(f'\n{G}Somos uma legião.{C}\n')
      exit()




main()

#Kratosy/Somos uma legião. 2021 ©
