from functions.run_python_file import run_python_file


def test():
    cases = [
        ("calculator", "main.py"),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py"),
    ]
    for tup in cases:
        print(f"Result for {tup}:")
        print(run_python_file(*tup))


if __name__ == "__main__":
    test()
