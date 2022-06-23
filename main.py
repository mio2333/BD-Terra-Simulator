from random import random,randint
from tqdm  import trange
import numpy as np

N = 100000
S = 0
ns = 2

def simulate(ns):
    ans = 0
    skills = [0,0,0,0] # 0:E 1:D 2:C 3:B 4:A 5:S
    up_probs = [0.5,0.45,0.4,0.35,0.3,0.25]
    while True:
        ans += 1
        pos = randint(0,3)
        toz = randint(1,100) / 100
        up_prob = up_probs[skills[pos]]
        if toz < up_prob:
            # up skill
            skills[pos] = min(skills[pos]+1,5)
        else:
            # de skill
            skills[pos] = max(skills[pos]-1,0)

        # check
        if skills.count(5) == ns: break
    return ans

def simple_simulate(a,b):
    ans = 0
    up_probs = [0.5,0.45,0.4,0.35,0.3,0.25]
    skill = a
    while True:
        if skill == b: break
        ans += 1
        toz = random()
        up_prob = up_probs[skill]
        if toz < up_prob:
            # up skill
            skill = min(skill+1,5)
        else:
            # de skill
            skill = max(skill-1,0)
        
    return ans
# for t in range(5):
#     S = 0
#     for i in trange(N):
#         # S += simulate(ns)
#         S += simple_simulate(t,5)
#     print(S/N)

for i in trange(N):
    # S += simulate(ns)
    S += simple_simulate(0,5)
print(S/N)

print(f"在不使用任何汇入功能的情况下，平均需要{S/N*200}个泰拉才能洗到{ns}S")

