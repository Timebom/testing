from multiagent_debate.core.debate import Debate
from multiagent_debate.config import DebateConfig

if __name__ == "__main__":
    config = DebateConfig(num_rounds=4, model_name="gemini-1.5-pro")
    debate = Debate("Should AI agents replace human politicians by 2035?", config)
    debate.run()