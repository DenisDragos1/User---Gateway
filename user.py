import asyncio
import websockets
import json
import random

async def request_sensor_data():
    """Trimite cereri către gateway pentru diferiți senzori."""
    async with websockets.connect("ws://localhost:8765") as websocket:
        sensor_ids = [121, 141, 111]  # Id-urile senzorilor interesați
        for sensor_id in sensor_ids:
            request = {"id_senzor": sensor_id}
            await websocket.send(json.dumps(request))
            print(f"Cerere trimisă pentru senzorul {sensor_id}.")
            
            # Așteaptă și afișează răspunsurile de la gateway
            for _ in range(5):  # Se așteaptă 5 mesaje per senzor
                response = await websocket.recv()
                data = json.loads(response)
                print(f"Date primite: {data}")
            
            await asyncio.sleep(random.uniform(1, 5))  # Interval între cereri

if __name__ == "__main__":
    asyncio.run(request_sensor_data())
