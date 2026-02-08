from core.base import Base

class Test(Base):
    def initialize(self):
        print('Initializing stuff :)')

    def update(self):
        pass

test = Test()
test.run()