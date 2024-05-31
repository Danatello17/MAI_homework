import matplotlib.pyplot as plt
import csv


if __name__ == "__main__":
    with open("result/result1.csv") as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        count = 0
        x = []
        y = []
        for row in file_reader:
            if count == 0:
                label = [row[1], row[2]]
            else:
                x.append(float(row[1]))
                y.append(float(row[2]))
            count += 1
    plt.figure(figsize=(10, 5))

    plt.plot(x, y, "-k", label=label[1])
    plt.legend()

    plt.xlabel(label[0])
    plt.ylabel(label[1])
    plt.show()
