# Example_8_1.py

# 读取HTML文件内容，并将结果转换为一个分行列表。
def getHTMLlines(htmlname):
    f = open(htmlname, "r", encoding='utf-8')
    ls = f.readlines()
    f.close()
    return ls


# 解析文件并提取图像的URL
def extractImageUrls(htmllines):
    urls = []
    for line in htmllines:
        if 'img' in line:
            url = line.split('src=')[-1].split('"')[1]
            if 'http' in url:
                urls.append(url)
    return urls


# 将获取的链接输出到屏幕上
def showResults(urls):
    count = 0
    for url in urls:
        print('第{:2}个URL：{}'.format(count, url))
        count += 1


# 保存结果到文件
def saveResults(filename, urls):
    f = open(filename, 'w')
    for url in urls:
        f.write(url + "\n")
    f.close()


def main():
    inputfile = 'nationalgeographic.html'
    outputfile = 'nationalgeographic-urls.txt'
    htmlLines = getHTMLlines(inputfile)
    imageUrls = extractImageUrls(htmlLines)
    showResults(imageUrls)
    saveResults(outputfile, imageUrls)


main()
