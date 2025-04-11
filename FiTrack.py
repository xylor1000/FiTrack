import os
import math

#food database (Lipa City-based)
local_foods = {
    "Ectomorph": ["Grilled Tilapia", "Brown Rice", "Mongo Stew", "Banana"],
    "Mesomorph": ["Chicken Adobo", "Sweet Potato", "Boiled Eggs", "Papaya"],
    "Endomorph": ["Tinolang Manok", "Cauliflower Rice", "Ampalaya Stir Fry", "Apple"]
}

# workouts
workouts = {
    "Ectomorph": {
        "home": ["Push-ups", "Bodyweight Squats", "Jumping Jacks", "Plank (1 min)"],
        "gym": ["Bench Press", "Deadlift", "Squats", "Barbell Rows"]
    },
    "Mesomorph": {
        "home": ["Burpees", "Lunges", "Push-ups", "Mountain Climbers"],
        "gym": ["Pull-ups", "Leg Press", "Dumbbell Shoulder Press", "Cable Row"]
    },
    "Endomorph": {
        "home": ["Walking in Place", "Wall Sit", "Yoga", "Stair Climbing"],
        "gym": ["Elliptical Machine", "Treadmill", "Stationary Bike", "Rowing Machine"]
    }
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def suggest_workout(body_type, setting):
    return workouts.get(body_type, {}).get(setting, [])

def suggest_meals(body_type):
    return local_foods.get(body_type, [])

def main():
    while True:
        clear()
        print("======================")
        print("     Welcome to FiTrack     ")
        print("======================\n")
        print("1. Start Planning")
        print("2. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            clear()
            print("--- Personal Information ---")
            body_type = input("Enter your body type (Ectomorph/Mesomorph/Endomorph): ").capitalize()
            workout_place = input("Preferred workout setting (home/gym): ").lower()
            
            try:
                weight = float(input("Enter your weight in kilograms: "))
                height = float(input("Enter your height in meters: "))
                bmi = calculate_bmi(weight, height)
                category = get_bmi_category(bmi)

                clear()
                print("--- FiTrack Report ---")
                print(f"Body Type: {body_type}")
                print(f"Workout Setting: {workout_place.capitalize()}")
                print(f"BMI: {bmi} ({category})\n")

                print("Recommended Workouts:")
                for w in suggest_workout(body_type, workout_place):
                    print(f"- {w}")

                print("\nSuggested Meals:")
                for food in suggest_meals(body_type):
                    print(f"- {food}")

                input("\nPress Enter to return to main menu...")

            except ValueError:
                input("Invalid input. Press Enter to return to menu...")

        elif choice == '2':
            print("Thank you for using FiTrack. Stay healthy!")
            break

        else:
            input("Invalid choice. Press Enter to try again...")

if __name__ == '__main__':
    main()
