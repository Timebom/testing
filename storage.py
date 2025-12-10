# multiagent_debate/database/storage.py
import aiosqlite
import asyncio
from datetime import datetime
from typing import List, Dict, Optional

DB_PATH = "debate_evolution.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS debate_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            debate_id TEXT,
            round_num INTEGER,
            agent_name TEXT,
            personality TEXT,
            prompt TEXT,
            response TEXT,
            clarity INTEGER,
            persuasiveness INTEGER,
            originality INTEGER,
            respectfulness INTEGER,
            total_score INTEGER,
            justification TEXT,
            is_winner BOOLEAN,
            is_eliminated BOOLEAN DEFAULT 0,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        await db.commit()

# Call once at startup
asyncio.create_task(init_db())

async def save_turn(
    debate_id: str, round_num: int, agent_name: str, personality: str,
    prompt: str, response: str, scores: Dict, is_winner: bool = False
):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
        INSERT INTO debate_history 
        (debate_id, round_num, agent_name, personality, prompt, response,
         clarity, persuasiveness, originality, respectfulness, total_score,
         justification, is_winner)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            debate_id, round_num, agent_name, personality, prompt, response,
            scores.get('clarity',0), scores.get('persuasiveness',0),
            scores.get('originality',0), scores.get('respectfulness',0),
            scores.get('total',0), scores.get('justification',''),
            int(is_winner)
        ))
        await db.commit()

async def get_agent_stats(agent_name: str) -> Dict:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute("""
            SELECT AVG(total_score) as avg_score, COUNT(*) as battles,
                   SUM(is_winner) as wins
            FROM debate_history WHERE agent_name = ?
        """, (agent_name,))
        row = await cursor.fetchone()
        return dict(row) if row else {"avg_score": 0, "battles": 0, "wins": 0}

async def get_best_response(agent_name: str, topic: str) -> Optional[str]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("""
            SELECT response FROM debate_history
            WHERE agent_name = ? AND total_score > 30
            AND prompt LIKE ?
            ORDER BY total_score DESC LIMIT 1
        """, (agent_name, f"%{topic[:50]}%"))
        row = await cursor.fetchone()
        return row[0] if row else None