import asyncio
from bleak import BleakClient

ADDRESS = "2C:CF:67:CC:B5:B4"

UART_TX = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
UART_RX = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"


def notify_handler(sender, data):
    print("RX:", data.decode())


async def main():

    async with BleakClient(ADDRESS) as client:

        print("Connected")

        await client.start_notify(UART_TX, notify_handler)

        while True:
            cmd = input("CMD> ")
            await client.write_gatt_char(UART_RX, cmd.encode())


asyncio.run(main())