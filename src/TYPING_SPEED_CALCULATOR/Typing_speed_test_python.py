from time import time, sleep
import random
import string
import pygame
import HIghScore 

# Initialize pygame
pygame.init()

# Load sound effects
keypress_sound = pygame.mixer.Sound("Media/quick-mechanical-keyboard.mp3")
error_sound = pygame.mixer.Sound("Media/ERRORplayernocanselect.mp3")

def generate_random_text(difficulty):
    if difficulty == "easy":
        num_words = random.randint(5, 10)
        max_chars = 6
    elif difficulty == "medium":
        num_words = random.randint(10, 15)
        max_chars = 9
    elif difficulty == "hard":
        num_words = random.randint(15, 20)
        max_chars = 12
    text = ""

    for _ in range(num_words):
        num_chars = random.randint(1, max_chars)
        word = ''.join(random.choice(string.ascii_letters) for _ in range(num_chars))
        text += word + " "

    return text.strip()

def display_typing_text(text):
    print("\n" + text + "\n")

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Test starting in {i} seconds...")
        sleep(1)
    print("Go!\n")

def play_keypress_sound():
    keypress_sound.play()


def calculate_accuracy(expected_text, user_input):
    total_chars = len(expected_text)
    correct_chars = sum(1 for r, u in zip(expected_text, user_input) if r == u)
    accuracy = (correct_chars / total_chars) * 100
    return accuracy

def calculate_wpm(text, start_time, end_time):
    total_words = len(text.split())
    time_taken = end_time - start_time
    minutes_taken = time_taken / 60
    wpm = total_words / minutes_taken
    return wpm

def calculate_kpm(text, start_time, end_time):
    total_chars = len(text)
    time_taken = end_time - start_time
    minutes_taken = time_taken / 60
    kpm = total_chars / minutes_taken
    return kpm

def display_result(name, speed, errors, accuracy, wpm, kpm, error_distribution , score):
    print("\nTyping Test Result for", name)
    print(f"Speed: {speed} w/sec")
    print(f"Errors: {errors}")
    print(f"Accuracy: {accuracy}%")
    print(f"WPM: {wpm}")
    print(f"KPM: {kpm}")
    print("Error Distribution:")
    for char, count in error_distribution.items():
        print(f"'{char}': {count}")
    print(f"Your Overall Score: {score}")
    print()

def calculate_score(accuracy, wpm, kpm, errors):
    # Define a scoring formula based on your preferences
    score = (accuracy / 100) * (wpm + kpm) - (errors * 2)
    return score

if __name__ == "__main__":
    print("nKUMAR TYPING SPEED CALCULATOR".center(50, "="))

    # Set the display to be initialized in the main loop
    pygame.display.init()

    while True:
        check_ready = input("\n\nReady to Test? (yes/no): ").lower()
        if check_ready == "no":
            break
        if check_ready != "yes":
            print("Wrong Input")
            continue
        
        name = input("\nEnter your name: ")
        difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()

        if difficulty not in ["easy", "medium", "hard"]:
            print("Invalid difficulty level. Please choose from easy, medium, or hard.")
            continue


        selected_text = generate_random_text(difficulty)

        display_typing_text(selected_text)

        countdown_timer(3)

        start_time = time()

        print("\nStart typing:")
        play_keypress_sound()  # Play keypress sound after the first character input
        user_input = input("")
        end_time = time()

        # Pad user input if it's shorter
        user_input += ' ' * (len(selected_text) - len(user_input))

        error_count = sum(1 for r, u in zip(selected_text, user_input) if r != u)
        accuracy = calculate_accuracy(selected_text, user_input)
        wpm = calculate_wpm(selected_text, start_time, end_time)
        kpm = calculate_kpm(selected_text, start_time, end_time)
        
        # Error distribution
        error_distribution = {}
        for char in set(selected_text):
            error_distribution[char] = selected_text.count(char) - user_input.count(char)

        
        score = calculate_score(accuracy, wpm, kpm, error_count)
        display_result(name, round(len(selected_text) / (end_time - start_time), 2), error_count, round(accuracy, 2), round(wpm, 2), round(kpm, 2), error_distribution , score)
        
        HIghScore.update_high_scores(name , difficulty , score)
        
    show_high_scores = input("\nDo you want to see the high scores? (yes/no): ").lower()
    if show_high_scores == "yes":
        personal_high_scores, global_high_scores = HIghScore.load_high_scores()
        HIghScore.display_high_scores(name , personal_high_scores, global_high_scores)
    # Quit pygame when done
    pygame.quit()
