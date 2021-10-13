import asyncio
import time


async def countdown():
    task = asyncio.create_task(fibonacci())
    print(5)
    print(4)
    print("Get ready to see the fibonacci sequence!")
    time.sleep(5)
    await asyncio.sleep(5)
    print("Did you see the fibonacci sequence to the 10th value?")
    print("I hope you're ready for the rest of the countdown...  ")
    print(3)
    await asyncio.sleep(2)
    print(2)
    await asyncio.sleep(2)
    print(1)
    await asyncio.sleep(1)
    print("All done!!")


async def fibonacci(a=0, b=1):
    for i in range(0, 11):
        print(a)
        a, b = b, a + b


asyncio.run(countdown())
