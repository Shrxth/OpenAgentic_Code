from agent.router import route_task


def test_coding_task():
    assert route_task("Fix this Python bug") == "coding"


def test_browser_task():
    assert route_task("Search this website") == "browser"


def test_general_task():
    assert route_task("Hello agent") == "general"
