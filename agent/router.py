def route_task(task: str) -> str:
    """Route a task to the most appropriate agent."""

    text = task.lower()

    coding_terms = (
        "code", "bug", "python", "javascript",
        "repository", "github", "implement", "debug"
    )

    browser_terms = (
        "website", "web", "browser", "search",
        "online", "navigate", "open", "visit",
        "google", "url", "page"
    )

    if any(term in text for term in coding_terms):
        return "coding"

    if any(term in text for term in browser_terms):
        return "browser"

    return "general"
