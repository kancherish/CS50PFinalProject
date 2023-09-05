from project import scope,show,Findcontent

def main():
     test_scope()
     test_show()
     test_FindContent()

def test_scope():
    assert scope("root")=="/"
    assert scope("w")=="w"

def test_show():
     assert show("w")==[]

def test_FindContent():
    assert Findcontent("w","w")=={}

