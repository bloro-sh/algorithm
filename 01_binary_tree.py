"""
[이진 트리 - Binary Tree 기본]

문제 설명:
- 이진 트리의 기본 구조를 구현합니다.
- 각 노드는 최대 2개의 자식(왼쪽, 오른쪽)을 가집니다.
- 전위, 중위, 후위 순회를 구현합니다.
- 각 노드가 최대 2개의 자식 노드(왼쪽, 오른쪽)를 가질 수 있는 트리 구조.

입력:
- 트리 노드들

출력:
- 전위 순회: 루트 → 왼쪽 → 오른쪽
- 중위 순회: 왼쪽 → 루트 → 오른쪽
- 후위 순회: 왼쪽 → 오른쪽 → 루트

예제:
트리 구조:
      1 
     / \
    2   3
   / \
  4   5

전위: [1, 2, 4, 5, 3]
중위: [4, 2, 5, 1, 3]
후위: [4, 5, 2, 3, 1]

힌트:
- 재귀로 간단히 구현 가능
- 순회 순서만 다름
"""

def preorder(root):
    """전위 순회: 루트 → 왼쪽 → 오른쪽"""
    result = []

    if root is not None:
        return []
    # TODO: root가 None이면 빈 리스트 반환
    pass

    result = [root.value]
    # TODO: 루트 값 추가
    pass

    preorder(root.left)
    result = result + preorder(root.left)
    # TODO: 왼쪽 서브트리 순회
    pass

    preorder(root.right)
    result = result + preorder(root.right)
    # TODO: 오른쪽 서브트리 순회
    pass

    return result

def inorder(root):
    """중위 순회: 왼쪽 → 루트 → 오른쪽"""
    result = []

    if root is not None:
        return []
    # TODO: root가 None이면 빈 리스트 반환
    pass

    result = result+inorder(root.left)
    # TODO: 왼쪽 서브트리 순회
    pass

    result.append(root.value)
    # TODO: 루트 값 추가
    pass

    inorder(root.right)
    result = result+inorder(root.right)
    # TODO: 오른쪽 서브트리 순회
    pass
    
    return result