from database.storage import get_best_response, save_turn

class Agent:
    def __init__(self, name: str, personality: str, color: str):
        self.name = name
        self.personality = personality
        self.color = color
        self.eliminated = False
        self.temperature_boost = 0.7
        self.llm = AsyncGeminiClient()

    async def respond(self, topic: str, debate_id: str, round_num: int) -> str:
    # 1. Try to find a past reflective/improved response on similar topic
    past_gold = await get_best_reflective_response(self.name, topic)
    
    inspiration = ""
    if past_gold:
        inspiration = f"""
You once reflected and created this superior answer on a similar topic:
"{past_gold}"

Use that wisdom. Build on it. Go further.
"""

    context = SharedMemory().get_context(debate_id)

    prompt = f"""
{inspiration}
You are {self.name}, {self.personality} — continuously improving.

You have reflected and learned from past defeats and victories.
Topic: {topic}
Round: {round_num}

Recent turns:
{context or "Be the first to set the tone."}

Answer in 2–4 exceptionally strong sentences.
This is your chance to show growth.
"""

    response = await self.llm.generate(prompt, temperature=0.7 + (round_num * 0.1))
    return response