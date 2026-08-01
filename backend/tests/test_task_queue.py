import sys
from pathlib import Path

# Add backend folder to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.orchestrator.task_queue import TaskQueue

queue = TaskQueue()

print("===== Enqueue =====")
queue.enqueue("planner")
queue.enqueue("research")
queue.enqueue("database")

print(queue.get_all())

print("\n===== Peek =====")
print(queue.peek())

print("\n===== Size =====")
print(queue.size())

print("\n===== Is Empty =====")
print(queue.is_empty())

print("\n===== Dequeue =====")
print(queue.dequeue())
print(queue.dequeue())

print("\n===== Queue After Dequeue =====")
print(queue.get_all())

print("\n===== Clear =====")
queue.clear()
print(queue.get_all())

print("\n===== Empty Queue =====")
print(queue.is_empty())