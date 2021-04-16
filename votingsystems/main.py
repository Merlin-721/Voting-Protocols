from votingsystems import BallotRegistry, Ballot, VoteCount
import random

# Example Poll 1: Who's The Favourite Guy from F.R.I.E.N.D.S.? (3 candidates, constant ballot generation)

candidates = ["Chandler", "Joey", "Ross"]

r = BallotRegistry()

config = [1, 2, 3]

b = Ballot(candidates, config)

for i in range(13):
    r.addBallot(b)

config = [1, 3, 2]

b = Ballot(candidates, config)

for i in range(7):
    r.addBallot(b)

config = [2, 1, 3]

b = Ballot(candidates, config)

for i in range(19):
    r.addBallot(b)

config = [2, 3, 1]

b = Ballot(candidates, config)

for i in range(26):
    r.addBallot(b)

config = [3, 1, 2]

b = Ballot(candidates, config)

for i in range(28):
    r.addBallot(b)

config = [3, 2, 1]

b = Ballot(candidates, config)

for i in range(7):
    r.addBallot(b)

v = VoteCount(r)

v.plurality()
v.instantrunoff()
v.bordacount()
v.condorcet()


def randomBallotVoteConfiguration(c: []) -> []:
    con = c
    random.shuffle(con)
    return con


# Example Poll 2: What's Most Important At Slowing Spread of Virus? (5 candidates, randomized ballot generation)

options = ["Soap", "Sanitizer", "Masks/Face Shields", "Physical/Social Distancing", "Self-Isolation"]

configs = []
registry = BallotRegistry()
for i in range(100):
    configs.append(randomBallotVoteConfiguration([1, 2, 3, 4, 5]))

for c in configs:
    registry.addBallot(Ballot(options, c))

vote = VoteCount(registry)

vote.plurality()
vote.instantrunoff()
vote.bordacount()
vote.condorcet()
