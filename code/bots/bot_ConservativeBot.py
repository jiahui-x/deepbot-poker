#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 02:00:48 2019

@author: cyril
"""


from pypokerengine.players import BasePokerPlayer
from pypokerengine.utils.card_utils import gen_cards

class ConservativeBot(BasePokerPlayer):
    def declare_action(self, valid_actions, hole_card, round_state):
        self.hole_card = gen_cards(hole_card)
        if self.hole_card[0].rank<self.hole_card[1].rank:
            self.hole_card = [self.hole_card[1],self.hole_card[0]]

        #holding A,K and A,K,Q,J
        if self.hole_card[0].rank >= 13 and self.hole_card[1].rank >= 11:
            action='call'
            call_amount = [item for item in valid_actions if item['action'] == 'call'][0]['amount']
            amount = call_amount
        else:
            action='fold'
            amount=0
        return action, amount

    def receive_game_start_message(self, game_info):
        self.i_stack = game_info['rule']['initial_stack']
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        pass

def setup_ai():
    return ConservativeBot()
