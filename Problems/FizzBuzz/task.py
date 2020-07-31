for n in range(1, 101):
    txt = ""
    if n % 3 == 0:
        txt = "Fizz"
    if n % 5 == 0:
        txt += "Buzz"
    print(n if txt == "" else txt)
