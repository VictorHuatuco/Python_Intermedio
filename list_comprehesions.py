def run():

    squares = [i for i in range(1, 10000) if i % 36 == 0]

    # squares = []
    # for i in range (1, 51):
    #     if (i**2) % 3 == 0:
    #         squares.append(i**2)
    print("los numeros son", squares, "jejeje")

if __name__ == '__main__':
    run()