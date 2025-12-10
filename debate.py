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

    async def run(self):
    await init_db()
    console.print(Panel(f"[bold red]EVOLUTIONARY DEBATE: {self.topic}[/]"))

    active_agents = self.agents.copy()

    for round_num in range(1, self.config.num_rounds + 1):
        console.print(f"\n[bold]Round {round_num} | Active: {len(active_agents)} agents[/]")

        # Parallel response from ACTIVE agents only
        tasks = [a.respond(self.topic, self.debate_id, round_num) for a in active_agents]
        responses = await asyncio.gather(*tasks)

        round_responses = [{"agent": a.name, "text": r} for a, r in zip(active_agents, responses)]

        # Referee judges
        judgment = await self.referee.evaluate_round(self.topic, round_responses)

        # Save every response
        round_scores = {}
        for resp, agent in zip(round_responses, active_agents):
            name = resp["agent"]
            score_data = judgment["scores"].get(name, {})
            round_scores[name] = score_data.get("total", 0)

            await save_turn(
                debate_id=self.debate_id,
                round_num=round_num,
                agent_name=name,
                personality=agent.personality,
                prompt="...",  # you can hash or truncate
                response=resp["text"],
                scores=score_data,
                is_winner=(judgment.get("winner") == name)
            )

        # Inside Debate.run(), after judgment:

# === REFLECTIVE EVOLUTION PHASE ===
console.print("\n[bold magenta]REFLECTIVE IMPROVEMENT PHASE — All agents evolve[/]")

reflection_tasks = []
for agent, original_text in zip(self.agents, responses_text_list):
    task = reflective_improvement(
        agent=agent,
        topic=self.topic,
        original_response=original_text,
        winning_response=winning_response_text,
        winner_name=judgment["winner"],
        winner_reason=judgment["winner_reason"],
        debate_id=self.debate_id,
        round_num=round_num
    )
    reflection_tasks.append(task)

# All agents improve in parallel
improved_versions = await asyncio.gather(*reflection_tasks)

# Show one example
console.print(f"[dim]{judgment['winner']} was already strong, but others just got smarter.[/]")
console.print(f"[italic]Example evolution — {self.agents[0].name} v2:[/] {improved_versions[0][:120]}...")

        # EVOLUTION STEP
        await evolve_agents(active_agents, round_scores)

        # Remove eliminated agents from next round
        active_agents = [a for a in active_agents if not getattr(a, 'eliminated', False)]

        if len(active_agents) <= 1:
            console.print("[bold red]Only one remains![/]")
            break

        show_round(round_num, round_responses, judgment)

    # Final survivor
    survivor = max(self.scores.items(), key=lambda x: x[1])[0]
    console.print(Panel(f"[bold gold]ULTIMATE SURVIVOR: {survivor}[/]", title="EVOLUTION COMPLETE"))