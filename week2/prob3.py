name = ["farmer", "wolf", "sheep", "grass"]
scheme_count = 0
# 完成后的状态


def is_done(status):
    return status[0] and status[1] and status[2] and status[3]


# 成为下一个状态的所有情况
def create_all_next_status(status):
    next_status_list = []
    for i in range(0, 4):
        if status[0] != status[i]:  # 和农夫不同一侧
            continue
        next_status = [status[0], status[1], status[2], status[3]]
        # 农夫和其中一个过河，i 为 0 时候，农夫自己过河。
        next_status[0] = not next_status[0]
        next_status[i] = next_status[0]  # 和农夫一起过河
        if is_valid_status(next_status):
            next_status_list.append(next_status)
    return next_status_list

# 判断状态是否合法


def is_valid_status(status):
    if status[1] == status[2]:
        if status[0] != status[1]:
            # 狼和羊同侧，没有人在场
            return False

    if status[2] == status[3]:
        if status[0] != status[2]:
            # 羊和草同侧，没有人在场
            return False
    return True


def search(history_status):
    # 定义全局变量
    global scheme_count
    current_status = history_status[len(history_status) - 1]
    next_status_list = create_all_next_status(current_status)
    for next_status in next_status_list:
        if next_status in history_status:
            # 出现重复的情况
            continue
        history_status.append(next_status)
        if is_done(next_status):
            scheme_count += 1
            print("scheme " + str(scheme_count) + ":")
            print_history_status(history_status)
        else:
            search(history_status)
        history_status.pop()


def readable_status(status, is_across):
    result = ""
    for i in range(0,4):
        if status[i] == is_across:
            if len(result) != 0:
                result += ","
            result += name[i]
    return "[" + result + "]"

# 打印结果


def print_history_status(history_status):
    for status in history_status:
        print(readable_status(status, False) + "--------" + readable_status(status, True))

# 程序开始的入口


if __name__ == "__main__":
    # 初始局面
    status = [False, False, False, False]
    # 局面队列
    history_status = [status]
    # 对已知状态进行求解
    search(history_status)
    print("finish search, find " + str(scheme_count) + " scheme")
