import time
import random
import asyncio



async def marriage(name):
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"{name} married")


def main():
    for child in ["mamad", "gholi", "goli", "alex"]:
        marriage(child)

        
if __name__ == "__main__":
    start_time = time.perf_counter()