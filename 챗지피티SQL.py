import sqlite3
import random

class ElectronicsDatabase:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """
        전자제품 테이블 생성
        """
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                price REAL NOT NULL
            )
            """)
    
    def insert_product(self, product_name, price):
        """
        제품 삽입
        """
        with self.conn:
            self.conn.execute("""
            INSERT INTO products (product_name, price) 
            VALUES (?, ?)
            """, (product_name, price))
    
    def update_product(self, product_id, product_name=None, price=None):
        """
        제품 정보 업데이트
        """
        with self.conn:
            if product_name and price is not None:
                self.conn.execute("""
                UPDATE products
                SET product_name = ?, price = ?
                WHERE product_id = ?
                """, (product_name, price, product_id))
            elif product_name:
                self.conn.execute("""
                UPDATE products
                SET product_name = ?
                WHERE product_id = ?
                """, (product_name, product_id))
            elif price is not None:
                self.conn.execute("""
                UPDATE products
                SET price = ?
                WHERE product_id = ?
                """, (price, product_id))

    def delete_product(self, product_id):
        """
        제품 삭제
        """
        with self.conn:
            self.conn.execute("""
            DELETE FROM products 
            WHERE product_id = ?
            """, (product_id,))

    def select_product(self, product_id=None):
        """
        제품 조회
        """
        with self.conn:
            cursor = self.conn.cursor()
            if product_id:
                cursor.execute("""
                SELECT * FROM products 
                WHERE product_id = ?
                """, (product_id,))
                return cursor.fetchone()
            else:
                cursor.execute("""
                SELECT * FROM products
                """)
                return cursor.fetchall()

    def close(self):
        """
        데이터베이스 연결 종료
        """
        self.conn.close()

# 전자제품 데이터베이스 생성 및 사용
db = ElectronicsDatabase()

# 샘플 데이터 생성 및 삽입
product_names = [f"Product {i}" for i in range(1, 101)]
for name in product_names:
    price = round(random.uniform(10.0, 500.0), 2)  # 10.0에서 500.0 사이의 랜덤 가격
    db.insert_product(name, price)

# 샘플 데이터 확인 (모든 제품 출력)
products = db.select_product()
for product in products:
    print(product)

# 제품 정보 업데이트 (예: ID 1번 제품의 가격과 이름 변경)
db.update_product(1, product_name="Updated Product 1", price=299.99)

# 특정 제품 조회 (예: ID 1번 제품)
print(db.select_product(1))

# 제품 삭제 (예: ID 100번 제품)
db.delete_product(100)

# 삭제 후 모든 제품 조회
products = db.select_product()
for product in products:
    print(product)

# 데이터베이스 연결 종료
db.close()
