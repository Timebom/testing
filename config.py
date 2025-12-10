from dataclasses import dataclass

@dataclass
class DebateConfig:
    model_name: str = "gemini-1.5-flash"  # or "gemini-1.5-pro"
    temperature: float = 0.7
    max_output_tokens: int = 1024
    num_rounds: int = 3
    cache_ttl_seconds: int = 3600  # 1 hour cache