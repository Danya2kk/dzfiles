def foo(grades):

    with open(grades, 'r') as f:
        file = f.readlines()
        print(file)

        ls = []
        for i in file:
            if int(i.strip()[-1]) < 3:
                ls.append(i.strip())

        for i in ls:
            print(i)


foo("grades.txt")