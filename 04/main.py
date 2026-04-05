# main.py
from game_logic import generate_secret, check_guess, MAX_TRIES
from ui import prompt_guess, display_feedback, ask_play_again, reveal_secret, display_start

def play_round():
    secret = generate_secret()
    tries = 0
    while True:
        guess = prompt_guess()
        tries += 1
        result = check_guess(guess, secret)
        display_feedback(result)
        if result == 'correct':
            break
        if tries >= MAX_TRIES:
            reveal_secret(secret)
            break

def main():
    display_start()
    while True:
        play_round()
        if not ask_play_again():
            print("Paldies par spēli!")
            break

if __name__ == "__main__":
    main()
