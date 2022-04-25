# Computer-Vision-Project
Using a teachable machine, we trained a machine to recognize four images: Rock, Paper, Scissors and Nothing. 
We will then use our trained model and install dependicies. Afterward, we will code for the game of Rock, Paper and Scissors using if/while/else statements. Finally, we will proceed to play Rock, Paper, Scissors with the computer.


**Milestone 1: Training the model (Completed):**
Using teachablemachine.withgoogle.com, we trained an image model with four different classes: Rock, Paper, Scissors and Nothing. The trained model was then downloaded via TensorFlow and saved in a directory.
  
Example of Scissors: ![image](https://user-images.githubusercontent.com/102431019/163892362-aac51e8e-6d17-4942-9756-fc1d1f4a8211.png)
 
 
 Example of Paper: ![image](https://user-images.githubusercontent.com/102431019/163892481-60a1d385-ffc3-43ed-858f-c6f1b342b956.png)
 
 
 Example of Rock: ![image](https://user-images.githubusercontent.com/102431019/163892568-2eacf2ef-76d2-4a2b-a8dd-66d79f1b9bc0.png)
 
 
 
 
 
 
 
**Milestone 2: Installing the dependencies (In Progress):**
A new virtual environment was created using conda. Within this new environment, opencv-python, TensorFlow, and ipykernel libraries were downloaded using the commandline. The model was then run oon my local machine. This model makes variable predictions containing the output of the model. Each element in the output corresponds to the class

Within the command line:

    #To change the directory to my working directory:
    
      cd ~/Documents/AiCore/AiCore_Projects/Computer_Vision_Rock_Paper_Scissors
      
      #To create a new conda environment. 
      # Note the newest version of TensorFlow is not compatible with current version of python so the environment was made with an older version.
      $ conda create -n Computer_Vision_RPS python=3.8
      
      #To activate the environement:
      $ conda activate Computer_Vision_RPS
      
      #To install the dependencies: opencv-python, TensorFlow and ipykernel
      $ pip install opencv-python
      $ pip install tensorflow
      $ pip install ipykernel
      
![image](https://user-images.githubusercontent.com/102431019/164050034-5dd85f6e-cda8-4254-a8e3-ec344959d780.png)

  
  
  
  
  
  
**Milestone 3: Creating the Rock, Paper, Scissor Game (In Progress):**
A command for user input was made to store the user's and the computer's choices using the random with python. Using while, if, else statements, a wiinning structure was created so the program can decide who wins. This code was then encompassed in a function to similate a game of Rock, Paper, Scissors.

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
    
    
 ![image](https://user-images.githubusercontent.com/102431019/165142439-bb39ca18-9481-4d17-a84f-9f6b6b5c9873.png)






          
**Milestone 4: Putting it together (Not Completed):**
Finally, code to use the webcam was then combined to previously designed play function which requires the user to put an input of Rock, Paper or Scissors and output the computer vision model. A countdown was added foe easy gameplay.
