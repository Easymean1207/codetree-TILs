class Agent:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score

Agents = []
for _ in range(5):
    code_name, score = tuple(input().split())
    score = int(score)
    Agents.append(Agent(code_name,score))

min_idx = 0
for i in range(len(Agents)):
    if Agents[i].score < Agents[min_idx].score:
        min_idx = i

min_agent = Agents[min_idx]

print(min_agent.code_name, min_agent.score)