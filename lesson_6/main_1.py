from contextlib import redirect_stdout

with open("input.txt", "r") as fr:
    result = fr.readline()
    while result:
        with open("output.txt", "a") as f:
            with redirect_stdout(f):
                print(result, end="")
                result = fr.readline()
