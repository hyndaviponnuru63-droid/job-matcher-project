from db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT * FROM users")
print("Users table OK")

cur.execute("SELECT * FROM jobs")
print("Jobs table OK")

cur.execute("SELECT * FROM saved_jobs")
print("Saved_jobs table OK")

conn.close()
