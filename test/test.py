#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提
# 成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？






def  get_reward(I):
    rewards = 0
    if I <= 10:
        rewards = I * 0.1

    elif (I > 10) and (I <= 20):
        rewards = (I - 10) * 0.075 + get_reward(10)

    elif (I > 20) and (I <= 40):
        rewards = (I - 20) * 0.05 + get_reward(20)

    elif (I > 40) and (I <= 60):
        rewards = (I - 40) * 0.03 + get_reward(40)

    elif (I > 60) and (I <= 100):
        rewards = (I - 60) * 0.015 + get_reward(60)

    else:
        rewards = get_reward(100) + (I - 100) * 0.01

    return rewards

if __name__ == '__main__':
    i = int(input('利润:'))
    print("1 发放的奖金为：", get_reward(i / 10000) * 10000)

    ten = 100000 * 0.1
    twenty = (200000 - 100000) * 0.075
    fourty = (400000 - 200000) * 0.05
    sixty = (600000 - 400000) * 0.03
    hundred = (1000000 - 600000) * 0.015
    if i < 100000:
        bonus = i * 0.1
    elif i > 100000 and i < 200000:
        bonus = ten + (i - 100000) * 0.075
    elif i > 200000 and i < 400000:
        bonus = ten + twenty + (i - 200000) * 0.05
    elif i > 400000 and i < 600000:
        bonus = ten + twenty + fourty + (i - 400000) * 0.03
    elif i > 600000 and i < 1000000:
        bonus = ten + twenty + fourty + sixty + (i - 600000) * 0.015
    elif i > 1000000:
        bonus = ten + twenty + fourty + sixty + hundred + (i - 1000000) * 0.01

    print("2 奖金为:", bonus)

    att = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for rdx in range(0, 6):
        if i > att[rdx]:
            r += (i - att[rdx]) * rat[rdx]
            i = att[rdx]
    print("3 奖金为：",r)

