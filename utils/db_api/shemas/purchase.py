from sqlalchemy import Column, String, Integer, Boolean, sql

from utils.db_api.db_gino import BaseModel


class Purchase(BaseModel):
	__tablename__ = 'purchases'
	id = Column(String(50), primary_key = True)
	product_id = Column(Integer, nullable = False)
	amount = Column(Integer, nullable = False, default = 0)
	address = Column(String(100), nullable = False)
	payed = Column(Boolean, nullable = False, default = False)
	
	query: sql.Select
