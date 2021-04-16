from votingsystems import Ballot


def test_ballot():
    b = Ballot(['a','b','c'],[1,2,3])
    assert b.votes != None
    assert b.candidates != None