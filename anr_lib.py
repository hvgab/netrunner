import json
import pprint
import random
import deckbuilder

# Runner setup
runner = {
    "identity": "",
    "deck": [],
    "discard": [],
    "programs": [],
    "hardware": [],
    "resource": [],
    "clicks": 4,
    "clicks_left": 4,
    "credits": 5,
    "hand": []
}

# Corp Setup
corp = {
    "identity": "",
    "deck": [],
    "discard": [],
    "servers": [],
    #	1,2,3,osv shields
    #	asset/agenda (1)
    #	upgrades
    "clicks": 3,
    "clicks_left": 3,
    "credits": 5,
    "hand": []
}


def ppprint(stuff):
    pp = pprint.PrettyPrinter(depth=2)
    #	pp.pprint(stuff.encode('cp850', errors='replace'))
    pp.pprint(stuff)
    #print (stuff.encode('cp850', errors='replace'))


def print_deck_short(deck):
    print('deck size: ' + str(len(deck)))
    print('hand/deck: ')
    for card in deck:
        print(card['title'] + ' - ' + card['type'] + '/' + card['subtype'])


def draw_a_card(from_deck, to_deck):
    to_deck.append(from_deck.pop())
    print(to_deck[0]['faction'] + ' ' + to_deck[0]['side'] + ' draws a card')


def play_card(card):
    print(card['side'] + ' plays ' + card['title'])


def print_card(card):
    # corp cards : identities, operations, agendas, ice, upgrades, and assets.
    # identities, hardware, resources, programs, and events.
    print('title - ' + card['title'])
    print('type - ' + card['type'])
    print('subtype - ' + card['subtype'])
    print('text - ' + card['text'])
    print('cost - ' + str(card.get('cost', 'NA')))
    print('faction_cost - ' + str(card.get('faction_cost', 'NA')))
    print('memoryunits - ' + str(card.get('memoryunits', 'NA')))
    print('strength - ' + str(card.get('strength', 'NA')))
    print('')


def print_deck(deck):
    print('deck size: ' + str(len(deck)))
    print('hand/deck: ')
    for card in deck:
        print_card(card)


def use_1_click(side):
    print('clicks_left: ' + str(side['clicks_left']))
    side['clicks_left'] = (side['clicks_left'] - 1)
    print('clicks_left: ' + str(side['clicks_left']))


def gain_credit(side, amount):
    print('credits: ' + str(side['credits']))
    side['credits'] = side['credits'] + amount
    print('credits: ' + str(side['credits']))


def spend_credit(side, amount):
    print('credits left: ' + str(side['credits']))
    side['credits'] = side['credits'] - amount
    print('credits left: ' + str(side['credits']))


def install_card(card):
    if card['side_code'] == runner:

        to_d.append(from_deck.pop())


# TURNS


def corp_turn():
    corp_turn_intro()
    corp['clicks_left'] = corp['clicks']  # + click modifier
    while corp['clicks_left'] > 0:
        corp_turn_actions()


def corp_turn_intro():
    print('Corporation\'s Turn \n' +
          'The Corporation\'s turn consists of three phases, ' +
          'which he performs in the following order:')

    print('Draw Phase: The Corporation draws one card from R&D.')
    print(
        'Action Phase: The Corporation has [click][click][click] with which to perform actions.'
    )
    print(
        'Discard Phase: The Corporation discards down to his maximum hand size, if necessary.'
    )

    print(
        'The Corporation draws the top card of R&D. This does not cost the Corporation any clicks.'
    )
    draw_a_card(corp['deck'], corp['hand'])
    print(
        'Note: If the Corporation\'s R&D is empty when he attempts to draw a card, '
        + 'the Runner immediately wins the game.')
    # TODO check kif corp has ran out

    print(
        'Action Phase: The Corporation has [click][click][click] with which to perform actions.'
    )

    print('1 - [click]: Draw one card from R&D.')
    print('2 - [click]: Gain 1 (one credit).')
    print('3 - [click]: Install an agenda, asset, upgrade, or piece of ice.')
    print('4 - [click]: Play an operation.')
    print('5 - [click], 1[credit]: Advance a card.')
    print(
        '6 - [click], 2[credit]: Trash a resource in the Runner\'s rig if the Runner is tagged.'
    )
    print('7 - [click][click][click]: Purge virus counters.')
    print('8 - Trigger a [click] ability on an active card (cost varies).')


def corp_turn_actions():
    action_input = input('--> ')
    if action_input == '1':
        print('draw')
        use_1_click(corp)
        draw_a_card(corp['deck'], corp['hand'])
    elif action_input == '2':
        use_1_click(corp)
        gain_credit(corp, 1)
    elif action_input == '3':
        use_1_click(corp)
        # TODO install agenda/asset/upgrade/ice
    elif action_input == '4':
        use_1_click(corp)
        # TODO play an operation
    elif action_inp2ut == '5':
        use_1_click(corp)
        spend_credit(corp, 1)
        #advance card
    elif action_input == '6':
        # TODO if runner_tagged() = True:
        use_1_click(corp)
        spend_credit(corp, 2)
        # TODO trash resource in the runners rig

    elif action_input == '7':
        use_1_click(corp)
        use_1_click(corp)
        use_1_click(corp)
        # TODO remove all virus counters

    elif action_input == '8':
        #TODO
        pass

    else:
        print('try again')
        # go to action select again


def runner_turn():
    runner_turn_intro()
    runner['clicks_left'] = runner['clicks']  # + click modifier
    while runner['clicks_left'] > 0:
        runner_turn_actions()


def runner_turn_intro():
    print('Runner\'s Turn \n')

    print(
        'Action Phase: The Runner has [click][click][click][click] with which to perform actions.'
    )

    print('1 - [click]: Draw one card from the stack.')
    print('2 - [click]: Gain 1 [credit](one credit).')
    print('3 - [click]: Install a program, resource, or piece of hardware.')
    print('4 - [click]: Play an event.')
    print('5 - [click], 2[credit]: Remove one tag.')
    print('6 - [click]: Make a run.')
    print('7 - ')
    print('8 - Trigger a [click] ability on an active card (cost varies).')


def runner_turn_actions():
    action_input = input('--> ')
    if action_input == '1':
        print('draw')
        use_1_click(runner)
        draw_a_card(runner['deck'], runner['hand'])
    elif action_input == '2':
        use_1_click(runner)
        gain_credit(runner, 1)
    elif action_input == '3':
        use_1_click(runner)
        # TODO install agenda/asset/upgrade/ice
    elif action_input == '4':
        use_1_click(runner)
        # TODO play an operation
    elif action_inp2ut == '5':
        use_1_click(runner)
        spend_credit(runner, 1)
        #advance card
    elif action_input == '6':
        # TODO if runner_tagged() = True:
        use_1_click(runner)
        spend_credit(runner, 2)
        # TODO trash resource in the runners rig

    elif action_input == '7':
        pass

    elif action_input == '8':
        #TODO
        pass

    else:
        print('try again')
        # go to action select again


# setup

# get decks for each player
runner['deck'] = deckbuilder.get_prebuilt_core_deck('shaper', 'runner')
corp['deck'] = uilder.get_prebuilt_core_deck('jinteki', 'corp')

shuffle_deck(corp['deck'])
shuffle_deck(runner['deck'])

for i in range(5):
    draw_a_card(corp['deck'], corp['hand'])
for i in range(5):
    draw_a_card(runner['deck'], runner['hand'])

# game
corp_turn()
runner_turn()
