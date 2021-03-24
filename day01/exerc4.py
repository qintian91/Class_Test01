print("1美元=6人名币")

def change_RMB(dollar):
    RMB=int(input("请输入人民币"))
    dollar=RMB/6

def change_dollar(RMB):
    dollar=int(input("请输入美元数:"))
    RMB=dollar*6

change_dollar()
change_RMB()

