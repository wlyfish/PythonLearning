# _*_ coding:utf-8 _*_
# @time 2022/7/31 10:45
# @Author wly
# @name Python分支优化案例.py

personHeight = input("请输入身高(m):")
personHeight = float(personHeight)

personWeight = input("请输入体重(kg):")
personWeight = float(personWeight)

personAge = input("请输入年龄:")
personAge = int(personAge)

personSex = input("请输入性别(男：1， 女：0):")
personSex = int(personSex)

if not (0 < personHeight < 3 and 0 < personWeight < 150 and 0 < personAge < 150 and (personSex == 1 or  personSex == 0)):
    print("数据不符合标准，程序退出！")
    exit()

# 处理数据
BMI = personWeight / (personHeight * personHeight)
TZL = 1.2 * BMI + 0.23 * personAge - 5.4 - 10.8 * personSex
TZL /= 100

if personSex == 1:
    result = 0.15 < TZL < 0.18
elif personSex == 0:
    result = 0.25 < TZL < 0.28

if personSex == 1:
    wenhao = "先生你好："
    minNum = 0.15
    maxNum = 0.18
elif personSex == 0:
    wenhao = "女士你好："
    minNum = 0.25
    maxNum = 0.28

if result:
    notice = "恭喜您，身体非常健康，请继续保持"
else:
    if TZL > maxNum:
        notice = "请注意，您的身体不健康，偏胖"
    else:
        notice = "请注意，您的身体不健康，偏瘦"

print(wenhao, notice)
