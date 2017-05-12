# BLAssistant 
# Command List type of assistant
import dataStructures
import time 
import datetime
import os

# Create differen


def quickOptions():

        # TODO SFT Builder Launcher
        # TODO Finish Website Launcher
        # TODO Case Recording via Excel
        # TODO Desktop Clean Up

        optionsMenu = ("""
1. Reload Hotkey Scripts
2. Search Documentation
3. Toolbox Product Key Search
4. Team Owner by Product
0. Exit
>> """)

        trigger = True
        
        while trigger == True:
            try:
                commandInput = int(input(optionsMenu))
                print(optionsMenu)
                # Reload Hotkey Scripts
                if commandInput == 1: 
                    print('Reloading Hotkey Scripts...')
                    os.system("C:/Users/blee/Documents/References/AHK/shortcuts.bat");
                    time.sleep(1.5)
                    print('Done')
                    

                # Documentation Search
                elif commandInput == 2: 
                    
                    docSearch = input('What Documentation Would you like to Search for?\nTo exit, input "exit"\n')
                    docSearch = docSearch.lower()

                    for documentation in dataStructures.matlabDoc:
                        if docSearch == documentation:
                            webbrowser.open(dataStructures.matlabDoc[documentation])
                        elif docSearch == 'exit':
                            self.quickOptions()
                        else:
                            print('No such documentation exists')
                            quickOptions()


                # Product Key Search            
                elif commandInput == 3:

                    docSearch = input('What Toolbox Product Key are you looking for?\n>>')
                    docSearch = docSearch.lower()

                    for toolbox in dataStructures.toolboxList:
                        if docSearch == toolbox:
                            print('[' + dataStructures.toolboxList[toolbox] + ']')
                            time.sleep(1.5)
                        else:
                            exit

                elif commandInput == 0:
                    trigger = False
 
                else:
                    print('That is not a valid option')
            # Prints Invalid Option if user inputs strings or floats
            except ValueError:
                    print('That is not a valid option')
            

quickOptions()