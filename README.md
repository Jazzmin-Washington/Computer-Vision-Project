#Computer-Vision-Project
---------------------------------------------------------------------------------------------------------------------------------------------
 ### Using a teachable machine, we trained a machine to recognize four images: Rock, Paper, Scissors and Nothing. We will then use the trained model to play a game of Rock, Paper and Scissors using the camera implementing python coding and Computer Vision techniques.  
---------------------------------------------------------------------------------------------------------------------------------------------

## **Milestone 1: Training the model (Completed):**
- Using a [Teachable Machine](teachablemachine.withgoogle.com) , we trained an image model with four different classes: Rock, Paper, Scissors and Nothing. The trained model was then downloaded via TensorFlow and saved in a directory.
  
  ![Picture_for_ReadME](https://user-images.githubusercontent.com/102431019/166975425-94d2a941-294d-4b26-961c-5899668f7bc3.png)

 - This model makes variable predictions containing the output of the model. Each element in the output corresponds to the class. The more pictures one uses, the better the overall model. This is why 1000 + images were used for this model. **Please keep in mind, the handshapes should be similar to those shown above or the model may not predict the player choices as accurately.**
 
 ---------------------------------------------------------------------------------------------------------------------------------------------
 
## **Milestone 2: Installing the dependencies (Completed):**
- A new virtual environment was created using conda. Within this new environment, opencv-python, TensorFlow, and ipykernel libraries were downloaded using the commandline. 

Within the command line:

    #To change the directory to my working directory:
    
      cd ~/Documents/AiCore/AiCore_Projects/Computer_Vision_Rock_Paper_Scissors
      
      #To create a new conda environment. 
      # Note the newest version of TensorFlow is not compatible with current version of python so the environment was made with an older version.
      $ conda create -n Computer_Vision_RPS python=3.8
      
      #To activate the environment:
     
      $ conda activate Computer_Vision_RPS
      
      #To install the dependencies: opencv-python, TensorFlow and ipykernel
      $ conda install opencv-python
      $ conda install tensorflow
      $ conda install ipykernel
  
  
  ![image](https://user-images.githubusercontent.com/102431019/164050034-5dd85f6e-cda8-4254-a8e3-ec344959d780.png)
   
   Picture Above: The necessary dependencies were downloaded and pictured above.
      
  - The model was then run on a local machine using the previously made conda environment as the Jupyter/Python interpreter. The following code was used to test the decision accuracy of the model and ensure it recognized the different classes.
  
        model = load_model('RPS_Model_Final.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        new_RPS_game = RPS_Game()
        new_RPS_game.welcome()


        while True: 
              ret, frame = cap.read()
              resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
              image_np = np.array(resized_frame)
              normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
              data[0] = normalized_image
              prediction = model.predict(data)
              cv2.imshow('Rock, Paper, Scissors Game', frame)
              new_RPS_game.getting_started()
              if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()
                  
 ---------------------------------------------------------------------------------------------------------------------------------------------
  
## **Milestone 3: Creating the Rock, Paper, Scissor Game: (Completed)**

- The necessary programs were imported including tensorflow, numpy, opencv(cv2) and time. A Rock, Paper, Scissors Class was created and attributes to keep track of the overall game was initialized:

      #Programs and Initialization
    
      from random import choice
      import time
      import cv2
      from tensorflow.keras.models import load_model
      import numpy as np

      class RPS_Game():     
            def __init__(self):
                  self.name = ''
                  self.player_choice = ''
                  self.computer_choice = ''
                  self.computer_wins = 0
                  self.player_wins = 0
                  self.options = ['Rock', 'Paper','Scissors']
                  self.rounds = 0 
            

- A command for user input was made to store the user's and the computer's choices using the random with python. To add a personal touch, the player is prompted to enter their name before the game begins. Note: if the camera isn't starting up, it could be due tto the program waiting for the name to be input.
    
        def welcome(self):
            print("Welcome to my Computer Vision Project in which 
            you will play the classic game of Rock, 
            Paper,Scissors")
            self.name = input("Please enter you name for the game")
            print('Hello,', self.name)
      

- A winning structure function `def who_wins()` was created so the program can decide a winner for each round. This function will then be integrated with the camera so the output of the camera is decided as a matching 'string' within the function.

        def who_wins(self):
            if self.player_wins < 3 and self.computer_wins < 3 :
                 if self.computer_choice == self.player_choice:
                        print("It's a tie")
                        self.show_text(frame, f"It's a Tie ", (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_8)
                        self.rounds +=1
                        cv2.waitKey(2500)
                        self.play_again()

                 elif self.player_choice == ('Rock'):
                        if self.computer_choice == 'Paper':
                              self.computer_wins += 1
                              print('The computer wins')
                              self.show_text(frame, f"The Computer Wins!!", (75, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (0, 255, 255), 2, cv2.LINE_8) 
                              self.rounds +=1
                              cv2.waitKey(2500)
                              self.play_again()
                        elif self.computer_choice == 'Scissors':
                              self.player_wins +=1
                              self.rounds +=1
                              print(f'{self.name} wins!')
                              self.show_text(frame, f"{self.name} Wins!!", (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_8)
                              cv2.waitKey(2500)
                              self.play_again()
                 elif self.player_choice == 'Paper':
                        if self.computer_choice == 'Scissors':
                              self.computer_wins += 1
                              self.rounds +=1
                              print('The computer wins')
                              self.show_text(frame, f"The Computer Wins!!", (75, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (0, 255, 255), 2, cv2.LINE_8)  
                              cv2.waitKey(2500)
                              self.play_again()
                        elif self.computer_choice == 'Rock':
                              self.player_wins += 1
                              self.rounds +=1
                              print(f'{self.name} wins!')
                              self.show_text(frame, f"{self.name} Wins!!", (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_8) 
                              cv2.waitKey(2500)
                              self.play_again()
                 elif self.player_choice == 'Scissors':
                        if self.computer_choice == 'Paper':
                              self.player_wins += 1
                              self.rounds +=1
                              print(f'{self.name} wins!')
                              self.show_text(frame, f"{self.name} Wins!!", (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_8)
                              cv2.waitKey(2500)
                              self.play_again()
                        elif self.computer_choice == 'Rock':
                              self.computer_wins += 1
                              self.rounds +=1
                              print('The computer wins')
                              self.show_text(frame, f"The Computer Wins!!", (75, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (0, 255, 255), 2, cv2.LINE_8)
                              cv2.waitKey(2500)
                              self.play_again() 
        
     ![image](https://user-images.githubusercontent.com/102431019/165142439-bb39ca18-9481-4d17-a84f-9f6b6b5c9873.png)
      
     The picture above illustrated how the  `def who_wins()` function was tested using an text input in which the user picks Rock, Paper, Scissors to ensure the correct winner is selected and the `play_again()` function was called properly.
                              
                              
- After the player or the computer achieves three wins, the game will end. The ``self.getting_started()`` will then give the player the option to play again or quit the game.
         
         #Determines when the game is over and the winner
         def play_again(self):
            if self.computer_wins == 3 or self.player_wins == 3:
                  
                  if self.computer_wins == 3:
                        cv2.putText(frame, f"The Computer Wins the Game!!", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (255, 255, 255), 2, cv2.LINE_AA)
                        cv2.waitKey(2500)
                        print('The Computer WINS the Game!!')
            
                  elif self.player_wins == 3:
                        cv2.putText(frame, f'{self.name} WINS the Game!!', (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (255, 255, 255), 2, cv2.LINE_AA)
                        cv2.waitKey(2500)
                        print(f'{self.name} WINS the Game!!')       
            else:
       
                  self.getting_started()
                                   
  
---------------------------------------------------------------------------------------------------------------------------------------------  
## **Milestone 4: Putting it together (Completed):**

- A class list was created to allow the program to match the input of the player to the trained model. **It is important to note that this class list should match the order of the classes that were put into the [Teachable Machine](teachablemachine.withgoogle.com)

      # Looks up which move is the best fit for the camera input
      def move_list(self, value):
            Rev_Class_Map = {
                  0: 'Rock',
                  1: 'Paper',
                  2: 'Scissors',
                  3: 'Nothing'
            }
            return Rev_Class_Map[value]



- Next, a function was created to allow the program to make a decision on which move is being displayed by the player.The trained model ouputs an array of four numbers based on how well the input from the camera matches the classes.  The `np.argmax(prediction[:0])` selects the number with the highest likelihood of matching the player input. This selection was then saved as the player choice. If the ``Nothing`` class was selected the user would be asked to make another selection.

      # Makes a prediction from the camera frame given when timer runs out
      def make_a_prediction(self, frame, data, model):
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            prediction = np.argmax(prediction[0])
            self.player_choice = self.move_list(prediction)
            print(f'{self.name} choice is {self.player_choice}')
            if self.player_choice != 'Nothing' and self.player_choice != 'None':
                  ret, frame = cap.read()
                  self.show_text(frame, f"{self.name}'s move: {self.player_choice}", (50,75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_4)
                  cv2.waitKey(500)
                  cv2.imshow('Rock, Paper, Scissors Game', frame)
                  self.get_computer_choice()
            else:
                  self.getting_started()


- The `getting_started()` function was created to allow the player to start the game, continue and stop the game on specific key presses for smooth game play. A five second timer was also added using the `time` module so the player is able to prepare. When the timer runs out, the selection in the frame is read and a move is decided.


           def getting_started(self):
            pressKey = cv2.waitKey(1) & 0xFF
            #Starting the game
            if self.player_wins == 3 or self.computer_wins == 3:
                self.show_text(frame, 'Press P to play again or Q to end game', (100, 225),  cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
                if pressKey == ord('q'):
                    self.computer_wins = 0
                    self.player_wins = 0
                    self.show_text(frame, 'Thanks for playing', (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_4)
                    cv2.waitKey(250)
                    # After the loop release the cap object
                    cap.release()
                    # Destroy all the windows
                    cv2.destroyAllWindows()

                elif pressKey == ord('p'):
                    self.computer_wins = 0
                    self.player_wins = 0
                    self.getting_started()

            elif self.player_wins == 0 and self.computer_wins == 0:
                self.show_text(frame, 'Press S to start or Q to quit', (100, 225),  cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2, cv2.LINE_AA)
                if pressKey == ord('q'):
                        self.show_text(frame, 'Thanks for playing', (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_4)
                        cv2.waitKey(250)
                        # After the loop release the cap object
                        cap.release()
                        # Destroy all the windows
                        cv2.destroyAllWindows()

                elif pressKey == ord('s'):
                              previous = time.time()
                              TIMER  = 5
                              while TIMER > 0:
                                    self.show_text(frame, f'Select Rock, Paper, Scissors:{TIMER}',(50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)         
                                    cv2.waitKey(125)


                                    #Countdown
                                    current = time.time()
                                    if current - previous >= 1:
                                          previous = current
                                          TIMER = TIMER - 1
                        
                              else:                           
                                    self.make_a_prediction(frame, data, model)
            else:
            
                  self.show_text(cap, 'Press C to continue to next round or Q to quit', (25, 250),  cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
                  if pressKey == ord('q'):
                        self.show_text(frame, 'Thanks for playing', (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_4)
                        cv2.waitKey(250)
                        # After the loop release the cap object
                        cap.release()
                        # Destroy all the windows
                        cv2.destroyAllWindows()

                  elif pressKey == ord('c'):
                        previous = time.time()
                        TIMER  = 5
                        while TIMER > 0:
                              self.show_text(frame, f'Select Rock, Paper, Scissors:{TIMER}',(50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)        
                              cv2.waitKey(125)


                              #Countdown
                              current = time.time()
                              if current - previous >= 1:
                                    previous = current
                                    TIMER = TIMER - 1

                        else: 
                              self.make_a_prediction(frame, data, model)
           
- Next, the 'random' module was used to select a random `choice` between Rock, Paper or Scissors. For a better gaming experience, images of each of the three choices were used so the computer's choice would be displayed. Once input from both the player and computer was determined, the program will then decide who wins

            def get_computer_choice(self):
            #Computer Choice for Game
            ret, frame = cap.read()
            cv2.rectangle(frame, (800, 100), (1200, 500), (255, 255, 255), 2)
            self.computer_choice = choice(self.options)
            print(f'The Computer chooses {self.computer_choice}')
            # Shows a picture of the Computer's move
            if self.computer_choice != 'None':
                  icon = cv2.imread(
                  "images/{}.png".format(self.computer_choice))
                  icon = cv2.resize(icon, (400,400))
                  image_np = np.array(icon)
                  normalized_icon = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                  cv2.imshow('RPS Game: Computer Choice', icon)
      
            self.show_text(icon, f"Computer's move: {self.computer_choice}", (400,75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2, cv2.LINE_4)
            cv2.waitKey(500)
            cv2.imshow('Rock, Paper, Scissors Game', frame)
            self.who_wins()
            
 - Finally it is important for the player to be able to visualise the output and decisions of the game. There for a `show_text()` function was added to track the number of rounds, the winner and the choice of each of the players.

        # Displays important information such as the player choice, player move, computer move, computer wins and rounds
        def show_text(self, frame, text, text_position, font, fontsize, color, thickness, linetype):
            ret, frame = cap.read()
            cv2.putText(frame, text, text_position, font, fontsize, (0, 255, 255),thickness,cv2.LINE_AA)
            cv2.putText(frame, f'{self.name}:' + str(self.player_wins), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_4)
            cv2.putText(frame, f'Computer Wins:' + str(self.computer_wins), (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_4)
            cv2.putText(frame, f'Rounds:' + str(self.rounds), (250, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_4)
            cv2.putText(frame, f"{self.name}'s move: {self.player_choice}", (50,75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_4)
            cv2.putText(frame, f"Computer's move: {self.computer_choice}", (400,75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_4)
            cv2.imshow('Rock, Paper, Scissors Game', frame) 
   
   
   ![Working Example 2](https://user-images.githubusercontent.com/102431019/166983947-9dd2fbc6-75b6-4bac-a132-821035d9cca9.png)
     
     The picture above is the working code and how the window should appear after deciding the winner of the round. In the right corner, is the output within the python/Jupyter Notebook

--------------------------------------------------------------------------------------------------------------------------------------------
# Conclusions
 
 **Positives:** Instead of using global variables, I used object- oriented programming to make sure each of the variables I initialized would translate throughout the different functions. I learned that it is easier to break the content up based on the proposed function and group them together using a clearly defined class. Therefore, it is easier to call each of the functions and I know there isn't any confusion in terms of the variables used.
 
 **Future Goals**: Using the teachable machine was easier as it trained the model through the cloud but, in future, I would like to train my own model and I look forward to achieving this goal. I would like to gain more experience using tensorflow as I only used the load_model function in this project.  
**Problem Solving:** In terms of the programming, I found the hardest part was integrating camera into the game but after poring through the opencv documentation I discovered several of my functions required the `ret, frame = cap.read` function to read the screen before it would give an output. Seondly, I also had a problem with coding the option for multiple key press options but discovered `waitKey(1) & 0xFF` function waits for a specific/individual key press. Therefore, it is better to save `waitKey(1) & 0xFF` as a variable allowing the program to differentiate between keys.
