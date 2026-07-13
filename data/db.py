import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path(__file__).parent / "store.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS scores (
                id TEXT PRIMARY KEY,
                nickname TEXT NOT NULL,
                category TEXT NOT NULL,
                score INTEGER NOT NULL,
                total INTEGER NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS photos (
                id TEXT PRIMARY KEY,
                nickname TEXT NOT NULL,
                caption TEXT,
                filename TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )


def add_score(nickname, category, score, total):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO scores (id, nickname, category, score, total, created_at) VALUES (?, ?, ?, ?, ?, ?)",
            (
                str(uuid.uuid4()),
                nickname[:30],
                category,
                score,
                total,
                datetime.now(timezone.utc).isoformat(),
            ),
        )


def get_leaderboard(category=None, limit=50):
    with get_connection() as conn:
        if category:
            rows = conn.execute(
                "SELECT * FROM scores WHERE category = ? ORDER BY (CAST(score AS FLOAT) / total) DESC, created_at DESC LIMIT ?",
                (category, limit),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM scores ORDER BY (CAST(score AS FLOAT) / total) DESC, created_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [dict(r) for r in rows]


def add_photo(nickname, caption, filename):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO photos (id, nickname, caption, filename, created_at) VALUES (?, ?, ?, ?, ?)",
            (
                str(uuid.uuid4()),
                nickname[:30],
                (caption or "")[:200],
                filename,
                datetime.now(timezone.utc).isoformat(),
            ),
        )


def get_photos(limit=200):
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM photos ORDER BY created_at DESC LIMIT ?", (limit,)
        ).fetchall()
        return [dict(r) for r in rows]
