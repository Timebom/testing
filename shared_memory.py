from typing import List, Dict, Any
from collections import defaultdict
import time

class SharedMemory:
    def __init__(self):
        self.memory: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        self.timestamps: Dict[str, float] = {}

    def add_turn(self, debate_id: str, agent: str, text: str, round_num: int):
        entry = {
            "agent": agent,
            "text": text,
            "round": round_num,
            "timestamp": time.time()
        }
        self.memory[debate_id].append(entry)
        self.timestamps[debate_id] = time.time()

    def get_context(self, debate_id: str, last_n: int = 6) -> str:
        turns = self.memory.get(debate_id, [])[-last_n:]
        return "\n".join([f"{t['agent']}: {t['text']}" for t in turns])