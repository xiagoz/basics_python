import random
import os
os.system('clear')

# Tupla de opciones
options = ('piedra', 'papel', 'tijeras')
print("Jugaremos el mítico juedo de Jan Ken Pon!!")
# Contador de victorias
computer_wins = 0
user_wins = 0
# Contador de rounds
rounds = 1

while True:
  print('')
  print('*' * 10)
  print('Round', rounds)
  print('*' * 10)
  print('')

  # user_option
  user_option = input('Selecciona una de estas opciones (estrictamente escritas como te las muestro) => piedra, papel o tijeras:  ').lower()
  
  # Opciones escogida aleatoreamente por el uso de random
  computer_option = random.choice(options)
  
  if not user_option in options:
    print('Esa opción no es valida')
    continue
  else:
    print('')
    print('*' * 50)
    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    print('*' * 50)
    print('')
    
  #Validaciones del juego
  if user_option == computer_option:
    print('')
    print('Ambos eligieron lo mismo, es un empate!! Buena esa cholo')
  elif user_option == 'piedra':
    if computer_option == 'tijeras':
      print("Piedra le gana a Tijeras")
      print('El usuario gana!')
      user_wins += 1
    else:
      print('Papel le gana a piedra')
      print('La computadora gana!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print("Papel le gana a Piedra")
      print('El usuario gana!')
      user_wins += 1
    else:
      print('Tijera le gana a Papel')
      print('La computadora gana!') 
      computer_wins += 1
  elif user_option == 'tijeras':
    if computer_option == 'papel':
      print("Tijeras le gana a Papel")
      print('El usuario gana!')
      user_wins += 1
    else:
      print('Piedra le gana a Tijeras')
      print('La computadora gana!')
      computer_wins += 1
  
  if computer_wins == 2:
    print('El ganador es la computadora')
    break

  if user_wins == 2:
    print('El ganador es el usuario')
    break

  print('')
  print('*' * 50)
  print(f'El score es => Computadora: {computer_wins}, Usuario: {user_wins}.')
  print('*' * 50)
  print('')

  rounds += 1