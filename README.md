:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# CATS VS DOGS
## CS 110 Final Project
### Fall, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

https://replit.com/join/embmmbslcl-michellelu11

[(https://docs.google.com/presentation/d/1Rce6Nk0iEW90KG6szCzRJ1Vt-jYvPCtduDy3YlERhqc/edit?usp=sharing)](#)

### Team: Monkey Squared
#### Nikki Tan and Michelle Lu

***

## Project Description

Space Invaders is a popular game, and our game is influenced by some of the aspects of that game. Our game will be a battle between cats and dogs! The user will be utilizing a dog as their player. The enemy will be the cat. The player will be allowed to move anywhere on the screen. It will shoot at the enemy (there will be multiple enemies postioned randomly throughout the screen) There will also be treats appearing randomly on the screen for power ups.

***    

## User Interface Design

- **Initial Concept**
  [[initial Game Screen] (ect/game_screen.png)](https://replit.com/@MichelleLu11/monkeysquared#etc/game_screen.png)
  - This is the game screen. It includes the player (dog), enemy (cat), and powerup (bone).
  [[initial Menu Screen] (ect/menu_screen.png)](https://replit.com/@MichelleLu11/monkeysquared#etc/menu_screen.png)
  - This is the menu screen. It includes a play button. Upon clicking the play button, the game will start.
    
    
- **Final GUI**
  [Game Screen] (ect/dogattack.png)
  [Click to Begin] (ect/presstobegin.png)
  [Lose Screen] (ect/catvictory.png)
  [Main Menu Screen] (ect/menuScreen2.png)

***        

## Program Design

* Non-Standard libraries
    
* Class Interface Design
    * [Class Interface Design] (ect/classinterface.png)
  
* Classes
    * Weapon - How the player will be able to attack the enemies. The weapon (a ball) will travel upward since the enemies will be coming from the top of the screen.
    * Enemy - The enemies (cat) will arrive from the top of the screen, traveling downward toward the player character (dog). Each will have one life. 
    * Player - The player character (dog) will be free to move anywhere around the screen. The player will start with a strength of 5. If an enemy successfully make it past the player character, the player character will lose a strength. 
    * Booster - Randomly scattered throughout the game, there will be power boosters that appear from the top of the screen and will travel downwards. If the player manages to collide with one, they will either gain a strength.
<<<<<<< HEAD
    * Button - Creates a button that changes color when the mouse hovers over it and changes screens when clicked.



## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * booster.py
    * button.py
    * controller.py
    * enemy.py
    * foldercontents.txt
    * menu.py
    * player.py
    * weapon.py
* assets
    * background.png
    * ball.png
    * cat1.png
    * cat2.png
    * cat3.png
    * cat4.png
    * cat5.png
    * cat6.png
    * cat7.png
    * cat8.png
    * class_diagram.jpg
    * dog.png
    * folercontents.txt
    * grass.png
* etc
    * bone booster.png
    * cat victory.png
    * classinterface.png
    * dog attack.png
    * dog vs cat.png
    * folderecontents.txt
    * game_screen.png
    * gui.png
    * level up.png
    * attack.png
    * begin.png
    * classinterface.png
    * dogvscat.png
    * folderecontents.txt
    * game_screen.png
    * gui.png
    * level.png
    * lost.png
    * menu_screen.png
    * menuScreen2.png
    * milestone2.md
    * milestone3.md
    * presstobegin.png

***

## Tasks and Responsibilities 
* Front End: Nikki and Michelle
* Back End: Nikki and Michelle
* During our first meeting, we brain stormed various ideas and with thoughtful consideration, we were able to come together to finalize our idea. After, we met up together in person multiple times to work on the code side by side. However, majoirity of the time, we worked on the code simultaneously virtually by communicating with each other through text message.

## Testing

*  Because there are so many running parts to the game, we approached each part individually before intergarting them together. We ran through each function alone, then we ran through everything together. Through this method, we were able to debug our code more efficently because there were less lines of code to work with. After we finished debugging each part, we moved on to the next one.

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run program          | GUI window displays Main Menu screen|
|  2                   | Click "Start" Button | Display changes to "Press to begin"|
|  3                   | Press Anywhere on Screen | Display changes to main game screen |
|  4                   | Press up, down, left, or right keyboard arrow | Player moves around the screen according to the arrow pressed |
|  5                   | Press spacebar key   | Player shoots a ball. If the ball comes into contact with a cat, the cat will disappear |
|  6                   | Click on X located at the very right | Display changes to "Press to begin" |