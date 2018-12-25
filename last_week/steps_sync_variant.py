import time


def left_foot(step_time, distance=10):
    for dis in range(1, distance):
        print("Prepare for left step")
        time.sleep(step_time)
        # await asyncio.sleep(step_time)
        print("Left step")


def right_foot(step_time, distance=10):
    for dis in range(1, distance):
        print("Prepare for right step")
        time.sleep(step_time)
        # await asyncio.sleep(step_time)
        print("Right step")


def main():
    tasks = (right_foot, left_foot)
    for task in tasks:
        task(1, 5)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(time.time() - start_time)
