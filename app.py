import random, time

weapons = ["rock", "paper", "scissors"]

def main():
  print("Rock Paper Scissors...")
  print("Play against the computer. Best of 3 rounds.")
  time.sleep(2)
  game_start = input("Shall we start? (y/n): ").lower()
  
  if game_start == 'y':
    player_score = 0
    computer_score = 0
    while True:
      if player_score == 3:
        print("You won the game.")
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
        time.sleep(5)
        quit()
      elif computer_score == 3:
        print("You lost to the computer.")
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
        time.sleep(5)
        quit()

      choice = input("Pick rock/paper/scissors: ").lower()
      computer_choice = random.choice(weapons)
      if choice == 'rock' and computer_choice == 'rock':
        print(f"Computer choice: {computer_choice}")
        print("It's a draw!")
      elif choice == 'rock' and computer_choice == 'paper':
        print(f"Computer choice: {computer_choice}")
        computer_score += 1
        print("Computer wins! 1 point added.")
      elif choice == 'rock' and computer_choice == 'scissors':
        print(f"Computer choice: {computer_choice}")
        player_score += 1
        print("You win! 1 point added.")
      elif choice == 'paper' and computer_choice == 'paper':
        print(f"Computer choice: {computer_choice}")
        print("It's a draw!")
      elif choice == 'paper' and computer_choice == 'rock':
        print(f"Computer choice: {computer_choice}")
        player_score += 1
        print("You win! 1 point added.")
      elif choice == 'paper' and computer_choice == 'scissors':
        print(f"Computer choice: {computer_choice}")
        computer_score += 1
        print("Computer wins! 1 point added.")
      elif choice == 'scissors' and computer_choice == 'scissors':
        print(f"Computer choice: {computer_choice}")
        print("It's a draw!")
      elif choice == 'scissors' and computer_choice == 'rock':
        print(f"Computer choice: {computer_choice}")
        computer_score += 1
        print("Computer wins! 1 point added.")
      elif choice == 'scissors' and computer_choice == 'paper':
        print(f"Computer choice: {computer_choice}")
        player_score += 1
        print("You win! 1 point added.")
      else:
        print("Invalid choice.")
  elif game_start == 'n':
    quit()

main()