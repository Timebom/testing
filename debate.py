import uuid
from .agent import Agent
from .referee import Referee
from ..ui.rich_display import show_round, console
from ..config import DebateConfig

class Debate:
    def __init__(self, topic: str, config: DebateConfig = None):
        self.topic = topic
        self.config = config or DebateConfig()
        self.debate_id = str(uuid.uuid4())[:8]
        self.agents = [
            Agent("Visionary", "excited futurist who sees infinite possibility", "bright_cyan"),
            Agent("Cynic", "brutal skeptic who destroys weak ideas", "bright_red"),
            Agent("Engineer", "pragmatic builder who demands working solutions", "bright_green"),
            Agent("Ethicist", "deep moral philosopher questioning everything", "bright_magenta"),
            Agent("Capitalist", "profit-obsessed entrepreneur", "yellow"),
        ]
        self.referee = Referee()
        self.scores = {a.name: 0 for a in self.agents}

    def run(self):
        console.print(Panel(f"[bold yellow]DEBATE: {self.topic}[/]", style="bold blue"))

        for round_num in range(1, self.config.num_rounds + 1):
            responses = []
            for agent in self.agents:
                reply = agent.respond(self.topic, self.debate_id, round_num)
                responses.append({"agent": agent.name, "text": reply})

            judgment = self.referee.evaluate_round(self.topic, responses)

            # Update scores
            for name, data in judgment.get("scores", {}).items():
                if name in self.scores:
                    self.scores[name] += data["total"]

            show_round(round_num, responses, judgment)

        # Final
        winner = max(self.scores.items(), key=lambda x: x[1])
        console.print(Panel(self.referee.final_verdict(self.scores, self.topic),
                            title="FINAL VERDICT", border_style="bright_white"))