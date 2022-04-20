from infosystem.database import db, new_session


class TransactionManager(object):

    def __init__(self) -> None:
        self.session = new_session()
        # self.session = db.session
        self.count = 0

    def begin(self):
        if self.count == 0:
            self.session.begin()
        self.count += 1

    def commit(self):
        self.count -= 1
        if self.count == 0:
            self.session.commit()

    def rollback(self):
        self.session.rollback()
        self.count = 0
    
    def shutdown(self):
        self.session.close()