# Voting Systems
![](https://travis-ci.com/azoght/voting-systems.svg?branch=master)
![](https://img.shields.io/badge/made%20with-python-gray&color=?color=f50505&style=for-the-badge)

Simulates four vote count systems that can used with ranked ballots:
1. Plurality/Majority
2. Instant Runoff (IRV/RCV)
3. Borda Count
4. Condorcet

## Credit
This is an edited version of azoght's repository, found here:
https://github.com/azoght/voting-systems



## How each voting system works

**Plurality:**
* Most commonly used system, especially for federal elections, and isn't generally ranked-ballot
* Counts the number of times each candidate is ranked first within the ballot registry
* Whichever candidate is ranked first the most wins
* Not the best voting system, in my opinion

**Instant Runoff:**
* This system works in rounds, eliminating the candidate with the lowest count
* Round _n_: times each non-eliminated candidate is ranked _n_ are counted
* If there is a majority and _n_ is greater than 1, the candidate with the highest count wins
* Otherwise, the last candidate standing wins

**Borda Count:**
* Ranked-ballot voting system developed by French mathematician Jean-Charles de Borda
* A weight is assigned in reverse proportion to each rank
* The candidate with the highest weighted value wins
* There are multiple variations, but the simplest one is the one I've coded

**Condorcet:**
* Puts each candidate against one another
* The winner of each round is whichever candidate is ranked higher than the other most times
* The candidate who won the most rounds wins
* Can result in a tie between all candidates

# Getting Started

> See travis.yml for how to get started

## Setup
![](https://img.shields.io/badge/python-3.8-blue) 

Requires Python 3 or higher

### To install:

```
pip install -r requirements.txt
```

### To run without IDE:

Make sure to set PYTHONPATH to where the votingsystems module is at, for example:

```
 export PYTHONPATH=$PYTHONPATH:.

```


### To clone:

```
git clone https://github.com/ThorChadMerlin/Voting-Protocols
```

__Don't forget to fork and edit the code anyway you wish!__

## How to...

### Make a ballot

Example:
```python
candidates = ['A','B','C']
votes = [1,2,3]
b = Ballot(candidates,votes)
```
### Make a ballot registry

Example (Non-randomized):
```python
r = BallotRegistry()
b = Ballot(['A','B','C'],[1,2,3])
for i in range(5):
    r.addBallot(b)
b = Ballot(['A','B','C'],[2,3,1])
for i in range(5):
    r.addBallot(b)
```
Example (Randomized):
```python
def randomBallotVoteConfiguration(c: []) -> []:
    con = c
    random.shuffle(con)
    return con
options = ['A','B','C']

configs = []
r = BallotRegistry()
for i in range(100):
    configs.append(randomBallotVoteConfiguration([1, 2, 3]))

for c in configs:
    r.addBallot(Ballot(options, c))
```

### Make vote count

```python
v = VoteCount(r)
# Voting Methods (return no value, but print winner)
v.plurality()
v.instantRunoff()
v.bordaCount()
v.condorcet()
```

## License

![](https://img.shields.io/badge/license-mpl%202.0-blue&color=?color=2c6ee8)

[Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
