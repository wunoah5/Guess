#終極密碼 while 的寫法
# 1.產生1~1000的隨機整數
# 2.讓使用者猜
# 3.每次猜錯時會告知範圍

import random
maxr = 100
mixr = 1
r = random.randint(mixr+1, maxr-1)
while True:
    print('終極密碼', mixr, '到', maxr, ': ')
    ans = int(input())
    #如果回答等於隨機數
    if r == ans:
        print('~~你~最~雖~小~~')
        break
    #如果回答大於最小值且小於隨機數，取代最小值
    elif ans > mixr and ans < r:
        mixr = ans
        print('恭喜過關!!!')
        print()
    #如果回答小於最大值且大於隨機數，取代最大值
    elif ans <  maxr and ans > r:     
        maxr = ans
        print('恭喜過關!!!')
        print()
    else:
        print('輸入錯誤')
        print()