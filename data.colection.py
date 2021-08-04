from matplotlib import pyplot as plt

x = []
y = []


def read():
    file = open("C:\\Users\\lenovo\\OneDrive\\Desktop\\QHO426\\data225.txt ", "r")
    try:
        counter = 0
        for line in file:
            if counter <= 11:
                x.append(line)
                counter += 1
            else:
                y.append(line)
        print(len(x))
        print(len(y))
        y.reverse()
        x.reverse()



    except:
        print('Could not find file')
    file.close()


read()
plt.bar(x, y)
plt.show()
