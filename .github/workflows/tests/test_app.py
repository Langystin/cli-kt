from main import main_function  

def main_function():
    print("результат 5")

if __name__ == "__main__":
    main_function()


def test_main_output(capsys):
    main_function()
    captured = capsys.readouterr()
    assert "результат 5" in captured.out