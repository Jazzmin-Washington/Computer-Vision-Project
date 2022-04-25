#%%
# # Computer Vision
from random import choice
import time
class RPS_Game():     
      def __init__(self):
            self.name = ''
            self.player_choice = None
            self.computer_choice = None
            self.computer_wins = 0
            self.player_wins = 0
            
      def welcome(self):
            print("Welcome to my Computer Vision Project in which you will play the classic game of Rock, Paper, Scissors")
            self.name = input("Please enter you name for the game")
            print('Hello,', self.name)
  
                             
      def selection(self):
            print(f'\n Computer Wins: {self.computer_wins}  \n Player Wins: {self.player_wins}\n ')
            guess = False
            self.options = ['Rock', 'Paper','Scissors']
            self.computer_choice = choice(self.options)
            while guess == False:
                   self.player_choice = input('Please use the camera to select: Rock, Paper or Scissors')
                  
                   if self.player_choice == None or self.computer_choice == None:
                        guess == False
                        self.selection()
                      
                   elif self.player_choice != None and self.computer_choice != None:
                        for word in self.options:
                              if self.player_choice == word:
                                   
                                    print(f'You have selected', self.player_choice)
                                    print(f'The computer has chosen', self.computer_choice)
                                    guess = True
                                    self.who_wins()
                                          
                 
           
                  
                        
      def who_wins(self):
            while self.player_wins < 3 and self.computer_wins < 3 :
                  if self.player_choice == ('Rock'):
                        if self.computer_choice ==('Rock'):
                              print("It's a tie")
                              self.selection()
                        elif self.computer_choice == 'Paper':
                              self.computer_wins += 1
                              print('The computer wins')
                              self.selection()
                        elif self.computer_choice == 'Scissors':
                              self.player_wins +=1
                              print(self.name, "wins!")
                              self.selection()
                  elif self.player_choice == 'Paper':
                        if self.computer_choice == 'Paper':
                              print("It's a tie")
                              self.selection()
                        elif self.computer_choice == 'Scissors':
                              self.computer_wins += 1
                              print('The computer wins')
                              self.selection()
                        elif self.computer_choice == 'Rock':
                              self.player_wins += 1
                              print(f'{self.name} wins!')
                              self.selection()
                  elif self.player_choice == 'Scissors':
                        if self.computer_choice == 'Paper':
                              self.player_wins += 1
                              print(f'{self.name} wins!')
                              self.selection()
                        elif self.computer_choice == 'Scissors':
                              print("It's a tie")
                              self.selection()
                        elif self.computer_choice == 'Rock':
                              self.computer_wins += 1
                              print('The computer wins')
                              self.selection()      
                  elif self.player_choice == 'Nothing' or self.computer_choice == 'Nothing':
                        print("You did not select an option or the camera did not pick up your movement. Please try again with a clear visibility of your hands")
                        self.selection() 
            else:
                   self.play_again()
                
           
            
           
                  
      def play_again(self):
            again = input('Would you like to play again? Enter yes or no')
            if again == 'yes':
                  self.lets_play()
            elif again == 'no':
                  print('Thanks for playing!')
            else:
                  print('Please enter y or n for yes and no, respectively')
                  self.play_again()
            
      def lets_play(self):
            self.welcome(), self.selection(), self.play_again()
                  
                        
                  
new_RPS_game = RPS_Game()
new_RPS_game.lets_play()


# %%
