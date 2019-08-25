from PyQt5 import QtWidgets
from add import Ui_MainWindow
import sys
import sqlite3
import getpass
from sqlite3 import Error

 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        print('connected')
        return conn
    except Error as e:
        print(e)
 
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def update_data(conn, data,data1):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """

    print('started updating')
    sql = '''UPDATE patients SET name = ? , address = ? , contact=? , prescription=?  WHERE name = ? AND address=? AND contact =? AND prescription=?'''
    cur = conn.cursor()
    data = data+data1
    cur.execute(sql, data)
    conn.commit()
    print('done')


def add_data(conn, data):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    print('started inserting')
    sql = ''' INSERT INTO patients 
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    print('done')

def add_data_column(conn):
    sql_create_patients_table = """ CREATE TABLE IF NOT EXISTS patients (
                                        name text NOT NULL,
                                        address text,
                                        contact text,
                                        prescription text
                                    ); """
    # create a database connection
    
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_patients_table)
        # create tasks table
    else:
        print("Error! cannot create the database connection.")

class add_patient(QtWidgets.QMainWindow):
    def __init__(self,mi,item=None,edit_check=False):
        super(add_patient, self).__init__(mi)
        self.mui = mi
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.edit_check = edit_check
        self.item = item
        if self.edit_check:
            self.ui.label.setText('Edit Patient Details')
            self.ui.name_txt.setText(self.item.text(0))
            self.ui.address_txt.setText(self.item.text(1))
            self.ui.contact_txt.setText(self.item.text(2))
            self.ui.prescript_txt.setText(self.item.text(3))
        username = getpass.getuser()    
        db_file =  "C:\\Users\\%s\\Documents\\DocDir\\DocDirpythonsqlite.db"%username
        self.conn = create_connection(db_file)
        self.cur = self.conn.cursor()
        try:
            self.data = self.read_from_db()
        except:
            pass
        self.connect()

    def connect(self):
        self.ui.ok_btn.clicked.connect(self.ok_pressed)
        self.ui.cancel_btn.clicked.connect(self.exit)

    def exit(self):
        self.close()

    def read_from_db(self):
        self.cur.execute("SELECT * FROM patients")
        data = self.cur.fetchall()
        return data

    def ok_pressed(self):
        if self.edit_check:
            add_data_column(self.conn)
            old_name = self.item.text(0)
            old_address = self.item.text(1)
            old_contact = self.item.text(2)
            old_prescription = self.item.text(3)
            name = self.ui.name_txt.text()
            address = self.ui.address_txt.text()
            contact = self.ui.contact_txt.text()
            prescript = self.ui.prescript_txt.toPlainText()
            new_data = (name,address,contact,prescript)
            old_data = (old_name,old_address,old_contact,old_prescription)
            if contact:
                try:
                    x = int(contact)
                    che=True
                except:
                    infoBox = QtWidgets.QMessageBox()
                    infoBox.setIcon(QtWidgets.QMessageBox.Information)
                    infoBox.setText("Please Write contact information in Digits ")
                    infoBox.setWindowTitle("Information")
                    infoBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    infoBox.exec_()
                    print('unable to convert')
                    che=False
            else:
                che=True
                print ('No contact ')
            if che:
                data = (name,address,contact,prescript)
                update_data(self.conn,new_data,old_data)
                self.mui.refresh_tree()
                self.close()
        else:
            add_data_column(self.conn)
            name = self.ui.name_txt.text()
            address = self.ui.address_txt.text()
            contact = self.ui.contact_txt.text()
            prescript = self.ui.prescript_txt.toPlainText()
            che = bool()
            if contact:
                try:
                    x = int(contact)
                    che=True
                except:
                    infoBox = QtWidgets.QMessageBox()
                    infoBox.setIcon(QtWidgets.QMessageBox.Information)
                    infoBox.setText("Please Write contact information in Digits ")
                    infoBox.setWindowTitle("Information")
                    infoBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    infoBox.exec_()
                    print('unable to convert')
                    che=False
            else:
                che=True
                print ('No contact ')
            if che:
                data = (name,address,contact,prescript)
                add_data(self.conn,data)
                self.mui.refresh_tree()
                self.close()
            



        
        
    


