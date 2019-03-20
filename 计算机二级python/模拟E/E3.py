import jieba
s = "世界冠军运动员的乒乓球拍卖完了"
ls = jieba.lcut(s,True)
print(ls)
