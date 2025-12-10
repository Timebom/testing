# multiagent_debate/evolution/evolver.py
import random
from database.storage import get_agent_stats

async def evolve_agents(agents: list, scores_this_round: dict):
    # 1. Eliminate worst performer this round (temporary)
    loser = min(scores_this_round.items(), key=lambda x: x[1])[0]
    for agent in agents:
        if agent.name == loser:
            agent.eliminated = True
            print(f"[red]ELIMINATED this debate: {loser}[/]")

    # 2. Permanent evolution: boost temperature & confidence for winners
    stats = {}
    for agent in agents:
        stats[agent.name] = await get_agent_stats(agent.name)

    # Winners get bolder over time
    for agent in agents:
        win_rate = stats[agent.name]["wins"] / max(1, stats[agent.name]["battles"])
        agent.temperature_boost = min(1.3, 0.7 + win_rate * 0.6)
        agent.confidence = win_rate