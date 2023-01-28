# Hangman

[View deployed site here](https://linber-hangman-pp3.herokuapp.com/)

This is my third project assignment during the Full Stack Software Developer course. It comes in the form of a hangman game which is ran in the python terminal.

![game on different devices](https://github.com/Linber93/Hangman_PP3/blob/main/readme-assets/am_i_responsive_pp3.png)

## Objective

The objective of the game is for the user to guess the correct word chosen by the computer by guessing individual letters. The computer will display a series of dashes representing the letters in the word and the user will have a set number of chances to guess the correct letters. If the user successfully guesses all of the letters in the word, they win the game. If the user reaches the maximum number of allowed incorrect guesses, they lose the game. The game also includes a feature to allow the user to quit the game at any time.


### Features

- __Main Menu__
 - will on launch display a welcome message and ask the user if they would like to
   read the instructions before starting the game.

![Main menu](https://github.com/Linber93/Hangman_PP3/blob/main/readme-assets/game_ui_pp3.png)

- __Navigation__
 - Navigation the menus if done via answering the questions asked with the letter "y" for yes, and "n" for no

- __instructions__
 - describes all the rules, instructions and options

![instructions](https://github.com/Linber93/Hangman_PP3/blob/main/readme-assets/instructions_pp3.png)

- __Word selection__
 - Word are selected randomly from a Google Sheet.

- __Game interface__
 - Displays dashes as a representation of the letter in the selected word.
 - Guesses will be transformed to uppercase and checked against the selected word.
 - On incorrect guesses the user will shown the amount of tries left before the game ends
 - On an correct guess the letter will be revealed

![incorrect guess]https://github.com/Linber93/Hangman_PP3/blob/main/readme-assets/Incorrect_guess_pp3.png)
![correct guess](https://github.com/Linber93/Hangman_PP3/blob/main/readme-assets/correct_guess_pp3.png)

- __Exiting game__
 - The game can be exited at all times by inputing the keyword "quit" in the terminal.


## UX

### The ideal user is looking for:
 1. An easy way to navigate the menu and start the game.
 2. Easy to understand instructions on how to play.
 3. Clear instructions in eventuall error messages when it expects a specific kind of input.
 4. Clear indications on how many tries the user has left.
 5. Replayable games without relaunching the script.
 6. A relaxing and a fun time playing the game running as expected.




## Testing

### Features tested
| Test subject | test action | Expected Result | Result |
| ----------- | ----------- | ----------| ----------|
| launching game| run the script | game launches and displays the title | PASSED |
| Navigation | navigate the menu using "y" and "n" | only accept the prompted responds | PASSED |
| Game Interface | navigate through menu and start game | displays a dashed reprensentation of the word and prompts user to guess a letter. | PASSED |
| Incorrect guesses | guess letters until a faulty one is found | terminal displays that the word was incorrect and shows the amount of incorrect tries left until game ends | PASSED |
| Correct guesses | guess letters until a correct one is found | the dashes representing that letter is removed and the letter is revealed | PASSED |
| game finished | play untill the game ends either by a loss or win | displays a success message and asks the user if they want to play again | PASSED |
| quit game | run the script and input "quit" into the terminal | program terminates | PASSED |
### Validator testing

- Python code Validated using the pep8. [PEP8](https://pep8ci.herokuapp.com/)

## Deployment

- The website has been deployed to Heroku. The process of moving the site to Heroku includes:

  1. Logging into Heroku
  2. Selecting "Create new app".
  3. Choosing a name and location for the app.
  4. Clicking "Create app".
  5. Going to the "settings" tab.
  6. Clicking "Reveal Config Vars".
  7. Adding a Config Var in the Heroku settings, with the key PORT and the value 8000.
  8. Scrolling down to "Buildpacks".
  9. Clicking "Add Buildpack".
  10. Adding "python" and clicking save.
  11. Adding "nodejs" and clicking save.

- It is not possible to automate deployment from GitHub using Heroku, instead you can use the following steps to deploy using Gitpod workspace:

  1. Open terminal.
  2. Run the command: heroku login -i
  3. Find the name of your app on Heroku.
  4. Run the command: heroku apps
  5. Set up the Heroku remote by running the command: heroku git:remote -a <app_name> (Replace <app_name> with your actual app name and remove the <> characters)
  6. Add and commit any changes to your code if applicable
  7. Run the command: git add . && git commit -m "Deploy to Heroku via CLI"
  8. Push the code to both GitHub and Heroku
  9. Run the command: git push origin main
  10. Run the command: git push heroku main

 [View deployed site here](https://linber-hangman-pp3.herokuapp.com/)

## Forking
Forking the GitHub Repository

forking the GitHub Repository allows you to make a copy of the original repository in your own GitHub account. This creates the possibility to view and make changes without the risk of affecting the original.

1. Log into GitHub and locate the GitHub Repository.
2. At the top right you will see a "Fork" button.
3. You should now have a new copy of the original repository in your own GitHub account.

## Cloning
 Creating a local clone
 1. Log into GitHub and locate the GitHub Repository.
 2. There is a button named "<>code" a dropdown will provide you with an option to download it as a zip file or clone it directly using HTTPS but copying provided URL
 3. Open Gitbash in your terminal
 4. Navigate to the directory which you want the clone to be located
 5. Type git clone, and then paste the URL you copied in step 2. For example, "git clone https://github.com/your-username/your-repository".
 6. Press enter, and the repository will be cloned to your working directory.



## External technologies used
 - [MDN](https://developer.mozilla.org/en-US/) - external resource to learn more about python
 - 
 - [Gitpod](https://www.gitpod.io/) - The developer used Gitpod to develop this project
 - [Github](https://github.com/) - used to store and save my project during the development process.
 - [heroku](https://heroku.com/) - Used to host and publish the project.
 - python - Language used for development
 - Google Sheets - used as an external data base for the word library.



## Credits
### Content
 - Content was created and assessed by Linus Berger.

### Acknowledgements
 - I received some ideas on design and how to clean up my code from friends and relatives
 - My Mentor Brian Macharia for guiding me through this project and giving valuable tips and advice throughout the development process.