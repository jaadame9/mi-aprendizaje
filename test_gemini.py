import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

print("--- Escaneando Bus de Modelos ---")
try:
    # 1. Listar modelos disponibles para tu API Key
    model_list = list(client.models.list())
    
    if not model_list:
        print("No se encontraron modelos. Revisa si tu API Key está activa.")
    else:
        # 2. Buscar el nombre real de cualquier modelo 'flash'
        flash_model = next((m.name for m in model_list if 'flash' in m.name), model_list[0].name)
        print(f"Modelo detectado en tu cuenta: {flash_model}")

        # 3. Probar comunicación
        print(f"\n--- Intentando handshake con {flash_model} ---")
        response = client.models.generate_content(
            model=flash_model,
            contents="¿Qué es más crítico en un MOSFET: Rds(on) o Qg?"
        )
        print("\n¡ÉXITO! Respuesta de Gemini:")
        print(response.text)

except Exception as e:
    print(f"\nError de sistema: {e}")
