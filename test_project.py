from project import swap_row, swap_column, check_none, greeting, mode_input, user_input, check_correct, play, congrat, initialize, checker, unique, solver, creator
import pyfiglet


def test_swap_row():
    assert swap_row([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 1, 2) == [[1, 2, 3], [3, 4, 5], [2, 3, 4]]
    assert swap_row([[11, 21, 31], [2, 5, 9], [3, 7, 8]], 1, 2) == [[11, 21, 31], [3, 7, 8], [2, 5, 9]]
    assert swap_row([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 0, 2) == [[3, 4, 5], [2, 3, 4], [1, 2, 3]]

def test_swap_column():
    assert swap_column([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 1, 2) == [[1, 3, 2], [2, 4, 3], [3, 5, 4]]
    assert swap_column([[11, 21, 31], [2, 5, 9], [3, 7, 8]], 1, 2) == [[11, 31, 21], [2, 9, 5], [3, 8, 7]]
    assert swap_column([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 0, 2) == [[3, 2, 1], [4, 3, 2], [5, 4, 3]]

def test_check_none():
    assert check_none([[1, 2, 3], [2, 3, 4], [3, 4, 5]]) == True
    assert check_none([[11, 21, 3], [222, 3, 41], [31, 4, 55]]) == True
    assert check_none([[1, None, 3], [2, 3, 4], [3, 4, 5]]) == False

def test_greeting():
    assert greeting("Hello") == pyfiglet.figlet_format("Hello", "slant")
    assert greeting("CS50") == pyfiglet.figlet_format("CS50", "slant")
    assert greeting("Play chess and sudoku") == pyfiglet.figlet_format("Play chess and sudoku", "slant")

def test_mode_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "create_new")
    assert mode_input() == "create_new"
    monkeypatch.setattr('builtins.input', lambda _: "play_new")
    assert mode_input() == "play_new"


def test_user_input(mocker):
    mocker.patch("builtins.input", side_effect = ["1", "2", "2"])
    assert user_input([[1, None, 3], [2, 3, 4], [3, 4, 5]]) == (2, 0, 1)
    mocker.patch("builtins.input", side_effect = ["1", "1", "2", "1", "3"])
    assert user_input([[1, None, 3], [None, 3, 4], [3, 4, 5]]) == (3, 1, 0)
    mocker.patch("builtins.input", side_effect = ["10", "10", "2", "1", "3"])
    assert user_input([[1, None, 3], [None, 3, 4], [3, 4, 5]]) == (3, 1, 0)

def test_check_correct():
    assert check_correct([[3, 2, 5, 1, 4], [2, 1, 4, 5, 3], [5, 4, 2, 3, 1], [4, 3, 1, 2, 5], [1, 5, 3, 4, 2]]) == True
    assert check_correct([[3, 3, 5, 1, 4], [2, 1, 4, 5, 3], [5, 4, 2, 3, 1], [4, 3, 1, 2, 5], [1, 5, 3, 4, 2]]) == False
    assert check_correct([[3, 2, 6, 1, 4], [2, 1, 4, 5, 3], [5, 4, 2, 3, 1], [4, 3, 1, 2, 5], [1, 5, 3, 4, 2]]) == False

def test_play(mocker):
    mocker.patch("builtins.input", side_effect = ["1", "2", "2"])
    assert play([[3, None, 5, 1, 4], [2, 1, 4, 5, 3], [5, 4, 2, 3, 1], [4, 3, 1, 2, 5], [1, 5, 3, 4, 2]]) == True
    mocker.patch("builtins.input", side_effect = ["1", "2", "3", "1", "4", "3"])
    assert play([[3, None, 5, None, 4], [2, 1, 4, 5, 3], [5, 4, 2, 3, 1], [4, 3, 1, 2, 5], [1, 5, 3, 4, 2]]) == False

def test_congrat(mocker):
    mocker.patch("builtins.input", side_effect = ["dimetrodon"])
    assert congrat() == True
    mocker.patch("builtins.input", side_effect = ["hehesaur"])
    assert congrat() == False

def test_initialize():
    #Random grid, so can only check format
    assert len(initialize([])) == 5
    assert len(initialize([])[0]) == 5
    assert check_correct(initialize([])) == True

def test_checker():
    assert checker([[1, 5, 2, 4, 3], [4, 3, 5, 2, 1], [3, 2, 4, 1, 5], [2, 1, 3, 5, 4], [5, 4, 1, 3, 2]]) == [[set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()]]
    assert checker([[None, 5, 2, 4, 3], [4, 3, 5, 2, 1], [3, 2, 4, 1, 5], [2, 1, 3, 5, 4], [5, 4, 1, 3, 2]]) == [[{1}, set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()]]
    assert checker([[None, None, 2, 4, 3], [4, 3, 5, 2, 1], [3, 2, 4, 1, 5], [2, 1, 3, 5, 4], [5, 4, 1, 3, 2]]) == [[{1}, {5}, set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()]]

def test_unique():
    assert unique([[1, 5, 2, 4, 3], [4, 3, 5, 2, 1], [3, 2, 4, 1, 5], [2, 1, 3, 5, 4], [5, 4, 1, 3, 2]]) == [[set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()]]
    assert unique([[None, None, 2, 4, 3], [4, 3, 5, 2, 1], [3, 2, 4, 1, 5], [2, 1, 3, 5, 4], [5, 4, 1, 3, 2]]) == [[{1}, {5}, set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()]]
    assert unique([[None, None, 2, 4, 3], [None, None, 5, 2, 1], [None, None, 4, 1, 5], [2, 1, 3, 5, 4], [5, 4, 1, 3, 2]]) == [[{1}, {5}, set(), set(), set()], [{4}, set(), set(), set(), set()], [set(), {2}, set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()]]

def test_solver():
    assert solver([[1, 5, 2, 4, 3], [4, 3, 5, 2, 1], [3, 2, 4, 1, 5], [2, 1, 3, 5, 4], [5, 4, 1, 3, 2]]) == ([[1, 5, 2, 4, 3], [4, 3, 5, 2, 1], [3, 2, 4, 1, 5], [2, 1, 3, 5, 4], [5, 4, 1, 3, 2]], True)
    assert solver([[None, None, 2, 4, 3], [4, 3, 5, 2, 1], [3, 2, 4, 1, 5], [2, 1, 3, 5, 4], [5, 4, 1, 3, 2]]) == ([[1, 5, 2, 4, 3], [4, 3, 5, 2, 1], [3, 2, 4, 1, 5], [2, 1, 3, 5, 4], [5, 4, 1, 3, 2]], True)
    assert solver([[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None]]) == (None, False)

def test_creator():
    grid = []
    grid = initialize(grid)

    #Random grid, so can only check format
    assert len(creator(grid)) == 5
    assert len(creator(grid)[0]) == 5
    solved, flag = solver(creator(grid))
    assert flag == True