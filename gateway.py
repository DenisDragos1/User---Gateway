import asyncio
import websockets
import random
import json
from datetime import datetime

async def simulate_sensor_data(websocket, sensor_id):
    """Simulează trimiterea datelor pentru un senzor."""
    for _ in range(5):  # Trimite 5 mesaje pentru fiecare cerere
        data = {
            "id_senzor": sensor_id,
            "temperatura": round(random.uniform(15, 30), 2),  # Temperatură aleatoare
            "timp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        await websocket.send(json.dumps(data))
        await asyncio.sleep(random.uniform(1, 3))  # Interval aleatoriu între mesaje

async def handle_connection(websocket):
    """Gestionează conexiunile primite."""
    async for message in websocket:
        request = json.loads(message)
        sensor_id = request.get("id_senzor")
        print(f"Solicitare primită pentru senzorul {sensor_id}.")
        await simulate_sensor_data(websocket, sensor_id)

async def main():
    async with websockets.serve(handle_connection, "localhost", 8765):
        print("Gateway-ul este pornit pe ws://localhost:8765")
        await asyncio.Future()  # Rulează permanent

if __name__ == "__main__":
    asyncio.run(main())
