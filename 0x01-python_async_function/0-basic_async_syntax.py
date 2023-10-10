#!/usr/bin/env python3
import asyncio
import random
'''
an asynchronous coroutine that takes in an integer argument
'''


async def wait_random(max_delay: int = 10):
    '''
    wait_random asynchronous function
    '''
    x = random.uniform(0, max_delay)
    await asyncio.sleep(int(x))
    return x
