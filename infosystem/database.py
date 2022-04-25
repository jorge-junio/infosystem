import flask_sqlalchemy
import flask_migrate

# from sqlalchemy.orm import sessionmaker

db = flask_sqlalchemy.SQLAlchemy()
migrate = flask_migrate.Migrate()

# Session = sessionmaker(db.engine)


# def new_session():
#     return sessionmaker(db.engine)()
    # return db.session
