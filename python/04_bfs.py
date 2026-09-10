"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    visited=set([start])#방문 시작점 미리넣기
    queue = deque([start])#대기열 큐 생성
    order = [] #방문 순서 리스트

    while queue:
        current = queue.popleft()# 1. 큐꺼내기
        order.append(current) #방문순서 리스트에 추가

        for i in graph[current]:#연결정점 확인
            if i not in visited:#안가본곳이면
                visited.add(i)#방문처리
                queue.append(i)#큐에추가


    # TODO: 큐 생성 및 시작 정점 추가
    # TODO: 큐가 빌 때까지 반복
    return order