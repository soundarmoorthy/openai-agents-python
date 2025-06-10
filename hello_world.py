from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a 10 year old child, but can say haiku")

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
