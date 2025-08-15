import asyncio
from bleak import BleakScanner

async def main():
    print("Scanning for 20 seconds to find scale.")
    devices = await BleakScanner.discover(timeout=20)
    for d in devices:
        print(f"{d.name or '(no name)'}  {d.address}")

asyncio.run(main())
