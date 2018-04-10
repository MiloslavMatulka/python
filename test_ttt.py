"""
This is a testing file for a Tic-Tac-Toe game.

"""

import pytest

import ttt
import ttt_pc_draw

def test_evaluate_no_winner():
    field = ttt.evaluate("xoxoxoxoxoxoxoxoxoxo")
    assert field == "!"


def test_evaluate_not_finished():
    field = ttt.evaluate("-xoxoxoxoxoxoxoxoxox")
    assert field == "-"


# Assigned number is bigger than length of field.
def test_draw_invalid_number():
    with pytest.raises(ValueError):
        ttt.draw("xoxoxoxoxoxoxoxoxoxo", 30, "x")


def test_draw_correct_position():
    field = ttt.draw("--xoxoxoxoxoxoxoxoxo", 0, "x")
    assert field == "x-xoxoxoxoxoxoxoxoxo"


class TestClass:
    def test_player_draw_correct_position(self):
        ttt.input = lambda x: "5"
        output = ttt.player_draw("oxoxo--xoxoxoxoxoxox")
        assert output == "oxoxox-xoxoxoxoxoxox"

    def teardown_method(self, method):
        ttt.input = input


def test_pc_draw_len_field():
    field = ttt_pc_draw.pc_draw("-")
    assert len(field) != 20


def test_pc_draw_full_field():
        field = ttt_pc_draw.pc_draw("xoxoxoxoxoxoxoxoxoxo")
        assert field == "xoxoxoxoxoxoxoxoxoxo"


def test_pc_draw_empty_field():
    field = ttt_pc_draw.pc_draw("")
    assert len(field) == 0
