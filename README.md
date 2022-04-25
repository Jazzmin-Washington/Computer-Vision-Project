# Computer-Vision-Project
Using a teachable machine, we trained a machine to recognize four images: Rock, Paper, Scissors and Nothing. 
We will then use our trained model and install dependicies. Afterward, we will code for the game of Rock, Paper and Scissors using if/while/else statements. Finally, we will proceed to play Rock, Paper, Scissors with the computer.


**Milestone 1: Training the model (Completed):**
Using teachablemachine.withgoogle.com, we trained an image model with four different classes: Rock, Paper, Scissors and Nothing. The trained model was then downloaded via TensorFlow and saved in a directory.
  
Example of Scissors: ![image](https://user-images.githubusercontent.com/102431019/163892362-aac51e8e-6d17-4942-9756-fc1d1f4a8211.png)
 
 
 Example of Paper: ![image](https://user-images.githubusercontent.com/102431019/163892481-60a1d385-ffc3-43ed-858f-c6f1b342b956.png)
 
 
 Example of Rock: ![image](https://user-images.githubusercontent.com/102431019/163892568-2eacf2ef-76d2-4a2b-a8dd-66d79f1b9bc0.png)
 
 
**Milestone 2: Installing the dependencies (Completed):**
A new virtual environment was created using conda. Within this new environment, opencv-python, TensorFlow, and ipykernel libraries were downloaded using the commandline. The model was then run on my local machine using VS Code inside a Jupyter notebook. This model makes variable predictions containing the output of the model. Each element in the output corresponds to a different class. 

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
      
To train the model on my local system using VSCode:
    ![image](https://user-images.githubusercontent.com/102431019/164271823-88b6241f-90f2-4675-8ddc-6d0390dff9d1.png)

Keep in mind, the Jupyter Notebook should be created in the same directory as the trained model you want to use. Be sure to use the conda environment as the interpreter for the Jupyter Notebook.
      
    
  
**Milestone 3: Creating the Rock, Paper, Scissor Game (Not Completed):**
A command for user input was made to store the user's and the computer's choices using the random with python. Using while, if, else statements, a wiinning structure was created so the program can decide who wins. This code was then encompassed in a function to similate a game of Rock, Paper, Scissors.
  
**Milestone 4: Putting it together (Not Completed):**
Finally, code to use the webcam was then combined to previously designed play function which requires the user to put an input of Rock, Paper or Scissors and output the computer vision model. A countdown was added foe easy gameplay.
