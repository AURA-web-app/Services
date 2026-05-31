from logger import logs

def top_requested_topics():
    topics = {}

    for log in logs:
        if log["event_type"] != "ai_request":
            continue
        topic = log["metadata"].get(
            "topic",
            "unknown"
        )
        topics[topic] = (
            topics.get(topic, 0) + 1
        )

    sorted_topics = sorted(
        topics.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_topics[:5]