def main():

    while True:
        myVar = int(input('Give number =>'))

        def foo(myDate):
            date_suffix = ["th", "st", "nd", "rd"]

            if myDate % 10 in [1, 2, 3] and myDate not in [11, 12, 13]:
                return date_suffix[myDate % 10]
            else:
                return date_suffix[0]

        foo(myVar)
        print(foo(myVar))


if __name__ == '__main__':
    main()
