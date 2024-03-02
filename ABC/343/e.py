v = list(map(int, input().split()))
if v[0] + v[1] * 2 + v[2] * 3 != 7 ** 3 * 3:
    print("No")
    exit()

def overlap_volume_two(cube1, cube2):
    # 立方体の各辺の長さ
    side_length = 7
    
    # 立方体1の座標
    x1, y1, z1 = cube1
    # 立方体2の座標
    x2, y2, z2 = cube2
    
    # 重なっている立方体の各辺の長さを計算
    dx = min(x1 + side_length, x2 + side_length) - max(x1, x2)
    dy = min(y1 + side_length, y2 + side_length) - max(y1, y2)
    dz = min(z1 + side_length, z2 + side_length) - max(z1, z2)
    
    # 体積が正の場合、立方体が重なっている
    if dx > 0 and dy > 0 and dz > 0:
        return dx * dy * dz
    else:
        return 0

def overlap_volume_three(cube1, cube2, cube3):
    # 立方体の各辺の長さ
    side_length = 7
    
    # 立方体1の座標
    x1, y1, z1 = cube1
    # 立方体2の座標
    x2, y2, z2 = cube2
    # 立方体3の座標
    x3, y3, z3 = cube3
    
    # 3つの立方体が重なっている場合
    dx = min(x1 + side_length, x2 + side_length, x3 + side_length) - max(x1, x2, x3)
    dy = min(y1 + side_length, y2 + side_length, y3 + side_length) - max(y1, y2, y3)
    dz = min(z1 + side_length, z2 + side_length, z3 + side_length) - max(z1, z2, z3)
    
    # 体積が正の場合、3つの立方体がちょうど重なっている
    if dx > 0 and dy > 0 and dz > 0:
        return dx * dy * dz
    else:
        return 0


x0, y0, z0 = 0, 0, 0
for x1 in range(8):
    for y1 in range(8):
        for z1 in range(8):
            for x2 in range(-7, 8, 1):
                for y2 in range(-7, 8, 1):
                    for z2 in range(-7, 8, 1):
                        cube_zero = [x0, y0, z0]
                        cube_one = [x1, y1, z1]
                        cube_two = [x2, y2, z2]
                        # 3つの重複部分を求める
                        if overlap_volume_three(cube_zero, cube_one, cube_two) != v[-1]:
                            continue
                        stack = 0
                        # 2つの重複部分を求める①②
                        stack += overlap_volume_two(cube_zero, cube_one)
                        # 2つの重複部分を求める②③
                        stack += overlap_volume_two(cube_one, cube_two)
                        # 2つの重複部分を求める③①
                        stack += overlap_volume_two(cube_two, cube_zero)
                        stack -= v[-1] * 3
                        if stack == v[1]:
                            print("Yes")
                            print(x0, y0, z0, x1, y1, z1, x2, y2, z2)
                            exit()
print("No")
