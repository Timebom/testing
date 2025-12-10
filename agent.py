from ..llm.gemini_client import GeminiClient
from ..memory.shared_memory import SharedMemory

class Agent:
    def __init__(self, name: str, personality: str, color: str = "white"):
        self.name = name
        self.personality = personality
        self.color = color
        self.llm = GeminiClient()
        self.memory = SharedMemory()

    def respond(self, topic: str, debate_id: str, round_num: int) -> str:
        context = self.memory.get_context(debate_id)

        prompt = f"""
You are {self.name}, {self.personality}.
You remember the full debate so far and adapt your arguments accordingly.

Topic: {topic}

Recent turns:
{context if context else "No previous turns yet."}

It's now Round {round_num}. Respond in 2–4 powerful sentences.
Be sharper and more informed than before. Do not repeat old points.
"""

        response = self.llm.generate(prompt, temperature=0.8)
        self.memory.add_turn(debate_id, self.name, response, round_num)
        return response