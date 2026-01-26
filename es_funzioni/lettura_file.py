def leggi_file() ->None:
    with open("domanda-1.txt", "r") as file:
        content = file.read()
        print(len(content))