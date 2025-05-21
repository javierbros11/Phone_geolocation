# External Packages
import folium
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from geopy.geocoders import Photon

def obtener_info_telefono(numero_telefono):
    """
    Obtener datos de geolocalización de un número de telefono.

    Args:
        numero_telefono(str): Número de teléfono.
    """

    numero = phonenumbers.parse(numero_telefono) # Requiere incluir el prefijo

    # Obtener la zona horaria

    zona_horaria = timezone.time_zones_for_number(numero)

    # Obtener el pais / región

    pais = geocoder.description_for_number(numero, "es") # Proporcionar el idioma que creemos que esta asociado a ese número.

    # Obtener el operador asociado con el número

    operador = carrier.name_for_number(numero,"es")

    info = {
        "Numero": phonenumbers.format_number(numero, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
        "Pais" : pais,
        "Operador": operador,
        "Zona horaria": zona_horaria
    }

    return info

def pintar_mapa(localizacion, filename="phone_map.html"):
    """
    Construye un mapa la localización de un número de teléfono.

    Args:
        filename(str, default: 'phone_map.html'): Nombre del archivo donde se almacenará el mapa.
    """

    geolocator = Photon(user_agent="geoapiExercise") # Aqui puede ir cualquier nombre como "user_agent"
    location = geolocator.geocode(localizacion)
    mapa = folium.Map([location.latitude,location.longitude], zoom_start=10)
    folium.Marker([location.latitude,location.longitude], popup=localizacion).add_to(mapa)

    # Guardar el mapa como un archivo .html

    mapa.save(filename)
    print(f"Mapa guardado en: {filename}")

# Inicio del programa    
if __name__ == "__main__":
    example = obtener_info_telefono("Numero random")
    pintar_mapa(example["Pais"])