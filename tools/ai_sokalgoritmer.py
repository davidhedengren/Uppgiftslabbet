"""Sökalgoritmer för AI-bankens uppgifter (labyrinter, träd, grafer, spelträd)."""
import heapq

UP, RIGHT, DOWN, LEFT = (-1, 0), (0, 1), (1, 0), (0, -1)
STD = (UP, RIGHT, DOWN, LEFT)


def cname(rc):
    return chr(65 + rc[0]) + str(rc[1] + 1)


def parse(rows):
    """'#' vägg, '.' gång, 'S' start, 'G' mål, siffra = kostnad att gå in i rutan."""
    start = goal = None
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == 'S':
                start = (r, c)
            if ch == 'G':
                goal = (r, c)
    return start, goal


def open_cell(rows, rc):
    r, c = rc
    return 0 <= r < len(rows) and 0 <= c < len(rows[0]) and rows[r][c] != '#'


def neigh(rows, rc, order=STD):
    return [(rc[0] + a, rc[1] + b) for a, b in order if open_cell(rows, (rc[0] + a, rc[1] + b))]


def cost(rows, rc):
    ch = rows[rc[0]][rc[1]]
    return int(ch) if ch.isdigit() else 1


def path_from(parent, goal):
    p = [goal]
    while p[-1] in parent:
        p.append(parent[p[-1]])
    return p[::-1]


def bfs(rows, order=STD, start=None, goal=None):
    s, g = parse(rows)
    start = start or s
    goal = goal or g
    q = [start]
    seen = {start}
    parent = {}
    out = []
    snaps = []  # (uttagen, kö efter uttaget och inläggning)
    while q:
        n = q.pop(0)
        out.append(n)
        if n == goal:
            snaps.append((n, list(q)))
            return dict(order=out, path=path_from(parent, goal), snaps=snaps, found=True)
        for v in neigh(rows, n, order):
            if v not in seen:
                seen.add(v)
                parent[v] = n
                q.append(v)
        snaps.append((n, list(q)))
    return dict(order=out, path=[], snaps=snaps, found=False)


def dist_all(rows, start):
    d = {start: 0}
    q = [start]
    while q:
        n = q.pop(0)
        for v in neigh(rows, n):
            if v not in d:
                d[v] = d[n] + 1
                q.append(v)
    return d


def dfs(rows, order=STD):
    start, goal = parse(rows)
    seen = set()
    out = []
    parent = {}
    backtracks = []  # (ruta där DFS fastnar, ruta den fortsätter från)
    stack_path = []

    def visit(n):
        seen.add(n)
        out.append(n)
        stack_path.append(n)
        if n == goal:
            return True
        for v in neigh(rows, n, order):
            if v not in seen:
                parent[v] = n
                if visit(v):
                    return True
        stack_path.pop()
        return False

    visit(start)
    return dict(order=out, path=path_from(parent, goal), found=goal in seen)


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(rows, tie_name=True):
    """A* med kostnad per inträdd ruta. Vid lika f: lägst h, sedan rutnamn."""
    start, goal = parse(rows)
    g = {start: 0}
    parent = {}
    closed = set()
    out = []
    openl = {start}
    while openl:
        n = min(openl, key=lambda x: (g[x] + manhattan(x, goal), manhattan(x, goal), cname(x)))
        openl.discard(n)
        closed.add(n)
        out.append(n)
        if n == goal:
            break
        for v in neigh(rows, n):
            if v in closed:
                continue
            alt = g[n] + cost(rows, v)
            if alt < g.get(v, 10 ** 9):
                g[v] = alt
                parent[v] = n
                openl.add(v)
    return dict(order=out, path=path_from(parent, goal), g=g)


def ucs_grid(rows):
    start, goal = parse(rows)
    best = {start: 0}
    pq = [(0, cname(start), start)]
    parent = {}
    done = set()
    while pq:
        d, _, n = heapq.heappop(pq)
        if n in done:
            continue
        done.add(n)
        if n == goal:
            return d, path_from(parent, goal)
        for v in neigh(rows, n):
            alt = d + cost(rows, v)
            if alt < best.get(v, 10 ** 9):
                best[v] = alt
                parent[v] = n
                heapq.heappush(pq, (alt, cname(v), v))
    return None, []


def ucs_graph(edges, start, goal):
    adj = {}
    for a, b, w in edges:
        adj.setdefault(a, []).append((b, w))
        adj.setdefault(b, []).append((a, w))
    best = {start: 0}
    parent = {}
    done = []
    pq = [(0, start)]
    while pq:
        d, n = heapq.heappop(pq)
        if n in done:
            continue
        done.append(n)
        if n == goal:
            break
        for v, w in sorted(adj[n]):
            if d + w < best.get(v, 10 ** 9):
                best[v] = d + w
                parent[v] = n
                heapq.heappush(pq, (d + w, v))
    return dict(order=[(n, best[n]) for n in done], path=path_from(parent, goal), cost=best[goal])


def minimax(t, mx):
    if isinstance(t, (int, float)):
        return t
    vals = [minimax(c, not mx) for c in t]
    return max(vals) if mx else min(vals)


def alphabeta(t, mx, a=float('-inf'), b=float('inf'), log=None):
    """t: tal (löv) eller lista. Returnerar värde; log samlar ('leaf', värde) och ('cut', rest)."""
    if isinstance(t, (int, float)):
        log.append(('leaf', t))
        return t
    v = float('-inf') if mx else float('inf')
    for i, c in enumerate(t):
        x = alphabeta(c, not mx, a, b, log)
        if mx:
            v = max(v, x)
            a = max(a, v)
        else:
            v = min(v, x)
            b = min(b, v)
        if a >= b and i + 1 < len(t):
            log.append(('cut', t[i + 1:], a, b))
            break
    return v


def greedy(rows):
    """Girig bäst först: lägst h, vid lika h rutnamn. Föregångare sätts när rutan upptäcks."""
    start, goal = parse(rows)
    parent, seen, out = {}, {start}, []
    openl = [start]
    while openl:
        openl.sort(key=lambda x: (manhattan(x, goal), cname(x)))
        n = openl.pop(0)
        out.append(n)
        if n == goal:
            break
        for v in neigh(rows, n):
            if v not in seen:
                seen.add(v)
                parent[v] = n
                openl.append(v)
    path = path_from(parent, goal)
    return dict(order=out, path=path, cost=sum(cost(rows, c) for c in path[1:]))


def path_cost(rows, path):
    return sum(cost(rows, c) for c in path[1:])


def astar_graph(edges, h, start, goal):
    """A* i en oriktad viktad graf. Vid lika f: lägst h, sedan namn."""
    adj = {}
    for a, b, w in edges:
        adj.setdefault(a, []).append((b, w))
        adj.setdefault(b, []).append((a, w))
    g, parent, closed, out = {start: 0}, {}, set(), []
    openl = {start}
    while openl:
        n = min(openl, key=lambda x: (g[x] + h[x], h[x], x))
        openl.discard(n)
        closed.add(n)
        out.append((n, g[n], h[n], g[n] + h[n]))
        if n == goal:
            break
        for v, w in adj[n]:
            if v not in closed and g[n] + w < g.get(v, 10 ** 9):
                g[v] = g[n] + w
                parent[v] = n
                openl.add(v)
    return dict(order=out, path=path_from(parent, goal), cost=g[goal], open=sorted(openl), g=g)


def greedy_graph(edges, h, start, goal):
    adj = {}
    for a, b, w in edges:
        adj.setdefault(a, []).append((b, w))
        adj.setdefault(b, []).append((a, w))
    parent, seen, out, openl, g = {}, {start}, [], [start], {start: 0}
    while openl:
        openl.sort(key=lambda x: (h[x], x))
        n = openl.pop(0)
        out.append(n)
        if n == goal:
            break
        for v, w in adj[n]:
            if v not in seen:
                seen.add(v)
                parent[v] = n
                g[v] = g[n] + w
                openl.append(v)
    return dict(order=out, path=path_from(parent, goal), cost=g[goal])
