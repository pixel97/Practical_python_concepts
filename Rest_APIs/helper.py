import sqlite3

DB_PATH = './todo.db'
NOT_STARTED = 'Not Started'
IN_PROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        print("DB connected")
        cur = conn.cursor()
        print("Cursor created")
        cur.execute('insert into items (item,status) values(?,?)', (item,NOT_STARTED))
        print("values inserted")
        conn.commit()
        return {"ITEM":item,"STATUS":NOT_STARTED}
    except Exception as e:
        print('Error',e)
        return None

def get_all_items():
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('select * from items')
        rows = cur.fetchall()
        return {"count":len(rows),"items":rows}
    except Exception as e:
        print('Error', e)
        return None

def get_item_status(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("select status from items where item = '%s'" % item)
        status = cur.fetchone()[0]
        return status
    except Exception as e:
        print('Error',e)
        return None

def update_item(item,status):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("update items set status=? where item=?", (status,item))
        conn.commit()
        return status
    except Exception as e:
        print('Error',e)
        return None

def delete_item(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("delete from items where item=?", (item,))
        conn.commit()
        return {"item":item}
    except Exception as e:
        print('Error',e)
        return None







