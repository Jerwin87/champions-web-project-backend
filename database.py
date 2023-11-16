import sqlite3

con = sqlite3.connect("../database/database.db")

cur = con.cursor()



def get_aspect(aspect_id: int):
    query = f"SELECT * FROM aspects WHERE aspect_id={aspect_id}"
    try:
        res = cur.execute(query)
    except sqlite3.OperationalError: 
        return {"ERROR": "sqlite3.OperationalError"}
    else:
        aspect = res.fetchone()
        if aspect is None:
            return {"message": "aspect not found"}
        else:
            return aspect
    
print(get_aspect(aspect_id=7))





