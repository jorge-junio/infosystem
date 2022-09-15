from enum import Enum

import sqlalchemy
from infosystem.common.subsystem import entity
from infosystem.database import db
from sqlalchemy import UniqueConstraint


class RoleType(Enum):
    MULTI_DOMAIN = 0
    ADMIN = 1


class Role(entity.Entity, db.Model):

    USER = 'User'
    SYSADMIN = 'Sysadmin'
    ADMIN = 'Admin'

    attributes = ['name', 'role_type']
    attributes += entity.Entity.attributes

    name = db.Column(db.String(80), nullable=False)
    role_type = db.Column(sqlalchemy.Enum(RoleType), nullable=False,
                          default=RoleType.ADMIN, server_default='ADMIN')

    __table_args__ = (
        UniqueConstraint('name', name='role_name_uk'),)

    def __init__(self, id, name, role_type,
                 active=True, created_at=None, created_by=None,
                 updated_at=None, updated_by=None, tag=None):
        super().__init__(id, active, created_at, created_by,
                         updated_at, updated_by, tag)
        self.name = name
        self.role_type = role_type
