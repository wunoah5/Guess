#終極密碼 for 寫法
# 1.產生1~1000的隨機整數
# 2.讓使用者猜
# 3.每次猜錯時會告知範圍

import random
qmin = 0 #宣告一個範圍值
qmax = 1000 #宣告一個範圍值
que = int(random.randint(qmin,qmax)) # 隨機產生數字
print(que)

for i in range(qmin,qmax):
	print(qmin," ～ ",qmax)
	ans = int(input("請輸入答案:") )
	if (ans != que):
		if que < ans and qmax > ans:
			qmax = ans
		elif que > ans and qmin < ans: 
			qmin = ans
		else:
			print('輸入錯誤')
	else:
		print("恭喜中獎")
		break