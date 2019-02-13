# FinancePredict.py

# 解析CSV文件，从中读取数据，并把数据表示为列表类型。
def parseCSV(filename):
    dataNames, data = [], []
    f = open(filename, 'r', encoding='utf-8')
    for line in f:
        splitedLine = line.strip().split(',')
        if '指标' in splitedLine[0]:
            years = [int(x[:-1]) for x in splitedLine[1:]]
        else:
            dataNames.append('{:10}'.format(splitedLine[0]))
            data.append([float(x) for x in splitedLine[1:]])
    f.close()
    return years, dataNames, data

# 计算所有数据的均值    
def means(data):
    return sum(data) / len(data)

# 计算线性回归值    
def linearRegression(xlist, ylist):
    xmeans, ymeans = means(xlist), means(ylist)
    bNumerator = - len(xlist) * xmeans * ymeans
    bDenominator =  - len(xlist) * xmeans ** 2
    for x, y in zip(xlist, ylist):
        bNumerator += x * y
        bDenominator += x ** 2
    b = bNumerator / bDenominator
    a = ymeans - b * xmeans
    return a, b

# 计算新的数值    
def calNewData(newyears, a, b):
    return [(a + b * x) for x in newyears]

# 集中展示运行结果，重点在于输出格式化    
def showResults(years, dataNames, newDatas):
    print('{:^60}'.format('国家财政收支线性估计'))
    header = '指标       '
    for year in years:
        header += '{:10}'.format(year)
    print(header)
    for name, lineData in zip(dataNames, newDatas):
        line = name
        for data in lineData:
            line += '{:>10.1f}'.format(data)
        print(line)
    
def main():
    newyears = [x+2010 for x in range(7)]
    newDatas = []
    years, dataNames, datas = parseCSV('finance.csv')
    for data in datas:
        a, b = linearRegression(years, data)
        newDatas.append(calNewData(newyears, a, b))
    showResults(newyears, dataNames, newDatas)
    
main()
