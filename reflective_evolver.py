# multiagent_debate/evolution/reflective_evolver.py
import asyncio
from database.storage import save_turn
from llm.gemini_client import AsyncGeminiClient

llm = AsyncGeminiClient()

async def reflective_improvement(
    agent,
    topic: str,
    original_response: str,
    winning_response: str,
    winner_name: str,
    winner_reason: str,
    debate_id: str,
    round_num: int
):
    """
    Every agent reflects and produces a better version of their answer.
    This improved response becomes training data forever.
    """
    prompt = f"""
You are {agent.name} ({agent.personality}).

In the last round about: "{topic}"

You originally said:
"{original_response}"

But {winner_name} won with:
"{winning_response}"

The referee said: {winner_reason}

Now, honestly reflect and answer the same topic AGAIN — but this time:
- Keep your unique personality
- Steal what made {winner_name} win
- Fix your weaknesses
- Be sharper, deeper, more persuasive

Respond in 2–4 powerful sentences.
This improved version will become your new standard.
"""

    improved = await llm.generate(prompt, temperature=0.9)

    # Save the evolved response as a "gold" example
    await save_turn(
        debate_id=debate_id,
        round_num=round_num,
        agent_name=agent.name,
        personality=agent.personality,
        prompt=f"[REFLECTIVE IMPROVEMENT] {topic}",
        response=improved,
        scores={
            "clarity": 10, "persuasiveness": 10, "originality": 9, "respectfulness": 10,
            "total": 39,
            "justification": f"Self-improved after learning from {winner_name}"
        },
        is_winner=False
    )

    return improved