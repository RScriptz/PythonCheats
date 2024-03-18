# Made By GamingResources (QuePro)

import os
import shutil
from colorama import init, Fore, Style
import time

# Initializing
init()

# ASCII Logo Art :p
Logo = """

                    ███████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗██╗  ██╗███████╗ █████╗ ████████╗
                    ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝
                    ███████╗██║   ██║██████╔╝█████╗  ██████╔╝██║     ███████║█████╗  ███████║   ██║   
                    ╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██║     ██╔══██║██╔══╝  ██╔══██║   ██║   
                    ███████║╚██████╔╝██║     ███████╗██║  ██║╚██████╗██║  ██║███████╗██║  ██║   ██║   
                    ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   
                                               By GamingResources (QuePro)


                                        
                                                    1  - Money Giver      
                                                    2  - Level Giver
                                                    3  - Store Expander
                                                    4  - Storage Expander
                                                    5  - License Unlocker
                                                    6  - Day Count Changer
                                                    7  - Completed Checkouts Giver
                                                    8  - Xp Giver
                                                    9  - Backup File
                                                    10 - Exit Program



"""

# Replace Data Function
def replace_lines(file_path, search_key, new_value):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Find The Number Of The Line To Replace
        for i, line in enumerate(lines):
            if search_key in line:
                old_value = line.split(':', 1)[1].strip()
                comma = ',' if not line.strip().endswith('}') else ''
                lines[i] = line.split(':', 1)[0] + ': ' + new_value.strip() + comma + '\n'
                break
        else:
            print(Fore.RED + f"Error: Key '{search_key}' not found in the file." + Style.RESET_ALL)
            return

        with open(file_path, 'w') as file:
            file.writelines(lines)
        
        print(Fore.GREEN + "Successfully modified." + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.RED + "Error: Save File not found." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

def backup_file(file_path):
    try:
        backup_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Backups')
        os.makedirs(backup_folder, exist_ok=True)
        
        # Get Filename And Extension
        base_name, extension = os.path.splitext(os.path.basename(file_path))
        
        # Backup Filename Handler
        index = 1
        while True:
            backup_file_name = os.path.join(backup_folder, f'{base_name}_Backup{index}{extension}')
            if not os.path.exists(backup_file_name):
                break
            index += 1
        
        shutil.copyfile(file_path, backup_file_name)
        
        print(Fore.GREEN + "Backup created successfully!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

# Main Function
def main():
    save_file_path = os.path.join('C:\\', 'Users', os.getlogin(), 'AppData', 'LocalLow', 'Nokta Games', 'Supermarket Simulator', 'SaveFile.es3')

    if not os.path.exists(save_file_path):
        print(Fore.RED + "Error: Save File doesnt exist, please open the game, create a new save or continue, close the game then try again." + Style.RESET_ALL)
        return

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear Console
        print((Fore.GREEN + Logo))

        choice = input(Fore.GREEN + "Choose an option: " + Style.RESET_ALL)

        if choice == '1':
            while True:
                new_money = input(Fore.GREEN + "Enter the new money value: " + Style.RESET_ALL)
                if new_money.isdigit():
                    replace_lines(save_file_path, '"Money"', new_money)
                    break
                else:
                    print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)
            time.sleep(1)
        elif choice == '2':
            while True:
                new_level = input(Fore.GREEN + "Enter the new level value: " + Style.RESET_ALL)
                if new_level.isdigit():
                    replace_lines(save_file_path, '"CurrentStoreLevel"', new_level)
                    break
                else:
                    print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)
            time.sleep(1)
        elif choice == '3':
            while True:
                new_level = input(Fore.GREEN + "Enter the number of expansions (max 22): " + Style.RESET_ALL)
                if new_level.isdigit() and 0 <= int(new_level) <= 22:
                    replace_lines(save_file_path, '"StoreUpgradeLevel"', new_level)
                    break
                else:
                    print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)
            time.sleep(1)
        elif choice == '4':
            while True:
                new_level = input(Fore.GREEN + "Enter the number of expansions (max 6): " + Style.RESET_ALL)
                if new_level.isdigit() and 0 <= int(new_level) <= 5:
                    replace_lines(save_file_path, '"StorageLevel"', new_level)
                    break
                else:
                    print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)
            time.sleep(1)
        elif choice == '5':
            toggle = input(Fore.GREEN + "Toggle Cheat (Type: on/off): " + Style.RESET_ALL)
            if toggle == 'on':
                replace_lines(save_file_path, '"UnlockedLicenses"', "[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47")
            elif toggle == 'off':
                replace_lines(save_file_path, '"UnlockedLicenses"', "[21")
            else:
                print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)
            time.sleep(1)
        elif choice == '6':
            while True:
                new_level = input(Fore.GREEN + "Enter the number of days: " + Style.RESET_ALL)
                if new_level.isdigit():
                    replace_lines(save_file_path, '"CurrentDay"', new_level)
                    break
                else:
                    print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)
            time.sleep(1)
        elif choice == '7':
            while True:
                new_level = input(Fore.GREEN + "Enter the number of checkouts: " + Style.RESET_ALL)
                if new_level.isdigit():
                    replace_lines(save_file_path, '"CompletedCheckoutCount"', new_level)
                    break
                else:
                    print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)
            time.sleep(1)
        elif choice == '8':
            while True:
                new_level = input(Fore.GREEN + "Enter the amount of xp: " + Style.RESET_ALL)
                if new_level.isdigit():
                    replace_lines(save_file_path, '"CurrentStorePoint"', new_level)
                    break
                else:
                    print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)
            time.sleep(1)
        elif choice == '9':
            backup_file(save_file_path)
            time.sleep(1)
        elif choice == '10':
            print(Fore.GREEN + "Exiting program..." + Style.RESET_ALL)
            time.sleep(2)
            break
        else:
            print(Fore.RED + "Invalid choice. Please choose again." + Style.RESET_ALL)
            time.sleep(1)

if __name__ == "__main__":
    main()

# JustaMarci is gay!
