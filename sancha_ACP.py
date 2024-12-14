from datetime import datetime 

#user will choose 1 or 2
def choices(): 
    while True:
        print("------------------------------------------------------------------------------------------")
        print("\t\tGreetings! Please choose your option.")
        print("\t[1] > Log Blood Pressure")
        print("\t[2] > Exit")
        choice = int(input("\t\nEnter here:"))
        
        if choice == 1:
            blood_pressure()
        elif choice == 2:
            print("Thank you for using, Your Heart Matters: Blood Pressure Log is always ready to make heart health your priority.")
        else:
            print("Invalid! Option is only 1 or 2.")    

#function where can find the details, readings, calculation, printing of data
def blood_pressure(): 
    print("----------------------------------------------------------------------------------------------")
    print("\t\tWelcome to Blood Pressure Log where Your Heart Matters!")
    print("----------------------------------------------------------------------------------------------")

    date_time = datetime.now()
    print(f"\t\tCurrent date and time: {date_time}")
    user_id = input("\nUser ID: ")
    name = input("Name: ")
    age = int(input("Age: "))

    print("----------------------------------------------------------------------------------------------")
    print(f"\tLet's log your blood pressure for today {name}")

    first_systolic = int(input("First Systolic: "))
    first_diastolic = int(input("First Diastolic: "))

    second_systolic = int(input("Second Systolic: "))
    second_diastolic = int(input("Second Diastolic: "))

# Calculation
    average_1 = (first_systolic + second_systolic) / 2
    average_2 = (first_diastolic + second_diastolic) / 2

# Range
    if average_1 < 120 and average_2 < 80:
        result = "Normal Blood Pressure"
        advice = "Healthy diet, regular exercise, take medication as prescribed."
    elif 120 <= average_1 <= 129 and average_2 < 80:
        result = "Elevated Blood Pressure"
        advice = "Stay hydrated, limit processed foods/sugary drinks, take medication as prescribed."
    elif 130 <= average_1 <= 139 or 80 <= average_2 <= 89:
        result = "Pre-Hypertension"
        advice = "Eat plenty of fruits, vegetables, whole grains, fish, and low-fat dairy, take medication as prescribed."
    elif  average_1  >= 140  or  average_2  >= 90 :  
        result = "High Blood Pressure"
        advice = "Reduce sodium intake, avoid stress, and consult a doctor, take medication as prescribed."
    elif average_1 >= 180 or average_2 >= 120:
        result = "Hypertensive Crisis!!"
        advice = "Stay calm and monitor the person's vital signs, seek for a doctor immediately!"
    else:
        result = "Invalid result."
        advice = "Invalid advice."

    print("----------------------------------------------------------------------------------------------")
    print(f"\t\t{date_time}")
    print(f"\nFirst Systolic and Diastolic: {first_systolic}/{first_diastolic}")
    print(f"Second Systolic and Diastolic: {second_systolic}/{second_diastolic}")

    print("==========================")
    print(f"Overall Result: {average_1:.1f}/{average_2:.1f}")
    print("==========================")

    print(f"Result: {result}")
    print(f"Advice: {advice}")
    print("----------------------------------------------------------------------------------------------")
    print("\t\tThank you for using the Blood Pressure Log.")
    print("Your Heart Matters: Blood Pressure Log is ready to monitor your blood pressure anytime.")

choices()
blood_pressure()
