from collections import deque


class TaskQueue:
    """
    FIFO queue for agent execution.
    """

    def __init__(self):
        self.queue = deque()

    def enqueue(self, agent_name: str):
        """
        Add an agent to the queue.
        """
        self.queue.append(agent_name)

    def dequeue(self):
        """
        Remove and return the next agent.
        """
        if self.is_empty():
            return None

        return self.queue.popleft()

    def peek(self):
        """
        View the next agent without removing it.
        """
        if self.is_empty():
            return None

        return self.queue[0]

    def is_empty(self):
        """
        Check whether the queue is empty.
        """
        return len(self.queue) == 0

    def size(self):
        """
        Number of queued agents.
        """
        return len(self.queue)

    def clear(self):
        """
        Remove all queued agents.
        """
        self.queue.clear()

    def get_all(self):
        """
        Return queued agents.
        """
        return list(self.queue)