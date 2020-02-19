from matplotlib import pyplot as plt
import csv

#Create CSV File Function
def createCsvFile(data):
    f = open('exchangerate.csv', 'w', encoding='UTF-8',newline='')
    csv.writer(f).writerow(data)
    f.close()

#new data Exchange Rate
def writeExchangeRate(data):
    with open('exchangerate.csv','a',encoding='UTF-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(data)

# show plot graph
def show(xlabel,ylabel,x, y):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# read csv file & call plot graph
def readCsvFile():
    x = []
    y = []
    xlabel, ylabel = '', ''

    with open('exchangerate.csv','r') as f:
        reader = csv.reader(f)
        j = 0
        # xlabel = reader[0][0]
        # ylabel = reader[0][1]
        for i in reader:
            if j == 0:
                xlabel = i[0]
                ylabel = i[1]
            else:
                x.append(i[0])
                y.append(int(i[1]))
            j += 1
    show(xlabel,ylabel,x, y)

#Main Function

#exchangerate CSV File check
try:
    f = open('exchangerate.csv','r')
    f.close()
except:
    createCsvFile(['Date', 'Rate'])

#main loop
while True:
    menu = int(input("""Select Menu
1. write exchange rate data
2. show graph exchange rate data
:"""))

    if menu == 1 :
        data = []
        data.append(input("Date :"))
        data.append(int(input("Rate :")))

        writeExchangeRate(data)

    elif menu == 2 :
        readCsvFile()
