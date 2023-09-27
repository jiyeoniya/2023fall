def convert_score_to_grade(score):
    if score < 60:
        a = '不合格'
    elif score < 75:
        a = '合格'
    elif score < 90:
        a = '良好'
    else:
        a = '优秀'
    print(a)


score = int(input())
convert_score_to_grade(score)