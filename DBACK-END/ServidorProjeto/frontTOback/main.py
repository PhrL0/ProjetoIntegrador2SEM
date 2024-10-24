import asyncio
import websockets
import consultaBanco

async def echo(websocket, path):
    await websocket.send(consultaBanco.fazConsulta())
    async for message in websocket:
        print(f"Recebido: {message}")
        await websocket.send("oi")

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
