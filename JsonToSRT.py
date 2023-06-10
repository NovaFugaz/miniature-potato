import json

def convert_to_srt(json_data):
    """
    La función toma el contenido del JSON que le usuarie da y hace un for para cada línea y le da formato, almacenando en memoria el contenido en srt_content.
    Function takes JSON's content given by user and uses a for loop and formats it into "srt_content".
    """
    lines = json_data["lyrics"]["lines"]
    srt_content = ""

    for i in range(len(lines)):
        line = lines[i]
        start_time = int(line["startTimeMs"]) // 1000
        if i+1 < len(lines):
            next_line = lines[i+1]
            end_time = int(next_line["startTimeMs"]) // 1000
        else:
            # Última línea, establecer end_time en 0
            end_time = 0
        text = line["words"]

        srt_content += f"{i+1}\n"
        srt_content += f"{format_time(start_time)} --> {format_time(end_time)}\n"
        srt_content += f"{text}\n"
        srt_content += "\n"

    return srt_content


def format_time(milliseconds):
    """
    La función convierte los milisegundos en horas, minutos, segundos y milisegundos según corresponde y devuelve siguiendo el formato hh:mm:ss:msms.
    Self-explanatory. Converts time.
    """
    hours = milliseconds // 3600
    minutes = (milliseconds // 60) % 60
    seconds = milliseconds % 60
    milliseconds = (milliseconds % 1000) // 10

    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:02d}"

# Solicitar al usuario ingresar el JSON //  Asks user for JSON content
json_data = input("Ingrese el contenido JSON: ")

# Parsear el JSON ingresado // Parses given JSON
try:
    json_data = json.loads(json_data)
except ValueError:
    print("Error: El JSON ingresado no es válido.")
    exit()

# Solicitar al usuario ingresar el nombre del archivo SRT (sin la extensión) // Asks user for a filename, without extension.
srt_filename = input("Ingrese el nombre del archivo SRT para guardar (sin la extensión .srt): ")
srt_filename += ".srt"  # Agregar la extensión .srt // Adds .srt extension.

# Convierte a formato SRT // Converts data to SRT
srt_data = convert_to_srt(json_data)

# Guarda el archivo SRT // Saves SRT
with open(srt_filename, "w", encoding='utf-8') as file:
    file.write(srt_data)

# Prints a confirmation message. 
print("El archivo SRT ha sido generado exitosamente.")