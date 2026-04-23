import os
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# 1. Función para extraer texto de un PDF
def extraer_texto(ruta_pdf):
    reader = PdfReader(ruta_pdf)
    texto = ""
    for page in reader.pages:
        texto += page.extract_text()
    return texto

# 2. Tu flujo de trabajo
ruta = "datasheet.pdf" # CAMBIA ESTO por el nombre de un PDF real que tengas

if os.path.exists(ruta):
    print(f"Leyendo {ruta}...")
    contenido_tecnico = extraer_texto(ruta)
    
    # Le pasamos el texto a Gemini con una instrucción de ingeniería
    pregunta = f"Basado en este texto técnico, extrae el Vds máximo y el Rds(on) típico: \n\n {contenido_tecnico}"
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", # El nombre que ya sabemos que funciona
        contents=pregunta
    )
    
    print("\n--- Análisis de Gemini ---")
    print(response.text)
else:
    print(f"No encontré el archivo {ruta}. Pon un PDF en esta carpeta.")
