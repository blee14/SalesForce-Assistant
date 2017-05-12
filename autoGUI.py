import pyautogui
import time
import os
import logging

# Changes current working directory to directory that contains all the images
os.chdir("C:\\Users\\blee\\Documents\\References\\Personal Projects\\BLAssistant\\images\\")

# Set Variables for All Images





# Creating a New Case
def createNewCase():
    # Clicks on Menu Dropdown
    pyautogui.moveTo(612, 173)
    pyautogui.click()

    # Clicks on 'Cases' from Dropdown
    pyautogui.moveTo(458, 234)
    pyautogui.click()

    # Clicks on 'New Case'
    time.sleep(2)
    newCase = pyautogui.locateCenterOnScreen("newCase.PNG")
    pyautogui.moveTo(newCase)
    pyautogui.click()
    

    # Clicks on 'Continue' 
    time.sleep(1.8)
    newCaseContinue = pyautogui.locateCenterOnScreen("newCaseContinue.PNG")
    print(newCaseContinue)
    pyautogui.moveTo(newCaseContinue)
    pyautogui.click()
    time.sleep(2)

    # Clicks on 'Save Case'
    newCaseSave = pyautogui.locateCenterOnScreen("newCaseSave.PNG")
    print(newCaseSave)
    pyautogui.moveTo(newCaseSave)
    pyautogui.click()


# TODO Set Case Topics 
class setTopic():

    topic = pyautogui.locateCenterOnScreen("topic.PNG")

##  TopiInstall Error
    def installTopic():
        pyautogui.moveTo(setTopic.topic)
        pyautogui.click(clicks=3)
        pyautogui.moveTo(1132,471)
        pyautogui.click()
        pyautogui.moveTo(1117,535)
        pyautogui.click()
        
##  Activation/Error
    def activationTopic():
        pyautogui.moveTo(setTopic.topic)
        pyautogui.click(clicks=3)
        pyautogui.moveTo(1147,474)
        pyautogui.click()
        pyautogui.moveTo(1117,500)
        pyautogui.click()

       
## Product Configuration Error
    def productTopic():
        pyautogui.moveTo(setTopic.topic)
        pyautogui.click(clicks=3)
        pyautogui.moveTo(1147,474)
        pyautogui.click()
        pyautogui.moveTo(1117,578)
        pyautogui.click()

## License Management Error
    def licMgmtTopic():
        pyautogui.moveTo(setTopic.topic)
        pyautogui.click(clicks=3)
        pyautogui.moveTo(1147,474)
        pyautogui.click()
        pyautogui.moveTo(1117,551)
        pyautogui.click()

class setSubTopic():

##  Sub-Topic : Error
    def errorSubTopic():
        pyautogui.moveTo(1134,490)
        pyautogui.click()
        pyautogui.moveTo(1120,520)
        pyautogui.click()
        pyautogui.moveTo(1210,526)
        pyautogui.click()

##  Instruction
    def instructionSubTopic():
        pyautogui.moveTo(1134,490)
        pyautogui.click()
        pyautogui.moveTo(1120,537)
        pyautogui.click()
        pyautogui.moveTo(1210,526)
        pyautogui.click()

    
# TODO Figure out how to implement license, release, and device
## TODO Choosing release, get user to input which release
## Take a screenshot of what the field will look like
## TODO Choosing license. Have user input a license number
## TODO No license reason. If yes, select reason
def licenseNoInput():
    time.sleep(2)
    licenseForm = pyautogui.locateCenterOnScreen("license.PNG")
    print(licenseForm)
    licenseNo = input('License Number: ')
    pyautogui.moveTo(licenseForm)
    pyautogui.click(clicks=3)
    pyautogui.typewrite(licenseNo) 

## TODO Choosing platform. Have user do it themselves

#Example
# Ask user what the issue is
# depending on input 

def casenew():
    mainTopic = input('''
Whats issue: 
1. Installation
2. Activation
3. Product Configuration
4. License Management
0. Create New Case
''')

    subTopic = input('''
    Sub Topic:
1. Error
2. Instruction
''')

# Make it so that the user can only do this once
# TODO Create GUI for easy use
    if mainTopic == '1' and subTopic == '1':
        setTopic.installTopic()
        setSubTopic.errorSubTopic()
    elif mainTopic == '2' and subTopic == '1':
        setTopic.activationTopic()
        setSubTopic.errorSubTopic()
    elif mainTopic == '3' and subTopic == '1':
        setTopic.productTopic()
        setSubTopic.errorSubTopic()
    elif mainTopic == '4' and subTopic == '1':
        setTopic.licMgmtTopic()
        setSubTopic.errorSubTopic()
    elif mainTopic == '1' and subTopic == '2':
        setTopic.installTopic()
        setSubTopic.instructionSubTopic()
    elif mainTopic == '2' and subTopic == '2':
        setTopic.activationTopic()
        setSubTopic.instructionSubTopic()
    elif mainTopic == '3' and subTopic == '2':
        setTopic.productTopic()
        setSubTopic.instructionSubTopic()
    elif mainTopic == '4' and subTopic == '2':
        setTopic.licMgmtTopic()
        setSubTopic.instructionSubTopic()
    elif mainTopic == '0':
        createNewCase()
    else:
        print('Invalid')
        casenew()
# Run license portion
    licenseNoInput()

createNewCase()
casenew()




    
