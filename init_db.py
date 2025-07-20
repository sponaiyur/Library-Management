import mysql.connector as ms

def initialize_schema():
    conn = ms.connect(host='localhost',user='root',passwd='*****',database='^^^^^')
    cursor = conn.cursor()

    with open("schema.sql", "r") as f:
        sql_statements = f.read()

    for statement in sql_statements.strip().split(";"):
        if statement.strip():
            try:
                cursor.execute(statement + ";")
            except Exception as e:
                print(f"[ERROR] Failed on statement:\n{statement.strip()}\n{e}")

    conn.commit()
    conn.close()
    print("[INFO] Database schema initialized successfully.")

if __name__ == "__main__":
    initialize_schema()
