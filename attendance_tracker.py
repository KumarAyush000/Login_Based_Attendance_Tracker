from datetime import datetime

def emp_attendance():           
    employees = {
        "ayush": "pass123",
        "neha": "neha456",
        "samar": "samar789"
    }
    
    attendance_log ={}
    time_log = {}
    
    
    while True:
        input_name = input("Enter your name (if want to quit press 'exit'): ")
        
        if input_name.lower() == "exit":
            print("Exiting the sytsem.")
            break
        elif input_name == "": # if the user presesses ENTER, will skip it
            continue
        elif input_name in attendance_log:
            print(f"{input_name} already marked as Present")
            continue
        elif input_name not in employees:         
            print("User does not exists (if you want to add the user Press : 'y' else press 'n')")
            choice = input("Enter your choice: ")              # allowing user the choice to add a new user in the system
            if choice.lower() == 'y':
                new_pass = input("Enter password for the user: ")
                employees[input_name] = new_pass
                print(f"{input_name} added to the system.")
                attendance_log[input_name] = "Present"
                time_log[input_name] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{input_name} marked as Present.")
            else:
                print("Access Denied")
        else:
            tries = 3        # setting a counter for tries
            while tries != 0:
                ask_pass = input("Enter password: ")
                if ask_pass == employees[input_name]:
                    print("Access Granted")
                    attendance_log[input_name] = "Present"
                    time_log[input_name] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"{input_name} marked as Present")
                    break
                else:
                    tries -= 1
                    if tries == 0:
                        print("No tries left. Access Denied. \n")
                    else:
                        print(f"Incorrect password. Tries left: {tries}")
    # if employess didn't logged in mark them as absent
    for emp in employees:  
        if emp not in attendance_log:
            attendance_log[emp] = "Absent"
            time_log[emp] = "N/A"
    
    # adding employees attendance to atteandance_tog.txt file
    with open("attendance_log.txt", "w")as file:
         for emp in employees:
             file.write(f"{emp} : {attendance_log[emp]} at {time_log[emp]} \n") 
                     
    # Printing final Attendance log
    print("\nAttendance log \n ")
    if attendance_log:
        for emp in employees:
            print(f"{emp} : {attendance_log[emp]}")
    else:
        print(f"No entry exist")
           
                    

emp_attendance()