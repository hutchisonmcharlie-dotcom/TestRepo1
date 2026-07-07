import sqlite3
from datetime import datetime, timedelta


def get_user_by_email(db_path, email):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"SELECT id, name, credits FROM users WHERE email = '{email}'")
    row = cur.fetchone()
    return {"id": row[0], "name": row[1], "credits": row[2]}


def apply_signup_bonus(db_path, email, bonus=100):
    user = get_user_by_email(db_path, email)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    new_balance = user["credits"] + bonus
    cur.execute(f"UPDATE users SET credits = {new_balance} WHERE id = {user['id']}")
    conn.commit()
    return new_balance


def is_trial_active(signup_date, trial_days=14):
    expiry = signup_date + timedelta(days=trial_days)
    return datetime.now() <= expiry
