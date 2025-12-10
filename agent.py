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
        if self.eliminated:
            return "... (eliminated this debate)"

        # Try to recall a winning response
        past_winner = await get_best_response(self.name, topic)
        recall = f"Recall your past winning argument: {past_winner}\n" if past_winner else ""

        context = SharedMemory().get_context(debate_id)
        prompt = f"""
{recall}
You are {self.name}, {self.personality}.
You have won {await get_agent_stats(self.name)}['wins']} times before.
Be more persuasive than ever.

Topic: {topic}
Round: {round_num}

Recent:
{context or "Start strong."}

Respond in 2–4 powerful, evolved sentences.
"""

        response = await self.llm.generate(prompt, temperature=self.temperature_boost)
        return response