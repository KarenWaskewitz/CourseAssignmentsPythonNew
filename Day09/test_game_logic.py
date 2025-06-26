from game_logic import check_guess

def test_check_guess():
    assert check_guess(50, 30) == 'low'
    assert check_guess(50, 70) == 'high'
    assert check_guess(50, 50) == 'correct'