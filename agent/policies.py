BLOCKED_COMMANDS = (
    "format ",
    "rm -rf",
    "shutdown",
    "del /s",
)


def is_command_allowed(command: str) -> bool:
    """Return False when a potentially destructive command is detected."""

    command_lower = command.lower()

    return not any(
        blocked in command_lower
        for blocked in BLOCKED_COMMANDS
    )
