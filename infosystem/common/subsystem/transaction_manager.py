from infosystem import database
from infosystem.database import db #, new_session

import logging


handler = logging.FileHandler('transaction.log')
handler.setFormatter(logging.Formatter('%(process)d-%(levelname)s-%(message)s'))
logger = logging.getLogger('vex')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


class TransactionManager(object):

    def __init__(self, session=None) -> None:

        # self.session = session if session is not None else new_session()
        self.session = database.db.session
        # self.session = db.session
        self.count = 0

        logger.info('Init: ' + str(self.session))

    def begin(self):
        logger.info('Begin ---- ' +  str(self.count)  + ' ----  ' + str(self.session))
        # if self.count == 0:
        #     self.session.begin()
        self.count += 1

    def commit(self):
        logger.info('commit ---- ' +  str(self.count)  + ' ----  ' + str(self.session))
        self.count -= 1
        if self.count == 0:
            logger.info('commit efetivo ----  ' +  str(self.count)  + ' ----  ' + str(self.session))
            self.session.commit()

    def rollback(self):
        logger.info('rollback ---- ' +  str(self.count)  + ' ----  ' + str(self.session))
        self.session.rollback()
        self.count = -1000000

    def shutdown(self):
        # logger.info('CLOSE ---- ')
        # if self.count == 0:
        #     self.session.close()
        pass