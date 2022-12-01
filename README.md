:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# CATS VS DOGS
## CS 110 Final Project
### Fall, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

https://replit.com/join/nozsozsdue-michellelu11

<< [link to demo presentation slides](#) >>

### Team: Monkey Squared
#### Nikki Tan and Michelle Lu

***

## Project Description

Our game will be a battle between cats and dogs! The user will have an option to either choose a dog and cat as their player. If the dog is chosen as the player, the enemy will be the cat. If the cat is chosen as the player, the enemy will be the dog. The player will move left and right across the bottom of the screen. It will shoot at the enemy (there will be multiple enemies postioned randomly throughout the screen) to earn inventory (bones or fish), which helps them level up. There will also be treats appearing randomly on the screen for power ups.

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
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
    * << all of your python files should go here >>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

* << Describe your testing strategy for your project. >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | open terminal, enter  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
|  3                   |