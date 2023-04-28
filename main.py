money_history = []
print('||||| Money Mangement Program |||||')
print('|-------- Commands List ----------|')
print('| 0 : exit program                |')
print('| 1 : deposit                     |')
print('| 2 : spend                       |')
print('| 3 : balance                     |')
print('| 4 : history                     |')
print('|---------------------------------|')
while True:  # forever!!!!
  command = input('Enter your command: ')
  if command == '1':
    print('[Deposit Money]')
    money = input('How much do you deposit? ')
    money_history.append(money)
    print(f'you saved ${money} ')
  # Assignment!!!! complete the spend part
  elif command == '2':
    print('[Spend Money]')
    money = input('How much do you spend? ')

    balance = 0
    for i in money_history:
      balance = balance + int(i)

    if int(money) > balance:
      print('Haha! you dont have enough balance')
    else:
      money_history.append('-' + money)
      print(f'you spent ${money} ')
  elif command == '3':
    print('[Check Balance]')
    balance = 0
    for i in money_history:
      balance = balance + int(i)
    print(f'You have ${balance}')
  elif command == '4':
    print('[Show History]')
    print(money_history)
  elif command == '0':
    break
  else:
    print('the command is not supported')

  print('-' * 30)