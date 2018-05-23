import collections

MatchResult = collections.namedtuple('MatchResult',
        ('winning_team', 'losing_team'))


def can_team_at_beat_team_b(matches, team_a, team_b):
    def build_graph():
        graph = collections.defaultdict(set)
        for match in matches:
            graph[match.winning_team].add(match.losing_team)

        return graph

    def is_reachable_dfs(graph, cur, dest, visited=set()):
        if cur == dest:
            return True
        elif cur in visited or cur not in graph:
            print("IN", cur in visited, cur not in graph, cur)
            return False
        visited.add(cur)
        print(visited, cur)
        return any(is_reachable_dfs(graph, team, dest) for team in graph[cur])

        for child in graph[cur]:
            if child not in visited:
                visited.add(child)
                return is_reachable_dfs(graph, child, dest, visited)
        return False


    return is_reachable_dfs(build_graph(), team_a, team_b)


def testSuite():
    matches = [MatchResult(a, b) for a,b in zip(range(10), range(1,11))]
    print(can_team_at_beat_team_b(matches, 0, 10))
    print(can_team_at_beat_team_b(matches, 4, 11))


testSuite()
