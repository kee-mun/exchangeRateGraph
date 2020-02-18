from matplotlib import pyplot as plt
import csv

#Create CSV File Function
def createCsvFile(data):
    f = open('exchangerate.csv', 'w', newline='')
    csv.writer(f).writerow(data)
    f.close()

#new data Exchange Rate
def writeExchangeRate(data):
    try:
        with open('exchangerate.csv','a', newline='') as f:
            wr = csv.wirter(f)
            wr.writerow(data)
    except:
        createCsvFile(['Date', "Rate"])
        writeExchangeRate(data)
def show(xlabel,ylabel,x, y):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def readCsvFile():
    x = []
    y = []
    xlabel, ylabel = '', ''
    try:
        with open('exchangerate.csv','r') as f:
            reader = csv.reader(f)
            xlabel = reader[0][0]
            ylabel = reader[0][1]
            for i in range(1,len(reader)):
                x.append(i[0])
                y.append(i[1])
        show(xlabel,ylabel,x, y)
    except:
        createCsvFile(['Date', "Rate"])
        print("저장된 데이터가 없습니다.")

#Main Function
menu = int(input("""Select Menu
1. write exchange rate data
2. show graph exchange rate data
:"""))

while True:
    if menu == 1 :
        data = []
        data.append(input("Date :"))
        data.append(int(input("Rate :")))

        writeExchangeRate(data)

    elif menu == 2 :
        pass

    menu = 0
