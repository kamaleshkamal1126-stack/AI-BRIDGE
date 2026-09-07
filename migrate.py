import sqlite3
import os

db_path = os.path.join("instance", "ai_bridge.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check existing columns
cursor.execute("PRAGMA table_info(user)")
columns = [row[1] for row in cursor.fetchall()]

if "department" not in columns:
    cursor.execute("ALTER TABLE user ADD COLUMN department VARCHAR(100)")
    print("✅ Added department")

if "year" not in columns:
    cursor.execute("ALTER TABLE user ADD COLUMN year VARCHAR(50)")
    print("✅ Added year")

if "location" not in columns:
    cursor.execute("ALTER TABLE user ADD COLUMN location VARCHAR(100)")
    print("✅ Added location")

conn.commit()
conn.close()

print("\n🎉 Database migration completed successfully!")