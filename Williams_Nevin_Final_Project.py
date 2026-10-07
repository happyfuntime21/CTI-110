#Nevin Williams
#10/7/26
#Final Project
#Draw game

import random
import time

def main():
    #Classes
    classes = ['Cowboy','Indian']
    Cowboy = {'Name' : 'Cowboy','Weapon' : 'Gun'}
    Indian = {'Name' : 'Indian','Weapon' : 'Spear'}
    
    #Input for player class
    self = input('You walk into a bar. Who are you?(Cowboy or Indian)\n')
    
    #Makes it so you can only choose Cowboy or Indian
    while self != 'Cowboy':
        if self == 'Indian':
            break
        else:
            self = input('Please choose a valid choice (Cowboy or Indian)\n')
    
    #Returns player class and gives prompt for player weapons.
    print(f'You are a(n) {self}.')
    self_weapon = input("You\'re told to hand over your weapons at the door. Which weapon do you keep?(Revolver or Knife)\n")
    
    #Makes it so you can only choose Revolver or Knife.
    while self_weapon != 'Revolver':
        if self_weapon == 'Knife':
            break
        else:
            self_weapon = input('Please choose a valid choice (Revolver or Knife)\n')
    
    
    #Creates enemy class and returns them and their weapon.
    enemy = random.choice(classes)
    if enemy == 'Cowboy':
        enemy_class = Cowboy
    if enemy == 'Indian':
        enemy_class = Indian
    print(f'A(n) {enemy} walks into a bar, they have a {enemy_class['Weapon']}.')
    
    
    #Draw prompt.
    print(f'The {enemy} looks you up and down. Be ready to draw!')
    time.sleep(1)
    print('3')
    time.sleep(.5)
    print('2')
    time.sleep(.25)
    print('1')
    
    #Takes amount of time it takes for player to input.
    start_time = time.time()
    input('Press ENTER!')
    end_time = time.time()
    elapsed_time = float(end_time - start_time)
    print(f'Time took to shoot:{elapsed_time}')
    
    #Results for when player uses revolver.
    if self_weapon == 'Revolver':
        if enemy_class == Cowboy:
            if elapsed_time < .5:
                print("You hit the cowboy! You won!")
            else:
                print("The Cowboy hit you. You lost..")
        if enemy_class == Indian:
            if elapsed_time < 1:
                print("You hit the Indian! You won!")
            if elapsed_time > 1 and elapsed_time < 2:
                print('You hit the Indian.. But they hit you. Nobody wins.')
            if elapsed_time > 2:
                print('The Indian hits you with their spear. You lose.')
    
    #Results for when player uses knife.
    if self_weapon == 'Knife':
        if enemy_class == Cowboy:
            if elapsed_time < .5:
                chance_knife = random.randint(1,2)
                if chance_knife == 1:
                    print('You threw your knife and hit the cowboy! You won!')
                if chance_knife == 2:
                    print('You threw your knife and missed. You lost..')
            else:
                print("The Cowboy hit you. You lost..")
        if enemy_class == Indian:
            chance_knife = random.randint(1,2)
            if elapsed_time < 1:
                if chance_knife == 1: 
                    print("You threw your knife and hit the Indian! You won!")
                if chance_knife == 2:
                    print('You threw your knife and missed the Indian. You lose')
            if elapsed_time > 1 and elapsed_time < 2:
                if chance_knife == 1:
                    print('You hit the Indian.. But they hit you. Nobody wins.')
                if chance_knife == 2:
                    print('You threw your knife and missed the Indian. You lose.')
            if elapsed_time > 2:
                print('The Indian hits you with their spear. You lose.')



main()