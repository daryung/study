import time
import logging
from test_robot import MirobotInterface

logging.basicConfig(level=logging.INFO)

def main():
    robot = MirobotInterface()  # 반드시 실제 연결된 COM 포트로 바꾸세요
    speed = 2000

    print("Connecting to robot...")
    if not robot.connect():
        print("❌ Failed to connect to robot. Check COM port.")
        return

    print("✅ Connected. Type 'help' for commands.")
    robot.home()
    time.sleep(2)  # 홈 위치 안정화

    while True:
        cmd = input("Command (open/close/move/rel/status/exit/help): ").strip().lower()

        if cmd == "open":
            robot.gripper_open()
        elif cmd == "close":
            robot.gripper_close()
        elif cmd == "move":
            try:
                coords = input("Target X Y Z: ").strip().split()
                x, y, z = map(float, coords)
                robot.move_to(x, y, z, speed)
            except:
                print("❌ Invalid input. Enter three numbers.")
        elif cmd == "rel":
            try:
                deltas = input("dX dY dZ: ").strip().split()
                dx, dy, dz = map(float, deltas)
                robot.move_relative(dx, dy, dz, speed)
            except:
                print("❌ Invalid input. Enter three numbers.")
        elif cmd == "status":
            st = robot.get_status()
            print(f"X={st.x:.2f}, Y={st.y:.2f}, Z={st.z:.2f}")
        elif cmd == "help":
            print("Commands: open, close, move, rel, status, exit")
        elif cmd == "exit":
            break
        else:
            print("Unknown command. Type 'help'.")

    robot.disconnect()
    print("Disconnected.")

if __name__ == "__main__":
    main()