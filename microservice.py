import asyncio
import websockets
import json


async def data(websocket):
    test_data = {"Player": "Bob Ross",
            "Passing Yards": 183,
            "Receptions": 12,
            "Receiving Yards": 87,
            "Rushing Yards": 43,
            "Fumbles": 2,
            "Interceptions": 0
            }

    return_data = json.dumps(test_data)
    await websocket.send(return_data)


async def main():
    async with websockets.serve(data, "127.0.0.1", 65432):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
