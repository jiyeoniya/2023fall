import re

id_card = input("请输入身份证号码：")
key = "^[1-9]{2}\d{4}(18|19|20)\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$"
brea = re.match(key, id_card)
if brea != None:
    print(brea.group())
    print("你的身份证号码为：" + brea.group())
    year = int(id_card[6:10])  # 截取年份
    month = int(id_card[10:12])  # 截取月份
    day = int(id_card[12:14])  # 截取日期
    sex = int(id_card[16])  # 截取性别奇数为男反之为女
    print("你的出生年日期为：%s" % year, month, day)
    if sex % 2 == 0:
        print("该身份证号码的持证人为女性")
    else:
        print("该身份证号码的持证人为男性")
else:
    print("匹配失败，请重新输入")
