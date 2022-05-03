import numpy as np
from enum import Enum
import GridWorldAgent2 as agent2

# 状态空间（尺寸）S，终点目标T，起点S，障碍B，奖励R，动作空间A，转移概率P

# 空间宽度
GridWidth = 5
# 空间高度
GridHeight = 5
# 起点
#Start = [0,0]
# 终点
# End = [(0,0),(3,3)]
# 墙
#Block = [[1,1]]
# end with reward，如果r=0,则StepReward=-1

# from s->s', get r
# s,s' 为状态序号，不是坐标位置
SepcialReward = {
    (0,0):-1,
    (1,1):-1,
    (2,2):-1,
    (3,3):-1,
    (4,4):-1,
    (5,5):-1,
    (9,9):-1,
    (10,10):-1,
    (14,14):-1,
    (15,15):-1,
    (19,19):-1,
    (20,20):-1,
    (21,21):-1,
    (22,22):-1,
    (23,23):-1,
    (24,24):-1,
    (1,21):+10,
    (3,13):+5
}
# 每走一步都-1，如果配置为0，则不减1，而是要在End处得到最终奖励
StepReward = 0

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

# 特殊移动，用于处理类似虫洞场景
SpecialMove = {
    (1,LEFT):21,
    (1,UP):21,
    (1,RIGHT):21,
    (1,DOWN):21,
    (3,LEFT):13,
    (3,UP):13,
    (3,RIGHT):13,
    (3,DOWN):13
}

# 动作空间
Actions = [UP, RIGHT, DOWN, LEFT]

EndStates = []

# 转移概率
class Probs(Enum):
    SlipLeft = 0.0
    MoveFront = 1.0
    SlipRight = 0.0
    SlipBack = 0.0

if __name__=="__main__":
    env = agent2.GridWorld(GridWidth, GridHeight, Actions, SepcialReward, Probs, StepReward, EndStates, SpecialMove)
    agent2.print_P(env.P)
    gamma = 0.9
    iteration = 1000
    V_pi = agent2.V_pi_2array(env, gamma, iteration)
    print(np.reshape(np.round(V_pi,2), (GridWidth,GridHeight)))

    V_star, Q_star = agent2.V_star(env, gamma)
    print("V*")
    print(np.reshape(np.round(V_star,2), (GridWidth,GridHeight)))
    print("Q*")
    agent2.print_P(Q_star)

    policy = agent2.get_policy(env, V_star, gamma)
    agent2.print_policy(policy, (GridWidth, GridHeight))
