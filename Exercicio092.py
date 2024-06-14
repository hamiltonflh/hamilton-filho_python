from datetime import datetime
trabs = {}
trabs["Nome"] = str(input('Nome completo: '))
nasc = int(input('Ano de nascimento: '))
anoat = datetime.now().year
trabs["Idade"] = anoat - nasc
r = str(input('Você tem CTPS(Carteira Nacional de Trabalho)? [S/N]: ')).upper().strip()[0]
if r in 'S':
  trabs["CTPS"] = int(input('Número da CTPS: '))
  primctrl = int(input('Ano do contrato: '))
  trabs["Contrato"] = primctrl
  trabs["Salário"] = float(input('Seu salário: R$'))
  apos = ((25 - (anoat - primctrl)) + anoat) - nasc
  trabs["Aposentadoria"] = apos

print('-='*60)
print('CADASTRO EFETUADO')
print('-='*60)  
for k, v in trabs.items():
  print(f'{k}: {v}')