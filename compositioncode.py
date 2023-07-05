class Share(object):

    def modular(self):
        print "This function belongs to the Share() base class."

class Copy(object):

    def __init__(self):
        self.firstbaseclass = Share()

    def text(self):
        print "This function belongs to the Copy() base class."
        self.firstbaseclass.modular()

cat = Copy()

cat.text()

