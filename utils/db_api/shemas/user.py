from sqlalchemy import Column, BigInteger, String, sql, Numeric

from utils.db_api.db_gino import BaseModel


class User(BaseModel):
	__tablename__ = 'users'
	id = Column(BigInteger, primary_key = True)
	name = Column(String(100))
	# description = Column(String(200))
	bonus = Column(Numeric)
	# zreferral = Column(BigInteger)
	
	query: sql.Select
