import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import main_function


def test_main_output(capsys):
    main_function()
    captured = capsys.readouterr()
    assert "результат 5" in captured.out
