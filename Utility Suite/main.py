from modules import alarm, notes, calculator, password_gen, get_weather, pc_monitoring, file_organizer
from threading import Thread
import time
from pathlib import Path
import random
from bootstrap import startup, getTime

startup()
getTime()
#print("\nType 'exit' to exit application")

while True:
    options = input(
        "\n1. Notes\n2. Calculator\n3. Alarm\n4. Mini-apps\n5. Exit\nChoose an option> "
    ).strip()

    if options in ["notes", "calculator", "mini apps", "mini-apps", "alarm"]:
        print("\nPlease enter the digit associated with your option")
    elif options == "":
        print("\nPlease enter something in\n")
    elif options not in ["1", "2", "3", "4", "5"]:
        print("\nOption does not exist\n")
    else:
        if options == "5":
            break
        
        if options == "1":
            while True:
                options_notes = input(
                    "\n1. Add Note\n2. View Notes\n3. Clear Notes\n4. Exit\nChoose an option> "
                ).strip()

                if options_notes == "":
                    print("\nPlease enter something in\n")
                elif options_notes not in ["1", "2", "3", "4"]:
                    print("\nOption does not exist")
                else:
                    if options_notes == "1":
                        note_input = input("\nAdd note: ")
                        notes.addnote(note_input)
                        print("Note added to notepad.txt")
                    elif options_notes == "2":
                        content = notes.read_notes()
                        if content:
                            print(f"\n{content}\n")
                        else:
                            print("\nNotepad is empty")
                    elif options_notes == "3":
                        notes.clear_notes()
                        print("\nNotepad has been cleared!")
                    elif options_notes == "4":
                        break
        if options == "2":
            while True:
                print("Type 'exit' to exit calculator")

                input_num1 = input("\nEnter First Number: ")
                if input_num1.lower() == "exit":
                    break
                input_num2 = input("Enter Second Number: ")
                if input_num2.lower() == "exit":
                    break
                operation = input("Enter Operator (+ - * /): ")
                if operation.lower() == "exit":
                    break

                if not (input_num1.isdigit() and input_num2.isdigit()):
                    print("Value entered is not a digit")
                elif operation not in ("+", "-", "*", "/"):
                    print("Value entered is not an operator")
                else:
                    input_num1 = int(input_num1)
                    input_num2 = int(input_num2)

                    if operation == "+":
                        calculator.addNumbers(input_num1, input_num2)
                    elif operation == "-":
                        calculator.subtractNumbers(input_num1, input_num2)
                    elif operation == "*":
                        calculator.multiplyNumbers(input_num1, input_num2)
                    elif operation == "/":
                        calculator.divideNumbers(input_num1, input_num2)

        if options == "3":
            while True:
                print("Type 'exit' to exit alarm")
                
                time_seconds = input("\nEnter Seconds (0 for blank): ")
                if time_seconds.lower() == "exit":
                    break
                time_minutes = input("Enter Minutes (0 for blank): ")
                if time_minutes.lower() == "exit":
                    break
                
                if not (time_seconds.isdigit() and time_minutes.isdigit()):
                    print("Value entered is not a digit\n")
                    continue
                
                time_seconds = int(time_seconds)
                time_minutes = int(time_minutes)    
                    
                if time_seconds > 0:
                    Thread(target=alarm.seconds, args=(time_seconds,)).start()
                    print(f"Alarm set for {time_seconds} seconds.\n")
                if time_minutes > 0:
                    Thread(target=alarm.minutes, args=(time_minutes,)).start()
                    print(f"Alarm set for {time_minutes} minutes.\n")
                    
                break
            
        if options == "4":
            while True:
                options_apps = input(
                    "\n1. Password Generator\n2. Weather\n3. File Organizer\n4. System Monitor\n5. Exit\nChoose an option> "
                ).strip()
                
                if options_apps == "1":
                    while True:
                        pass_length = input("\nPassword length: ")
                        
                        if not pass_length.isdigit():
                            print("Not a valid length. Please enter a digit(s)\n")
                        else:
                            pass_length = int(pass_length)
                            if pass_length > 15 or pass_length < 4:
                                print("\nPassword either too small or too large")
                            else:
                                gen_pass = password_gen.generatePassword(pass_length)
                                print(f"\nPassword: {gen_pass}")
                                time.sleep(1)
                            break
                        
                if options_apps == "2":
                    while True:
                        city_choice = input("\nCity: ").strip().lower()
                        
                        if city_choice == "exit":
                            break
                        
                        if city_choice:
                            temp_data_choice = input("Select a temperature unit (Metric / Imperial):").lower()
                            
                            if temp_data_choice in ("imperial", "i"):
                                print("\nType 'exit' to exit weather application")
                                get_weather.fetchWeather(city_choice, "imperial")

                            elif temp_data_choice in ("metric", "m"):
                                print("\nType 'exit' to exit weather application")
                                get_weather.fetchWeather(city_choice, "metric")

                            else:
                                print("\nUnit is invalid")
                                continue
                            
                if options_apps == "4":
                    while True:
                        loop_choice = input("Would you like to view the monitor in live update mode? (y / n): ").strip().lower()
                        
                        if loop_choice not in ("y", "n"):
                            print(f"'{loop_choice}' is an invalid choice\n")
                        elif loop_choice == "n":
                            pc_monitoring.display_usage()
                            break
                        else:
                            pc_monitoring.display_usage_loop_start()
                            break

                if options_apps == "5":
                    break
                
                if options_apps == "3":
                    directory_choice = input("\nChoose a directory to organize: ")
                    file_path = Path(directory_choice)
                    
                    if directory_choice == "exit":
                        break
                    
                    while True:
                        if file_path.exists():
                            #print("Path found")
                            extension_choice = input("\nChoose an extension to organize\n> ")
                            
                            if extension_choice == "exit":
                                break
                            
                            if extension_choice:
                                directory_choice = Path(directory_choice)
                                file_organizer.organizeExtension(directory_choice, extension_choice)
                                print("\nType 'exit' to exit File Organizer")
                                print("------------------------------")
                                time.sleep(random.randint(0, 2))
                        else:
                            print("Path not found")
                            break