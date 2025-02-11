import csv
import os

HIGH_SCORES_FILE = "static/high_scores.csv"

def load_high_scores():
    personal_high_scores = {}
    global_high_scores = {}
    if os.path.exists(HIGH_SCORES_FILE):
        with open(HIGH_SCORES_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = row["User"]
                difficulty = row["Difficulty"]
                score_str = row["Score"]  # Read score as string
                try:
                    score = float(score_str)  # Convert to float instead of int
                except ValueError:
                    print("Error converting score to float for row:", row)  # Debug print
                    continue  # Skip this row if conversion fails
                if user == "global":
                    global_high_scores[difficulty] = score
                else:
                    if user not in personal_high_scores:
                        personal_high_scores[user] = {}
                    personal_high_scores[user][difficulty] = score
    return personal_high_scores, global_high_scores

def save_high_scores(personal_high_scores, global_high_scores):
    with open(HIGH_SCORES_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["User", "Difficulty", "Score"])
        writer.writeheader()
        for user, scores in personal_high_scores.items():
            for difficulty, score in scores.items():
                writer.writerow({"User": user, "Difficulty": difficulty, "Score": score})
        for difficulty, score in global_high_scores.items():
            writer.writerow({"User": "global", "Difficulty": difficulty, "Score": score})
def update_high_scores(user, difficulty, score):
    personal_high_scores, global_high_scores = load_high_scores()
    
    # Update personal high scores
    if user not in personal_high_scores:
        personal_high_scores[user] = {}
    if difficulty in personal_high_scores[user]:
        if score > personal_high_scores[user][difficulty]:
            personal_high_scores[user][difficulty] = score
    else:
        personal_high_scores[user][difficulty] = score
    
    # Update global high scores
    if difficulty in global_high_scores:
        if score > global_high_scores[difficulty]:
            global_high_scores[difficulty] = score
    else:
        global_high_scores[difficulty] = score
    
    # Save high scores
    save_high_scores(personal_high_scores, global_high_scores)
    

def display_high_scores(name , personal_high_scores, global_high_scores):
    print("\nPersonal High Scores:")
    for user, scores in personal_high_scores.items():  # Iterate through users and their scores
        if user != name : continue
        for difficulty, score in scores.items():  # Iterate through difficulty levels and scores for each user
            print(f"{user} - {difficulty}: {score}")
    print("\nGlobal High Scores:")
    for difficulty, score in global_high_scores.items():
        print(f"{difficulty}: {score}")


if __name__ == "__main__":
    while True:
        print("\n1. Update High Scores")
        print("2. View High Scores")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user = input("Enter your username: ")
            difficulty = input("Enter difficulty level: ")
            score = int(input("Enter your score: "))
            update_high_scores(user, difficulty, score)
            print("High scores updated.")
        elif choice == "2":
            personal_high_scores, global_high_scores = load_high_scores()
            display_high_scores(personal_high_scores, global_high_scores)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a valid option.")
