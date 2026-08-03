from app.memory.manager import MemoryManager
from app.memory.short_term import ShortTermMemory


def main():

    # Create Manager
    manager = MemoryManager()

    # Create Memory
    memory = ShortTermMemory()

    # Register Memory
    manager.register_memory(memory)

    print("\n===== Registered Memories =====")
    print(manager.get_all_memories().keys())

    # Get Memory
    short_term = manager.get_memory("short_term")

    # Save
    short_term.save(
        "planner",
        "Planner completed successfully."
    )

    short_term.save(
        "database",
        "Database schema created."
    )

    print("\n===== Stored Data =====")
    print(short_term.get_all())

    # Get
    print("\n===== Get Planner =====")
    print(short_term.get("planner"))

    # Delete
    short_term.delete("planner")

    print("\n===== After Delete =====")
    print(short_term.get_all())

    # Clear
    short_term.clear()

    print("\n===== After Clear =====")
    print(short_term.get_all())


if __name__ == "__main__":
    main()