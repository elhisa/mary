1

n = int(input('insira um n'))
count = 0
t1 = -1
t2 = 1
while count <= n:
    t3 = t1 + t2
    if t3 != 0:
     print(t3)
    t1 = t2
    t2 = t3
    count += 1

4

c = ''
while True:
   if c == 'n':
     break
   n1 = int(input('insira um número:'))
   print('\n[+] soma\n[-] subtração\n[*] multiplicação\n[/] divisão\n[**] exponenciação')
   op = input('\ninsira uma operação: ')
   while not (op == "+" or op == "-" or op == '*' or op == "/" or op == "**"):
      print('operação inválida.')
      print('\n[+] soma\n[-] subtração\n[*] multiplicação\n[/] divisão\n[**] exponenciação')
      op = input('\ninsira uma operação : ')
   n2 = int(input('insira um outro número:'))
   if op == '+':
      result = n1 + n2
   elif op == "-":
      result = n1 - n2
   elif op == "*":
      result = n1 * n2
   elif op == "/":
      result = n1 / n2
   elif op == '**':
      result = n1 ** n2
   print(result)
   c = input('você quer continuar? [s/n]').lower()
   while not ((c == 's' or c == "n") and len(c)) == 1:
      print('resposta inválida')
      c = input('você quer continuar? [s/n] '). lower() 
      if c == 'n':
         break
      else:
        continue


