import time

# 设置工作时间长度（以秒为单位）
WORK_TIME = 25 * 60
# 设置短休息时间长度（以秒为单位）
SHORT_BREAK_TIME = 5 * 60
# 设置长休息时间长度（以秒为单位）
LONG_BREAK_TIME = 15 * 60

# 计时器函数
def timer(duration):
    while duration > 0:
        # 清屏
        print('\033c', end='')
        # 打印剩余时间
        print(f'Time Remaining: {duration//60:02d}:{duration%60:02d}')
        # 每秒钟递减一次时间
        time.sleep(1)
        duration -= 1
    # 时间结束后发出提示音
    print('\007')

# 循环运行，直到用户终止程序
while True:
    # 工作时间
    timer(WORK_TIME)
    # 短休息时间
    timer(SHORT_BREAK_TIME)
    # 工作时间
    timer(WORK_TIME)
    # 短休息时间
    timer(SHORT_BREAK_TIME)
    # 工作时间
    timer(WORK_TIME)
    # 长休息时间
    timer(LONG_BREAK_TIME)
