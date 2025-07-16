from functions.write_file import write_file


def test():
    cases = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this should not be allowed"),
    ]
    for tup in cases:
        _, testing_case, _ = tup
        print(f"Result for {testing_case}:")
        print(write_file(*tup))


if __name__ == "__main__":
    test()
