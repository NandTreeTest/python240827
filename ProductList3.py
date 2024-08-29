import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path

#데이터베이스 처리 클래스 (DAO)
class ProductDatabase:
    def __init__(self, db_name="ProductList.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        제품 테이블을 생성합니다.
        """
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Price INTEGER NOT NULL
        );""")
        self.conn.commit()

    def add_product(self, name, price):
        """
        새로운 제품을 데이터베이스에 추가합니다.
        """
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, price))
        self.conn.commit()

    def update_product(self, prod_id, name, price):
        """
        기존 제품의 정보를 업데이트합니다.
        """
        self.cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?;", (name, price, prod_id))
        self.conn.commit()

    def remove_product(self, prod_id):
        """
        제품을 데이터베이스에서 삭제합니다.
        """
        self.cur.execute("DELETE FROM Products WHERE id=?;", (prod_id,))
        self.conn.commit()

    def get_all_products(self):
        """
        모든 제품을 가져옵니다.
        """
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()

    def close(self):
        """
        데이터베이스 연결을 닫습니다.
        """
        self.conn.close()


# 디자인 파일 로드
form_class = uic.loadUiType("ProductList3.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 데이터베이스 객체 생성
        self.db = ProductDatabase()

        # QTableWidget 설정
        self.setup_table()

        # 이벤트 연결
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 초기 제품 리스트 로드
        self.getProduct()

    def setup_table(self):
        """
        QTableWidget 초기 설정을 합니다.
        """
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)

    def addProduct(self):
        """
        새로운 제품을 추가합니다.
        """
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db.add_product(name, price)
        self.getProduct()

    def updateProduct(self):
        """
        기존 제품의 정보를 업데이트합니다.
        """
        prod_id = self.prodID.text()
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db.update_product(prod_id, name, price)
        self.getProduct()

    def removeProduct(self):
        """
        제품을 삭제합니다.
        """
        prod_id = self.prodID.text()
        self.db.remove_product(prod_id)
        self.getProduct()

    def getProduct(self):
        """
        제품 리스트를 가져와서 QTableWidget에 표시합니다.
        """
        self.tableWidget.clearContents()
        products = self.db.get_all_products()
        
        for row, item in enumerate(products):
            itemID = QTableWidgetItem(str(item[0]))
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)
            
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))

            itemPrice = QTableWidgetItem(str(item[2]))
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

    def doubleClick(self):
        """
        QTableWidget의 행을 더블클릭하면 제품 정보를 로드합니다.
        """
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

    def closeEvent(self, event):
        """
        윈도우가 닫힐 때 데이터베이스 연결을 종료합니다.
        """
        self.db.close()
        event.accept()


# 인스턴스를 생성한다.
app = QApplication(sys.argv)
myWindow = Window()
myWindow.show()
app.exec_()
