from workout_planner import WorkoutPLanner

def main():
    planner = WorkoutPLanner()

    while True:
        print("--------WORKOUT PLANNER--------\n")
        print("[S]tart\t[E]nd")
        user_choice = input("Enter choice: ")

        if user_choice.upper() == "S":
            get_weight = float(input("\nEnter your weight: "))
            get_height = float(input("Enter your height (CM): "))
            user_bmi = planner.calc_bmi(get_weight, get_height)

            get_age = int(input("Enter your age: "))

            if 15 < get_age <= 40:
                print("\nWhat is your current status?\n")
                get_status = int(
                    input("[1] Beginner\t[2] Has experience in working out: "))
                print("\n")

                if get_status == 1:
                    user_goal = 'S'
                    if user_bmi < 18.5:
                        print(planner.workout_program(get_status, user_goal))
                        print(
                            "\nSince your BMI indicates that you are UNDERWEIGHT, "
                            "I suggest you to have a calorie surplus and minimize cardio in order to gain weight.\n")
                    elif 18.5 <= user_bmi < 25:
                        print(planner.workout_program(get_status, user_goal))
                        print("\nYour BMI indicates that you are of NORMAL weight, "
                              "I suggest you to eat your calorie maintenance while "
                              "eating more protein in order to help build muscle.\n")
                    elif user_bmi >= 25:
                        print(planner.workout_program(get_status, user_goal))
                        print("\nSince your BMI indicates that you are OVERWEIGHT, "
                              "I suggest you to have a calorie deficit and incorporate more cardio "
                              "in addition to these exercises in order to lose fat.\n")

                elif get_status == 2:
                    print("What is your goal?\n")
                    user_goal = input(
                        "[S]trength training\t[M]uscle Building: ")
                    if user_goal.upper() == 'S':
                        if user_bmi < 18.5:
                            print(planner.workout_program(
                                get_status, user_goal))
                            print(
                                "\nSince your BMI indicates that you are UNDERWEIGHT, "
                                "I suggest you to have a calorie surplus and minimize "
                                "cardio in order to gain weight.\n")
                        elif 18.5 <= user_bmi < 25:
                            print(planner.workout_program(
                                get_status, user_goal))
                            print(
                                "\nYour BMI indicates that you are of NORMAL weight, "
                                "I suggest you to eat your calorie maintenance while "
                                "eating more protein in order to help build muscle.\n")
                        elif user_bmi >= 25:
                            print(planner.workout_program(
                                get_status, user_goal))
                            print("\nSince your BMI indicates that you are OVERWEIGHT, "
                                  "I suggest you to have a calorie deficit and incorporate "
                                  "more cardio in addition to these exercises in order to lose fat.\n")

                    elif user_goal.upper() == 'M':
                        if user_bmi < 18.5:
                            print(planner.workout_program(
                                get_status, user_goal))
                            print(
                                "\nSince your BMI indicates that you are UNDERWEIGHT, "
                                "I suggest you to have a calorie surplus and minimize "
                                "cardio in order to gain weight.\n")
                        elif 18.5 <= user_bmi < 25:
                            print(planner.workout_program(
                                get_status, user_goal))
                            print(
                                "\nYour BMI indicates that you are of NORMAL weight, "
                                "I suggest you to eat your calorie maintenance while "
                                "eating more protein in order to help build muscle.\n")
                        elif user_bmi >= 25:
                            print(planner.workout_program(
                                get_status, user_goal))
                            print("\nSince your BMI indicates that you are OVERWEIGHT, "
                                  "I suggest you to have a calorie deficit and incorporate more "
                                  "cardio in addition to these exercises in order to lose fat.\n")

                    else:
                        print("Enter a valid input.")

            else:
                planner.age_restriction(get_age)

        elif user_choice.upper() == "E":
            print("\nThank you for using this workout planner!")
            break
        else:
            print("\nPlease enter a valid choice.")


if __name__ == "__main__":
    main()
