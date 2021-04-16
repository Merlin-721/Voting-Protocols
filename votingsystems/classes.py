import random


class Ballot:  # ranked ballot, containing list of candidates, and their corresponding ranks

    def __init__(self, c: [str], v: [int]):
        if len(c) == len(v):  # the ballot must have an equal number of candidates and ranks to be considered legit
            self.candidates = c
            self.votes = v
        else:
            self.candidates = None
            self.votes = None
            print("Invalid Ballot!")


def isEqualToAll(l1: [], l2: []) -> bool:  # determines if two lists are exactly equal
    if len(l1) == len(l2):
        count = 0
        for i in range(len(l1)):
            if l1[i] == l2[i]:
                count += 1
        if count == len(l1):
            return True
    return False


def hasMajority(b: Ballot) -> bool:  # determines if a candidate has more than half of total votes
    majThreshold = 0
    for v in range(len(b.votes)):
        if b.votes[v] != -1:
            majThreshold += b.votes[v]
    majThreshold = majThreshold // 2
    biggest = 0
    for v in range(len(b.votes)):
        if b.votes[v] > b.votes[biggest]:
            biggest = v
    if b.votes[biggest] >= majThreshold:
        return True
    return False


def containsBoth(l: [], a1, a2) -> bool:  # determines if a list contains two specified elements
    for i in range(len(l)):
        if l[i] == [a1, a2] or l[i] == [a2, a1]:
            return True
    return False


def isHigherThan(b: Ballot, b1: int, b2: int) -> bool:  # determines if a candidate is ranked higher than another
    return b.votes[b1] < b.votes[b2]


class BallotRegistry:  # list of ballots to be used for vote count

    def __init__(self):
        self.br = []

    def addBallot(self, b: Ballot):  # adds ballot to registry
        if len(self.br) == 0:
            self.br.append(b)
        elif len(self.br) >= 0:
            zeropos = self.br[0]
            if isEqualToAll(b.candidates, zeropos.candidates):
                self.br.append(b)
            else:
                print("Invalid ballot for registry")


class VoteCount:  # contains vote count methods to be done on a ballot registry

    def __init__(self, br: BallotRegistry):
        self.registry = br

    def __makecountregister__(self) -> Ballot:  # creates a vote count register to be used for vote count methods
        vee = []
        for c in range(len(self.registry.br[0].candidates)):
            vee.append(0)
        count_register = Ballot(c=self.registry.br[0].candidates, v=vee)
        return count_register

    def plurality(self):  # also known as majority
        count_register = self.__makecountregister__()
        for b in self.registry.br:  # adds candidates ranked 1 in ballots to register
            for r in range(len(b.votes)):
                if b.votes.index(r+1) == 0:
                    count_register.votes[r] += 1
                    break

        winner = 0

        for c in range(len(count_register.votes)):  # winner is whoever was ranked 1 the most
            if count_register.votes[c] > count_register.votes[winner]:
                winner = c
        print([x for _,x in sorted(zip(count_register.votes,count_register.candidates))])
        print("Winner is", count_register.candidates[winner])

    def instantrunoff(self):  # ranked voting method that eliminates candidate with least votes each round
        count_register = self.__makecountregister__()
        eliminated = []
        # for each round
        for r in range(len(count_register.candidates)):
            count_register = self.__makecountregister__()
            # for each candidate    
            for o in range(len(count_register.candidates)):
                if o+1 in eliminated:
                    count_register.votes[o] = -1
                # for each ballot
                for b in self.registry.br:  # adds candidates, except eliminated candidates ranked o in ballots to register
                    # for each place in ballot
                    for r in range(len(b.votes)):
                        # if index after -1 (if -1 in ballot) is candidate, add 1 to candidate
                        if b.votes[r] != -1:
                            index = r
                        else:
                             continue#(b.votes.index(-1) + 1)
                        # if b.votes[b.votes.index(-1)+1 if -1 in b.votes else 0] == o:
                        if b.votes[index] == o+1:  
                            count_register.votes[o] += 1
                            break
                        else:
                            break
            

                # for b in self.registry.br:  # adds candidates, except eliminated candidates ranked o in ballots to register
                #     for r in range(len(b.votes)):
                #         if b.votes[r] == o and count_register.candidates[r] != -1:
                #             count_register.votes[r] += 1
                #             break
            
            #least = [0] # index of candidate (1,2,3,4) with least votes
            least = next((i for i, v in enumerate(count_register.votes) if v != -1), 0)
                # if o > 1 and hasMajority(count_register):  # can end early due to a majority
                #     break
            
            
            for c in range(len(count_register.votes)):  # elimination process
                if count_register.votes[c] <= count_register.votes[least] and count_register.votes[c] != -1:
                    if c + 1 not in eliminated:
                        least =c
            
            for b in self.registry.br:
                if least+1 in b.votes:
                    elim = b.votes.index(least+1)
                    b.votes[elim] = -1
            eliminated.append(elim)
                # count_register.votes[least] = -1

        winner = 0
        for c in range(len(count_register.votes)):  # winner is whoever has most in register
            if count_register.votes[c] > count_register.votes[winner]:
                winner = c
        print([x for _,x in sorted(zip(count_register.votes,count_register.candidates))])
        print("Winner is", count_register.candidates[winner])

    def bordacount(self):  # ranked voting method assigning a weight to each rank (ex. 1 = 3, 2 = 2, 3 = 1)
        count_register = self.__makecountregister__()
        points = [3,2,1,0]
        # for each ballot
        for b in self.registry.br:
            # for each ballot position
            for i in range(len(b.votes)):
                count_register.votes[b.votes[i]-1] += points[i]


        winner = 0
        for c in range(len(count_register.votes)):  # winner has most in register
            if count_register.votes[c] > count_register.votes[winner]:
                winner = c
        print([x for _,x in sorted(zip(count_register.votes,count_register.candidates))])
        print("Winner is", count_register.candidates[winner])

    def condorcet(self):  # ranked voting method that pairs each candidate agianst each other
        count_register = self.__makecountregister__()
        roundList = []  # list of possible
        fillingList = True
        lengthofRoundList = 0.5 * (len(count_register.candidates) ** 2) - 0.5 * len(count_register.candidates)
        while fillingList:  # order of rounds is random
            r1 = random.randint(0, len(count_register.candidates) - 1)
            r2 = random.randint(0, len(count_register.candidates) - 1)
            if r1 != r2:
                if not containsBoth(roundList, r1,
                                    r2):  # checks if a pairing of r1 and r2 are already in the round list
                    roundList.append([r1, r2])
            if len(roundList) == lengthofRoundList:
                fillingList = False

        for ro in roundList:
            c1 = 0  # count of ballots where ro[0] is ranked higher than ro[1]
            c2 = 0  # count of ballots where ro[1] is ranked higher than ro[0]
            for b in self.registry.br:
                #if isHigherThan(b, b.votes.index(ro[0]), b.votes.index(ro[1])):
                if b.votes.index(ro[0]+1) < b.votes.index(ro[1]+1):
                    c1 += 1
                else:
                    c2 += 1
            if c1 > c2:
                count_register.votes[ro[0]] += 1  # ro[0] wins this round
            if c2 > c1:
                count_register.votes[ro[1]] += 1  # ro[1] wins this round

        biggest_num = 0
        for v in range(len(count_register.votes)):  # finds the biggest number in vote count register
            if count_register.votes[v] > biggest_num:
                biggest_num = count_register.votes[v]

        count = 0
        for v in range(len(count_register.votes)):  # checks if that biggest number is repeated so a tie can be declared
            if count_register.votes[v] == biggest_num:
                count += 1

        if count > 1:
            print("It's a tie!")
        else:
            print([x for _,x in sorted(zip(count_register.votes,count_register.candidates))])
            winner = ""
            for c in range(len(
                    count_register.candidates)):  # if there isn't a tie, the winner is whichever candidate won most rounds
                if count_register.votes[c] == biggest_num:
                    winner = count_register.candidates[c]

            print("Winner is", winner)
