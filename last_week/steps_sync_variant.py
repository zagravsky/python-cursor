import time


def left_foot(step_time, distance=10):
    # for dis in range(1, distance):
    print("Prepare for left step")
    time.sleep(step_time)
    print("Left step")


def right_foot(step_time, distance=10):
    # for dis in range(1, distance):
    print("Prepare for right step")
    time.sleep(step_time)
    print("Right step")


def main():
    # tasks = (right_foot, left_foot)
    for step in range(0, 10):
        left_foot(1)
        right_foot(1)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(time.time() - start_time)
