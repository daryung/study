import tkinter as tk

AREA_X = 18      # 가로 칸
AREA_Y = 11     # 세로 칸
SCALE = 40       # 1칸 = 10mm

WIDTH = AREA_X * SCALE
HEIGHT = AREA_Y * SCALE


# ==========================
# 왼쪽 아래 원점
# ==========================
ORIGIN_X = 293.50
ORIGIN_Y = -112.60


points = []
visited = set()


window = tk.Tk()
window.title("Mirobot Drawing Program")
window.geometry(f"{WIDTH+80}x{HEIGHT+120}")


canvas = tk.Canvas(
    window,
    width=WIDTH+40,
    height=HEIGHT+40,
    bg="white"
)

canvas.pack()


# ==========================
# 격자 + cm 표시
# ==========================

for x in range(AREA_X + 1):

    px = x * SCALE

    canvas.create_line(
        px, 0,
        px, HEIGHT,
        fill="gray"
    )

    if x < AREA_X:
        canvas.create_text(
            px + SCALE/2,
            HEIGHT + 15,
            text=f"{x}cm",
            font=("Arial", 8)
        )


for y in range(AREA_Y + 1):

    py = y * SCALE

    canvas.create_line(
        0, py,
        WIDTH, py,
        fill="gray"
    )

    if y < AREA_Y:
        canvas.create_text(
            WIDTH + 20,
            py + SCALE/2,
            text=f"{AREA_Y-y}cm",
            font=("Arial", 8)
        )


# ==========================
# 펜 그리기
# ==========================

def draw(event):

    grid_x = int(event.x // SCALE)
    grid_y = int(event.y // SCALE)


    if grid_x < 0 or grid_x >= AREA_X:
        return

    if grid_y < 0 or grid_y >= AREA_Y:
        return


    if (grid_x, grid_y) in visited:
        return


    visited.add((grid_x, grid_y))


    # ==========================
    # 좌표 변환
    #
    # 왼쪽 아래 칸 = 원점
    #
    # 오른쪽 이동:
    # 두번째 값 증가
    #
    # 위쪽 이동:
    # 첫번째 값 감소
    # ==========================

    move_up = AREA_Y - 1 - grid_y

    robot_x = ORIGIN_X - (move_up * 10)

    robot_y = ORIGIN_Y + (grid_x * 10)


    coordinate = (
        round(robot_x, 2),
        round(robot_y, 2),
        120.70,
        0.00,
        0.00,
        0.00
    )


    points.append(coordinate)


    # 화면 표시

    x1 = grid_x * SCALE
    y1 = grid_y * SCALE

    canvas.create_rectangle(
        x1,
        y1,
        x1 + SCALE,
        y1 + SCALE,
        fill="black",
        outline=""
    )


canvas.bind("<Button-1>", draw)
canvas.bind("<B1-Motion>", draw)



# ==========================
# 출력
# ==========================

def run():

    print("======================")
    print("Robot Coordinate")
    print("======================")


    for p in points:

        print(
            f"({p[0]:.2f},"
            f"{p[1]:.2f},"
            f"{p[2]:.2f},"
            f"{p[3]:.2f},"
            f"{p[4]:.2f},"
            f"{p[5]:.2f})"
        )


    print("======================")


button = tk.Button(
    window,
    text="RUN",
    command=run,
    width=15,
    height=2
)

button.pack(pady=10)


window.mainloop()