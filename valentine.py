import time
import sys
import random

def slow_print(text, delay=0.05):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def heart_animation():
    hearts = ["💖","❤️","💕","💘"]
    for _ in range(10):
        print(" ".join(random.choices(hearts, k=10)))
        time.sleep(0.2)

def love_message(name):
    messages = [
        f"{name}, kamu itu selalu bikin aku tersenyum 😊",
        f"Setiap detik aku pikirin kamu, {name} 💕",
        f"Kamu spesial banget buat aku, {name} ❤️",
        f"{name}, semoga hari ini kamu selalu bahagia 💖",
        f"Aku suka cara kamu bikin aku jatuh hati terus {name} 💘"
    ]
    return random.choice(messages)

def main():
    slow_print("Selamat datang di Valentine Surprise! 🥰\n")
    your_name = input("Masukkan nama kamu: ")
    partner_name = input("Masukkan nama pasanganmu: ")

    slow_print(f"\nHai {partner_name}, ada sesuatu buat kamu... 😳\n", 0.07)
    time.sleep(1)

    # Heart animation
    heart_animation()

    # Tampilkan pesan romantis acak beberapa kali
    for _ in range(3):
        msg = love_message(partner_name)
        slow_print(msg, 0.07)
        time.sleep(1)

    slow_print(f"\nSemoga kamu senyum ya, {partner_name}! 😘\n", 0.07)
    slow_print("💌 From: " + your_name)
    heart_animation()

if __name__ == "__main__":
    main()