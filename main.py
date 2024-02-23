import random


SUITS = {
    'hearts': '❤️',
    'diamonds': '♦️',
    'clubs': '♣️',
    'spades': '♠️'
}


FACE_CARDS = {
    1: '🅰️',  # Ace
    11: 'J',   # Jack
    12: 'Q',   # Queen
    13: 'K'    # King
}


def create_deck():
    deck = []
    for suit in SUITS.keys():
        for value in range(1, 14):
            deck.append((value, suit))
    random.shuffle(deck)
    return deck


def calculate_hand_value(hand):
    total_value = 0
    num_aces = 0
    for card in hand:
        value = card[0]
        if value == 1:
            num_aces += 1
            total_value += 11
        elif value >= 10:
            total_value += 10
        else:
            total_value += value
    while total_value > 21 and num_aces:
        total_value -= 10
        num_aces -= 1
    return total_value


def display_card(card):
    value, suit = card
    if value in FACE_CARDS:
        value = FACE_CARDS[value]
    return f"{value}{SUITS[suit]}"


def display_hand(hand):
    return ' '.join(display_card(card) for card in hand)


def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("🃏 Welcome to Emoji Blackjack! 🃏")
    print("Your hand:", display_hand(player_hand))
    print("Dealer's hand:", display_card(dealer_hand[0]), "🎴")

    while True:
        player_choice = input("Hit or Stand? (h/s): ").strip().lower()
        if player_choice == 'h':
            player_hand.append(deck.pop())
            print("Your hand:", display_hand(player_hand))
            if calculate_hand_value(player_hand) > 21:
                print("Busted! 😞 You lose!")
                break
        elif player_choice == 's':
            break

    if calculate_hand_value(player_hand) <= 21:
        print("Dealer's hand:", display_hand(dealer_hand))
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
            print("Dealer hits:", display_card(dealer_hand[-1]))
        dealer_value = calculate_hand_value(dealer_hand)
        player_value = calculate_hand_value(player_hand)
        print("Dealer's hand:", display_hand(dealer_hand))
        if dealer_value > 21 or player_value > dealer_value:
            print("Congratulations! 🎉 You win!")
        elif player_value < dealer_value:
            print("Sorry, you lose! 😔")
        else:
            print("It's a tie! 🤝")


if __name__ == "__main__":
    play_blackjack()
