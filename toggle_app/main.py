import sqlite3

class Registro_datos:
	"""docstring for Registro_datos"""
	def __init__(self):
		BD = 'mydatabase.db'
		self.conn = sqlite3.connect(BD)

	def insert_products(self, cod, name, model, price, qty):
		cur = self.conn.cursor()
		sql = '''INSERT INTO product (cod, name, model, price, quantity)
				 VALUES('{}', '{}', '{}', '{}', '{}')'''.format(cod, name, model, price, qty)
		cur.execute(sql)
		self.conn.commit()
		cur.close()
		self.conn.close()

	def show_products(self):
		cur = self.conn.cursor()
		sql = '''INSERT INTO product (cod, name, model, price, quantity)
				 VALUES('{}', '{}', '{}', '{}', '{}')'''.format(cod, name, model, price, qty)


	def search_product(self, product_name):
		cur = self.conn.cursor()
		sql = "SELECT * FROM product WHERE name = {}".format(product_name)
		cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		return result

	def delete_product(self, cod):
		cur = self.conn.cursor()
		sql = '''DELETE FROM product WHERE cod = {}'''.format(cod)
		cur.execute(sql)
		self.conn.commit()
		cur.close()

	def update_product(self, Id, cod, name, model, price, qty):
		cur = self.conn.cursor()
		sql = '''UPDATE product SET cod = '{}', name = '{}', model = '{}', price = '{}', quantity = '{}'
				WHERE id = '{}' '''.format(cod, name, model, price, qty, Id)

		cur.execute(sql)
		a = cur.rowcount
		self.conn.commit()
		cur.close()
		return a

