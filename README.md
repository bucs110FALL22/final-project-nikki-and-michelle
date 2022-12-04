:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# CATS VS DOGS
## CS 110 Final Project
### Fall, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

https://replit.com/join/embmmbslcl-michellelu11

<< [link to demo presentation slides](#) >>

### Team: Monkey Squared
#### Nikki Tan and Michelle Lu

***

## Project Description

Space Invaders is a popular game, and our game is influenced by some of the aspects of that game. Our game will be a battle between cats and dogs! The user will be utilizing a dog as their player. The enemy will be the cat. The player will move left and right across the bottom of the screen. It will shoot at the enemy (there will be multiple enemies postioned randomly throughout the screen) to earn inventory (bones), which helps them level up. There will also be treats appearing randomly on the screen for power ups.

***    

## User Interface Design

- **Initial Concept**
  - https://replit.com/@MichelleLu11/monkeysquared#game_screen.JPEG
    - This is the game screen. It includes the player (dog), enemy (cat), and powerup (bone).
  - https://replit.com/@MichelleLu11/monkeysquared#menu_screen.JPEG
    - This is the menu screen. It includes a play button. Upon clicking the play button, the game will start.
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
  * pygame
  * random
    
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
           
* Class Interface Design
    * [class diagram](https://drive.google.com/file/d/1McgleuoHiwyq2lsYEGvpBBlLcfoMIo3N/view?usp=sharing)
  
* Classes
    * Ability - How the player will be able to attack the enemies. The ability will travel upward since the player character will be located at the bottom of the screen and the enemies will be coming from the top.
    * Background - Moving grass-like background that will move upwards, giving the impression that the player character is advancing forward. 
    * Enemy - The enemies (either cat or dog, the opposite of the player character) will arrive from the top of the screen, traveling downward toward the player character. Each will have one life. 
    * Player - The player character (either cat or dog) will be located at the bottom of the screen, and it can only move sideways. The player will have 3 lifes. If an enemy successfully make it past the player character, the player character will lose a life. 
    * Powerup - Randomly scattered throughout the game, there will be power boosters that appear from the top of the screen and will travel downwards. If the player manages to get one, they will either gain a life or get a boost in their ability. 


## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * controller.py
    * enemy.py
    * player.py
    * weapon.py
* assets
    * background.png
    * ball.png
    * cat.png
    * class_diagram.jpg
    * dog.png
    * folercontents.txt
    * grass.png
    * start.png
* etc
    * folderecontents.txt
    * milestone2.md
    * milestone3.md

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
|  1                   | open terminal, enter  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
|  3                   |