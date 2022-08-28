def is_inside(a, b, c, p):
    ax, ay = a
    bx, by = b
    cx, cy = c
    px, py = p
    ab_ap = (bx  - ax) * (py - ay) - (by - ay) * (px - ax)
    bc_bp = (cx  - bx) * (py - by) - (cy - by) * (px - bx)
    ca_cp = (ax  - cx) * (py - cy) - (ay - cy) * (px - cx)
    if (ab_ap > 0 and bc_bp > 0 and ca_cp > 0) or (ab_ap < 0 and bc_bp < 0 and ca_cp < 0):
        return True
    else:
        return False

points = []
for i in range(4):
    x, y = map(int, input().split())
    points.append([x, y])

for i in range(4):
    if is_inside(points[i], points[(i + 1) % 4], points[(i + 2) % 4], points[(i + 3) % 4]):
        print("No")
        exit()
print("Yes")