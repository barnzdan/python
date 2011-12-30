class Behave(object):
    def __init__(self, name):
         self.name = name
    def once(self):
        print "Hello,",  self.name
    def rename(self, newName)
        self.name = newName
    def repeat(self, N):
        for i in range(N): self.once()
