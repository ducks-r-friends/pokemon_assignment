import random
import requests

p1_deck = []
p2_deck = []


def fetch_pokemon(id):
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(id)
    response = requests.get(url)

    if response.status_code < 200 or response.status_code >= 300:
        exit(2)

    data = response.json()

    return {
        'id': data['id'],
        'name': data['name'],
        'height': data['height'],
        'weight': data['weight'],
        'moves': len(data['moves']),
        'base_experience': data['base_experience'],
    }


def output_stats(pokemon):
    print(pokemon)
    return


while True:
    p1 = random.randint(1, 151)
    p2 = random.randint(1, 151)
    pokemon1 = fetch_pokemon(p1)
    pokemon2 = fetch_pokemon(p2)

    print(
        "'Welcome Human. It's time to play your pokemon in a winner takes all battle. The Pokemon you will play is: {}'".format(
            pokemon1['name']))

    output_stats(pokemon1)

    user_stat = input('Which stat do you want to play: ').lower()

    if user_stat not in pokemon1.keys():
        print('invalid move')
        continue
    elif user_stat == 'id':
        print('invalid move')
        continue
    elif user_stat == 'name':
        print('invalid move')
        continue

    print('LET BATTLE COMMENCE!')
    print('>>>>>>>>>>>>>>>>>>>>>')
    print('')

    if user_stat == 'height':
        if pokemon1['height'] > pokemon2['height']:
            print('you win')
            p1_deck.append(pokemon2['name'])
        else:
            print('you lose')
            p2_deck.append(pokemon1['name'])

    elif user_stat == 'weight':
        if pokemon1['weight'] > pokemon2['weight']:
            print('you win')
            p1_deck.append(pokemon2['name'])
        else:
            print('you lose')
            p2_deck.append(pokemon1['name'])

    elif user_stat == 'base_experience':
        if pokemon1['base_experience'] > pokemon2['base_experience']:
            print('you win')
            p1_deck.append(pokemon2['name'])
        else:
            print('you lose')
            p2_deck.append(pokemon1['name'])

    elif user_stat == 'moves':
        if pokemon1['moves'] > pokemon2['moves']:
            print('you win')
            p1_deck.append(pokemon2['name'])
        else:
            print('you lose')
            p2_deck.append(pokemon1['name'])

    else:
        print("'It's a draw. Keep your Pokemon to battle another day")
        p1_deck.append(pokemon1['name'])
        p2_deck.append(pokemon2['name'])

    print('player 2 played:')
    output_stats(pokemon2)

    play_again = input(" Do you want to play again? Yes/No ").lower()
    if play_again == "yes":  # go back to the top
        continue
    else:
        break

print('\n')
print('Thanks for playing!\n')

if len(p1_deck) > len(p2_deck):
    print('Player 1 Wins!')
elif len(p2_deck) > len(p1_deck):
    print('Player 2 Wins!')
else:
    print('It\'s a draw!')
