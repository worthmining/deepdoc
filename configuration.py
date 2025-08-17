import uuid

LLM_CONFIG = {
    "provider": "openai",
    "model": "gpt-4o-mini", 
    "temperature": 0.5,
}

THREAD_CONFIG = {
    "configurable": {
        "thread_id": str(uuid.uuid4()),
        "max_queries": 3,
        "search_depth": 2,
        "num_reflections": 2,
        "n_points": 1,
    }
}
