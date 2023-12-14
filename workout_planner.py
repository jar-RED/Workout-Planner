class WorkoutPLanner:
    def __init__(self):
        self.bmi = 0
        self.exercise_program = []
        self.exercises = (
            "Push ups",
            "Decline push ups",
            "Pike push ups",
            "Lateral raises",
            "Triceps extensions",
            "Pull ups",
            "Bicep curls",
            "Squats",
            "Bulgarian split squats",
            "Crunches",
        )

    def calc_bmi(self, weight, height):
        height_in_meters = height/100
        self.bmi = weight / (height_in_meters*height_in_meters)
        return self.bmi

    def age_restriction(self, age):
        if 10 < age <= 15:
            print("\nI do not recommend you to start working out yet, "
                  "however, you can do physical activities that are aerobic to be fit.\n")
        elif age > 40:
            print("\nI recommend you to do regular light exercises, "
                  "stretching routines and having a healthy diet in order to stay fit.\n")
        elif age < 0:
            print("\nEnter a valid age.")
        else:
            print("\nI suggest you to not do a set of physical activities at that age.\n")

    def workout_program(self, status, goal):
        if status == 1 and goal.upper() == 'S':
            index_of_exercise = [0, 2, 5, 7, 9]
            for index in index_of_exercise:
                specific_exercises = self.exercises[index]
                self.exercise_program.append(specific_exercises)

            print("\n============ HERE IS YOUR WORKOUT PROGRAM ============\n")
            for exercise in self.exercise_program:
                print(f"{exercise} - 2 sets until failure (2 minutes rest)")
            print("\n======================================================")
            print(
                "\nDo these set of exercises every other day in order for your body to have a resting period day\n")

            self.exercise_program = []

        elif status == 2:
            for index in range(len(self.exercises)):
                specific_exercises = self.exercises[index]
                self.exercise_program.append(specific_exercises)

            if goal.upper() == 'S':
                print("\n============ HERE IS YOUR WORKOUT PROGRAM ============\n")
                print("WORKOUT A\n")
                for index in range(len(self.exercise_program)):
                    if index < 5:
                        exercise = self.exercise_program[index]
                        print(
                            f"{exercise} -  4 sets until failure (3 minutes rest)")
                print("\n======================================================")
                print("\nWORKOUT B\n")
                for indexb in range(len(self.exercise_program)):
                    if indexb > 4:
                        exerciseb = self.exercise_program[indexb]
                        print(
                            f"{exerciseb} -  4 sets until failure (3 minutes rest)")
                print("\n======================================================")
                print("Workout A and B are to be done consecutively, "
                      "not at once. For example: M - Workout A | T - Workout B, "
                      "then followed by a rest day, then repeat.")
                print(
                    "Since you are training for strength, I recommend you to add weights "
                    "according to your preference while doing these exercises.\n")

                self.exercise_program = []

            elif goal.upper() == 'M':
                print("\n============ HERE IS YOUR WORKOUT PROGRAM ============\n")
                print("WORKOUT A\n")
                for index in range(len(self.exercise_program)):
                    if index < 5:
                        exercise = self.exercise_program[index]
                        print(
                            f"{exercise} -  3 sets until failure (1 minute rest)")
                print("\n======================================================")
                print("\nWORKOUT B\n")
                for indexb in range(len(self.exercise_program)):
                    if indexb > 4:
                        exerciseb = self.exercise_program[indexb]
                        print(
                            f"{exerciseb} -  3 sets until failure (1 minute rest)")
                print("\n======================================================")
                print("Workout A and B are to be done consecutively, "
                      "not at once. For example: M - Workout A | T - Workout B, "
                      "then followed by a rest day, then repeat.\n")

                self.exercise_program = []
