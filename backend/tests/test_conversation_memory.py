from app.memory.manager import MemoryManager
from app.memory.conversation import ConversationMemory


def main():

    manager = MemoryManager()

    conversation = ConversationMemory()

    manager.register_memory(conversation)

    print("\n===== Registered Memories =====")
    print(manager.get_all_memories().keys())

    memory = manager.get_memory("conversation")

    # Save conversation
    memory.save(
        "user",
        "Explain FastAPI"
    )

    memory.save(
        "assistant",
        "FastAPI is a modern Python web framework."
    )

    memory.save(
        "user",
        "What is dependency injection?"
    )

    print("\n===== Conversation =====")
    for message in memory.get_all():
        print(message)

    print("\n===== First Message =====")
    print(memory.get(0))

    print("\n===== Delete First Message =====")
    memory.delete(0)

    for message in memory.get_all():
        print(message)

    print("\n===== Clear =====")
    memory.clear()

    print(memory.get_all())


if __name__ == "__main__":
    main()