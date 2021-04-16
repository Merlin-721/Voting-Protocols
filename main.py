from votingsystems import Ballot
from votingsystems import BallotRegistry
from votingsystems import VoteCount

r = BallotRegistry()

candidates = ['A','B','C','D']
profiles = [(1,[3,2,1,4]),(1,[2,3,1,4]),(1,[1,2,3,4]),(1,[4,3,1,2])]

r = BallotRegistry()
for p in profiles:
    b = Ballot(candidates, p[1])
    for i in range(p[0]):
        r.addBallot(b)
v = VoteCount(r)
print("\nBorda count:")
v.bordacount()
