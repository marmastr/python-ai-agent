from functions.get_file_content import get_file_content


def test():
    cases = [
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py"),
    ]
    for tup in cases:
        _, testing_case = tup
        if testing_case == ".":
            testing_case = "current"
        print(f"Result for {testing_case} directory:")
        print(get_file_content(*tup))


if __name__ == "__main__":
    test()
