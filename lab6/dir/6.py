for i in range(65,91):
    let=chr(i)
    with open(f"{let}.txt", "w", encoding="utf-8") as file:
        file.write("Hello, world!")
