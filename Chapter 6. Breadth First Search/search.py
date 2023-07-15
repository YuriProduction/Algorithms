from collections import deque

people = dict()
people["You"] = ["Bob", "Alice", "Clar"]
people["Clar"] = ["Tom", "Johni"]
people["Alice"] = ["Peggi"]
people["Peggi"] = ["Bob"]
people["Bob"] = ["Anudj"]
people["Anudj"] = []
people["Tom"] = []
people["Johni"] = []


def BFS(abstractGraph: dict, startKey):
    search_queue = deque()
    search_queue += abstractGraph[startKey]
    visited = []
    while search_queue:
        item = search_queue.popleft()
        if item not in visited:
            # If we search Anudj for example
            if item.endswith("udj"):
                return item
            else:
                search_queue += abstractGraph[item]
                visited.append(item)
    return None


print(BFS(people, "You"))
