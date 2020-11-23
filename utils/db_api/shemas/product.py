from sqlalchemy import Column, BigInteger, String, Numeric, LargeBinary, sql, Float

from utils.db_api.db_gino import BaseModel


class Product(BaseModel):
	__tablename__ = 'products'
	id = Column(BigInteger, primary_key = True, autoincrement = True)
	name = Column(String(50), nullable = False, server_default = 'trtrt')
	description = Column(String(100))
	# price = Column(Numeric(scale = 2, asdecimal = True, decimal_return_scale = 2))
	photo = Column(String(100))
	price = Column(Float)
	
	query: sql.Select
