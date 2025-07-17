from functions.get_files_info import get_files_info


def test():
    cases = [
        ("calculator", "."),
        ("calculator", "pkg"),
        ("calculator", "/bin"),
        ("calculator", "../"),
    ]
    for tup in cases:
        _, testing_case = tup
        if testing_case == ".":
            testing_case = "current"
        print(f"Result for {testing_case} directory:")
        print(get_files_info(*tup))


if __name__ == "__main__":
    test()
