import sys
sys.setrecursionlimit(10 ** 6)

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        # 頂点の数
        self.V = vertices
        # 隣接リストの辞書
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        # 頂点uからvへのエッジを追加
        self.graph[u].append(v)
    
    def _dfs(self, v, visited, stack):
        # 現在の頂点を訪問済みにする
        visited[v] = True
        # この頂点に隣接するすべての頂点を訪問
        for i in self.graph[v]:
            if not visited[i]:
                self._dfs(i, visited, stack)
        # 完了したらスタックに頂点を積む
        stack.append(v)
    
    def _fill_order(self):
        # すべての頂点を未訪問にする
        visited = [False] * self.V
        stack = []
        # 各頂点でDFSを実行
        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, stack)
        return stack
    
    def _transpose(self):
        # グラフの逆を作成
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g
    
    def _dfs_util(self, v, visited, component):
        # 現在の頂点を訪問済みにする
        visited[v] = True
        # 強連結成分のリストにこの頂点を追加
        component.append(v)
        # この頂点に隣接するすべての頂点を訪問
        for i in self.graph[v]:
            if not visited[i]:
                self._dfs_util(i, visited, component)
    
    def get_sccs(self):
        # ステップ1: グラフのすべての頂点をDFSし、終了時にスタックに積む
        stack = self._fill_order()
        # ステップ2: 逆グラフを作成
        gr = self._transpose()
        # ステップ3: すべての頂点を未訪問にする
        visited = [False] * self.V
        # 強連結成分を格納するリスト
        sccs = []
        # スタックから1つずつ頂点を取り出し、逆グラフでDFSを行う
        while stack:
            i = stack.pop()
            if not visited[i]:
                # 強連結成分のリストを初期化
                component = []
                gr._dfs_util(i, visited, component)
                # 強連結成分をsccsリストに追加
                sccs.append(component)
        return sccs

n = int(input())
a = list(map(int, input().split()))
g = Graph(n)
rg = Graph(n)
for i in range(n):
    g.add_edge(i, a[i] - 1)
    rg.add_edge(a[i] - 1, i)

# 強連結成分ごとにindex化
sccs_set_list = []
node2sccs_idx = dict()
for i, sccs in enumerate(g.get_sccs()):
    sccs_set_list.append(set(sccs))
    for node in sccs:
        node2sccs_idx[node] = i

# 強連結成分ごとにトポロジカルソート
from_sccs_count = [0 for _ in range(len(sccs_set_list))]
for i in range(len(sccs_set_list)):
    sccs_set = sccs_set_list[i]
    for node in sccs_set:
        next_node = a[node] - 1
        if node2sccs_idx[next_node] != i:
            from_sccs_count[i] += 1

from collections import deque
que = deque()
for i in range(len(sccs_set_list)):
    if from_sccs_count[i] == 0:
        que.append(i)

ans = 0
# それぞれの強連結成分ごとに足し算
sccs_values = [0 for _ in range(len(sccs_set_list))]
for i in range(len(sccs_set_list)):
    if len(sccs_set_list[i]) == 1:
        ans += 1
        sccs_values[i] = 1
    else:
        value = len(sccs_set_list[i])
        ans += value
        ans += (value) * (value - 1)
        sccs_values[i] = value

# トポロジカルソートした順に、処理していく
while(que):
    sccs_idx = que.popleft()
    for node in sccs_set_list[sccs_idx]:
        for from_node in rg.graph[node]:
            if node2sccs_idx[from_node] != sccs_idx:
                que.append(node2sccs_idx[from_node])
                ans += sccs_values[node2sccs_idx[from_node]] * sccs_values[sccs_idx]
                sccs_values[node2sccs_idx[from_node]] += sccs_values[sccs_idx]        

print(ans)