import matplotlib.pyplot as plt

# 객체 3 로봇 좌표
robot_path_obj3 = [
    (-30.00, -91.67), (-38.12, -45.83), (-38.12, -17.50), (-40.62, 5.83),
    (-43.75, 9.17), (-43.75, 43.33), (-41.25, 44.17), (-39.38, 65.00),
    (-33.75, 70.00), (11.88, 73.33), (18.75, 79.17), (25.00, 80.83),
    (25.62, 84.17), (73.12, 84.17), (80.00, 52.50), (83.12, 50.00),
    (83.12, 12.50), (80.62, 11.67), (77.50, -15.83), (75.00, -23.33),
    (73.75, -71.67), (66.25, -75.83), (35.62, -81.67), (23.12, -80.83),
    (15.62, -89.17), (15.62, -91.67), (-29.38, -91.67)
]

# 좌표 분리
x_coords = [p[0] for p in robot_path_obj3]
y_coords = [p[1] for p in robot_path_obj3]

# 점만 찍기
plt.figure(figsize=(8, 6))
plt.scatter(x_coords, y_coords, c='red', s=50, label='Points')

# 좌표 순서대로 선 연결
plt.plot(x_coords, y_coords, 'b-', alpha=0.5, label='Path')

plt.title("Robot Path - Object 3")
plt.xlabel("X (robot coordinate)")
plt.ylabel("Y (robot coordinate)")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()