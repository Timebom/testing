import json
import re
from ..llm.gemini_client import GeminiClient

class Referee:
    def __init__(self):
        self.llm = GeminiClient()

    def evaluate_round(self, topic: str, responses: list[dict]) -> dict:
        responses_text = "\n\n".join([f"{r['agent']}: {r['text']}" for r in responses])

        prompt = f"""
Strict Referee Judgment

Topic: {topic}

{responses_text}

Score each agent 1–10 on:
- Clarity & Logic
- Persuasiveness
- Originality
- Respectfulness

Then pick ONE winner.

Return ONLY valid JSON:
{{
  "scores": {{"Agent Name": {{"clarity":9, "persuasiveness":8, "originality":9, "respectfulness":10, "total":36, "justification":"..."}}}},
  "winner": "Name",
  "winner_reason": "2 sentences max."
}}
"""

        raw = self.llm.generate(prompt, temperature=0.3)

        # Extract JSON
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except:
                pass
        # Fallback
        return {"scores": {}, "winner": "Unknown", "winner_reason": "Parsing failed"}

    def final_verdict(self, scores: dict, topic: str) -> str:
        lines = "\n".join([f"- {name}: {score} pts" for name, score in scores.items()])
        prompt = f"Topic: {topic}\n\nFinal scores:\n{lines}\n\nDramatic final announcement (3 sentences max):"
        return self.llm.generate(prompt, temperature=0.9)