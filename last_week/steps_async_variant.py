import asyncio
import time


async def left_foot(step_time, distance=10):
    for dis in range(1, distance):
        print("Prepare for left step")
        # time.sleep(step_time)
        await asyncio.sleep(step_time)
        print("Prepare for left step")


async def right_foot(step_time, distance=10):
    for dis in range(1, distance):
        print("Prepare for right step")
        # time.sleep(step_time)
        await asyncio.sleep(step_time)
        print("Right step")


async def main():
    tasks = [right_foot(2, 10), left_foot(1, 10)]
    await asyncio.wait(tasks)


if __name__ == "__main__":
    print("Lets check async version")
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(time.time() - start_time)
