import json
from config import *
import asyncio
import aio_pika
from pika.adapters.asyncio_connection import AsyncioConnection
import aio_pika
import logging
from aio_pika import connect
from aio_pika.abc import AbstractIncomingMessage
from typing import Any
import ast
import time
from main import Supper

data_info_in_json = []

async def on_message(message: AbstractIncomingMessage) -> None:

        connection = await aio_pika.connect_robust(
            f'amqp://{mqlogin}:{mqpassword}@{mqhost}/',
        )
        print(" [x] Received message %r" % message)
        print("Before sleep!")
        await asyncio.sleep(2)  # Represents async I/O operations
        print("After sleep!")
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)
        # Declaring queue
        queue = await channel.declare_queue("")
        msg = await queue.get()
        body_str = msg.body.decode('UTF-8')
        # print(body_str)
        r = ast.literal_eval(body_str)
        # data_info_in_json.append(r)
        # print(data_info_in_json)
        #print(r)
        class_main = Supper()
        for main_urls_one in r['urls']:
            all_my_urls = await class_main.start_parser(urlss=main_urls_one)
            print(all_my_urls)

        # Добавить эту информацию после прохождения каждого url
        info = [r['id'], r['site'], r['task_id'], r['main']['region'], r['main']['city']]


async def main()-> None:
    connection = await aio_pika.connect_robust(
        f'amqp://{mqlogin}:{mqpassword}@{mqhost}/',
    )
    async with connection:
        # Creating a channel
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)
        # Declaring queue
        queue = await channel.declare_queue("")

        await queue.consume(on_message, no_ack=False)

        print(" [*] Waiting for messages. To exit press CTRL+C")
        await asyncio.Future()


asyncio.run(main())



