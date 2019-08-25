from PyQt5 import QtWidgets,QtCore
from master import Ui_MainWindow
from add_patient import add_patient
import sys,os
import getpass
import sqlite3
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
 
    return None

def delete_data(conn, data):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    print('Deleted %s'%str(data))
    sql = ''' DELETE INTO patients 
              VALUES(?,?,?,?) '''
    sql = '''DELETE FROM patients WHERE name = ? AND address=? AND contact =? AND prescription=?'''
          
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    print('done')

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect()
        username = getpass.getuser()
        db_file =  "C:\\Users\\%s\\Documents\\DocDir\\DocDirpythonsqlite.db"%username
        print (db_file)
        if not os.path.exists(os.path.dirname(db_file)):
            os.makedirs(os.path.dirname(db_file))
        self.conn = create_connection(db_file)
        self.cur = self.conn.cursor()
        self.ui.datatree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.datatree.customContextMenuRequested.connect(self.menuContextTree)
        if self.conn:
            self.refresh_tree()

    def refresh_tree(self):
        try:
            self.data = self.read_from_db()
            self.write_data()
        except:
            pass

    def menuContextTree(self, point):
        # Infos about the node selected.
        index = self.ui.datatree.indexAt(point)

        if not index.isValid():
            return

        item = self.ui.datatree.itemAt(point)
        name = item.text(0)
        # We build the menu.
        menu = QtWidgets.QMenu()
        refresh_action = menu.addAction("refresh")
        action = menu.addAction(name)
        menu.addSeparator()
        edit_action = menu.addAction("Edit")
        delete_action = menu.addAction("delete")
        action = menu.exec_(self.ui.datatree.mapToGlobal(point))

        if action is not None:
            if action == edit_action:
                self.edit_info(item)
            elif action == refresh_action:
                self.refresh_tree()
            elif action == delete_action:
                self.delete_info(item)

    def connect(self):
        self.ui.add_patient.clicked.connect(self.add)

    def edit_info(self,item):
        application = add_patient(self,item,True)
        application.show()

    def delete_info(self,item):
        name = item.text(0)
        address = item.text(1)
        contact = item.text(2)
        prescription = item.text(3)
        data = (name,address,contact,prescription)
        delete_data(self.conn,data)
        self.refresh_tree()        

    def add(self):
        application = add_patient(self)
        application.show()
    
    def read_from_db(self):
        self.cur.execute("SELECT * FROM patients")
        data = self.cur.fetchall()
        return data
    
    def write_data(self):
        self.ui.datatree.clear()
        for each in self.data:
            item = QtWidgets.QTreeWidgetItem(self.ui.datatree)
            item.setText(0,each[0])
            item.setText(1,each[1])
            item.setText(2,each[2])
            item.setText(3,each[3])
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()