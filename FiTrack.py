import math

# Local foods
local_foods = {
    "Ectomorph": ["Oat", "Rice", "Lean Beef/Chicken", "Banana", "Nuts", "Eggs", "Dairy"],
    "Mesomorph": ["Oat", "Rice", "Lean Beef/Chicken", "Banana", "Nuts", "Eggs", "Avocado"],
    "Endomorph": ["Rice", "Chicken Breast", "Sweet Potato", "Avocado", "Chia Seeds"]
}

# Workout Plans
workout_plans = {
    "Ectomorph": {
        "home": {
            "Chest": ["Push-ups", "Incline Push-ups"],
            "Back": ["Superman Exercise", "Reverse Snow Angels"],
            "Legs": ["Bodyweight Squats", "Lunges"],
            "Shoulders": ["Pike Push-ups", "Arm Circles"],
            "Biceps": ["Curls using Water Bottles", "Towel Rows"],
            "Triceps": ["Chair Dips", "Diamond Push-ups"],
            "Core": ["Plank (1 min)", "Bicycle Crunches"]
        },
        "gym": {
            "Chest": ["Incline Dumbbell Press", "Flat Bench Press", "Cable Crossovers"],
            "Back": ["Deadlifts", "Lat Pulldown", "Barbell Rows"],
            "Legs": ["Squats", "Leg Press", "Leg Extensions"],
            "Shoulders": ["Overhead Press", "Lateral Raises", "Rear Delt Flyes"],
            "Biceps": ["Barbell Curls", "Concentration Curls", "Cable Curls"],
            "Triceps": ["Tricep Pushdowns", "Skull Crushers", "Overhead Dumbbell Extension"],
            "Core": ["Cable Crunches", "Hanging Leg Raises"]
        }
    },
    "Mesomorph": {
        "home": {
            "Chest": ["Push-ups", "Wide Push-ups"],
            "Back": ["Back Extensions", "Superman Exercise"],
            "Legs": ["Step-ups", "Wall Sit"],
            "Shoulders": ["Pike Push-ups", "Shoulder Taps"],
            "Biceps": ["Water Bottle Curls", "Isometric Holds"],
            "Triceps": ["Chair Dips", "Overhead Tricep Extensions (Towel)"],
            "Core": ["Mountain Climbers", "Russian Twists"]
        },
        "gym": {
            "Chest": ["Flat Bench Press", "Incline Bench Press", "Chest Fly Machine"],
            "Back": ["Pull-ups", "Seated Cable Rows", "T-Bar Rows"],
            "Legs": ["Leg Press", "Walking Lunges", "Hamstring Curls"],
            "Shoulders": ["Dumbbell Shoulder Press", "Upright Rows", "Face Pulls"],
            "Biceps": ["EZ Bar Curls", "Incline Dumbbell Curls", "Hammer Curls"],
            "Triceps": ["Dips", "Rope Pushdowns", "Close-Grip Bench Press"],
            "Core": ["Leg Raises", "Cable Woodchoppers"]
        }
    },
    "Endomorph": {
        "home": {
            "Chest": ["Wall Push-ups", "Incline Push-ups"],
            "Back": ["Superman Hold", "Reverse Fly (Water Bottles)"],
            "Legs": ["Chair Squats", "Marching in Place"],
            "Shoulders": ["Arm Circles", "Wall Pushes"],
            "Biceps": ["Modified Curls (Water Bottles)", "Resistance Band Curls"],
            "Triceps": ["Wall Triceps Extension", "Towel Pushdowns"],
            "Core": ["Seated Knee Raises", "Standing Oblique Crunches"]
        },
        "gym": {
            "Chest": ["Chest Press Machine", "Incline Dumbbell Press", "Pec Deck Fly"],
            "Back": ["Lat Pulldown", "Assisted Pull-ups", "Seated Rows"],
            "Legs": ["Leg Curl Machine", "Stationary Bike", "Treadmill Walking"],
            "Shoulders": ["Cable Lateral Raises", "Shoulder Press Machine"],
            "Biceps": ["Cable Curls", "Dumbbell Curls", "EZ Bar Preacher Curls"],
            "Triceps": ["Tricep Rope Pushdowns", "Skull Crushers", "Tricep Kickbacks"],
            "Core": ["Plank on Bosu Ball", "Crunch Machine"]
        }
    }
}


# Body type descriptions
body_type_info = {
    "Ectomorph": """The ectomorph is the lucky body type that doesn’t carry much body fat, 
but are unlucky in that their body burns a lot of calories per day normally. 
In order to increase body weight, this type of person would need to increase calorie levels in stages 
until a pound in body weight is being added per week. 

The ectomorph's diet is crucial to increasing muscle tissue from their training. 
They should use a calorie level of 20-25 times their bodyweight in pounds as a starting position. 
Example: a 140 lb lifter would use a starting calorie level of between 2800-3500 calories per day.

Meals should be split into 6-8 meals (including weight gainer drinks) per day, spaced every 2.5 - 3 hours. 
Protein intake should be 25%-30% of total calories; carbohydrates approx. 50%; fats 20%-25%. 
Avoid simple sugars. Prefer low glycemic index foods like brown rice, whole grains, oats, and sweet potatoes. 
Supplement with multivitamins and essential fats from olive oil, nuts, seeds, fatty fish, flaxseeds, and walnuts.

Training Notes:
- Minimize aerobic activity
- Warm-up and cool down (5-10 minutes cardio)
- Use 2-1-2 repetition timing
- Rest 2 mins between sets; 3 mins between exercises
- Train short and intensely
- Get 8+ hours of sleep
- Abs: Mon & Thu or Tue & Fri

Workout Schedule:
- Monday: Chest & Triceps
- Tuesday: Back & Biceps
- Wednesday: Rest
- Thursday: Quads & Hamstrings
- Friday: Shoulders & Calves
- Saturday: Rest
- Sunday: Rest
""",
    "Mesomorph": """Mesomorphs gain muscle easily and typically have an athletic build. 
They respond quickly to training and can lose or gain weight without too much effort.

Diet should focus on a balanced macronutrient intake:
- Protein: 30%-35%
- Carbohydrates: 40%-50%
- Fats: 15%-25%

Meals should be consumed every 3-4 hours, emphasizing lean protein sources, complex carbs (brown rice, oats, sweet potato), 
and healthy fats (avocados, nuts, seeds). Hydration and micronutrient intake should not be overlooked.

Training Notes:
- Mix strength and cardio training
- 3-5 days of weight training and 2-3 days of cardio
- Include high-intensity interval training (HIIT)
- Vary reps and weights for continual progress
- Sleep: 7-8 hours/night

Workout Schedule:
- Monday: Chest & Triceps
- Tuesday: Legs
- Wednesday: Rest or Light Cardio
- Thursday: Back & Biceps
- Friday: Shoulders & Core
- Saturday: Full Body or HIIT
- Sunday: Rest
""",
    "Endomorph": """Endomorphs have a soft, round body and gain fat easily. 
Their metabolism is slower, requiring more effort to lose weight.

Diet:
- Low to moderate carbs, high protein and healthy fats
- Protein: 35%-40%
- Carbs: 30%-40% (choose low GI sources)
- Fats: 20%-30%

Eat 5-6 small meals daily. Focus on lean proteins (fish, chicken), leafy greens, vegetables, healthy oils (olive oil, flaxseed). 
Avoid sugar and processed food. Drink plenty of water.

Training Notes:
- Prioritize cardio: 4-6 sessions/week (30–45 mins)
- Strength train 3-4x/week with moderate weights and higher reps
- Combine HIIT with steady-state cardio
- Consistency and variety are key
- Sleep: 8+ hours for recovery

Workout Schedule:
- Monday: Cardio + Upper Body
- Tuesday: Lower Body + Core
- Wednesday: Cardio
- Thursday: Full Body Strength
- Friday: HIIT
- Saturday: Cardio
- Sunday: Rest
"""
}

def clear():
    print("\033c", end="")

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
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

def display_body_type_info(body_type):
    return body_type_info.get(body_type, "No information available.")

def display_workout_plan(body_type, setting):
    plans = workout_plans.get(body_type, {}).get(setting, {})
    output = ""
    for muscle_group, exercises in plans.items():
        output += f"\n{muscle_group}:\n"
        for ex in exercises:
            output += f"- {ex}\n"
    return output.strip()

def suggest_meals(body_type):
    return local_foods.get(body_type, [])

def main():
    while True:
        clear()
        print("======================")
        print("   Welcome to FiTrack   ")
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
                height_cm = float(input("Enter your height in centimeters: "))
                bmi = calculate_bmi(weight, height_cm)
                category = get_bmi_category(bmi)

                clear()
                print("--- FiTrack Report ---")
                print(f"Body Type: {body_type}")
                print(f"Workout Setting: {workout_place.capitalize()}")
                print(f"BMI: {bmi} ({category})\n")

                print("=== Body Type Info ===\n")
                print(display_body_type_info(body_type))

                print(f"\n=== Recommended Workouts ({workout_place.capitalize()}) ===")
                print(display_workout_plan(body_type, workout_place))

                print("\n=== Suggested Meals ===")
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
