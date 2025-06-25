print("🚀 Archivo app.py se está ejecutando")

from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv
import folium

load_dotenv() 
token = os.getenv('denue_token')

app = Flask(__name__)


@app.route('/')
def home():
    print("Estoy entrando a formulario")
    return render_template('formulario.html')

@app.route('/buscar-coordenadas', methods=['GET'])
def buscar_por_coordenadas():
    print("📌 Entrando a la función /buscar-coordenadas")

    condicion = request.args.get('condicion', 'todos')
    latitud = request.args.get('latitud')
    longitud = request.args.get('longitud')
    distancia = request.args.get('distancia', '1000')  
    print("📌 Parámetros recibidos:", latitud, longitud, distancia, condicion)
    
    #return f"condicion:{condicion} lat:{latitud} lon:{longitud} distancia:{distancia} jiji"
    if not all([latitud, longitud, token]):
        return 'Faltan parámetros latitud, longitud o token', 400 #Bad Request
    
    print("🔐 Token usado:", token)

    try:
        lat_float = float(latitud)
        lon_float = float(longitud)
    except ValueError:
        return jsonify({'error': 'Latitud y longitud deben ser números válidos'}), 400

    url = f"https://www.inegi.org.mx/app/api/denue/v1/consulta/Buscar/{condicion}/{latitud},{longitud}/{distancia}/{token}"

    print("🔗 URL generada:", url)
    

    try:
        r = requests.get(url)
        r.raise_for_status()  # Lanza excepción si hay error HTTP
        data = r.json()
        print("📦 JSON recibido:")
        print("Tipo:", type(data))
        print("Contenido:", data)
            
        # Verificar si la respuesta contiene datos
        if not data or 'message' in data:
            return jsonify({'error': 'No se encontraron establecimientos'}), 404
        
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error en la consulta a la API: {str(e)}'}), 500
    except ValueError as e:
        return jsonify({'error': 'Error al procesar la respuesta de la API'}), 500


    #Crear mapa
    mapa = folium.Map(location=[lat_float, lon_float], zoom_start=15)  

     # Agregar marcador del punto de búsqueda
    folium.Marker(
        [lat_float, lon_float],
        popup="Punto de búsqueda",
        icon=folium.Icon(color='red', icon='star') #info-sign
    ).add_to(mapa) 

    establecimientos_procesados = 0

    if isinstance(data, list):
        establecimientos = data
    else:
        # Si la respuesta tiene estructura diferente, ajustar según la API
        establecimientos = data.get('establecimientos', [])
    
    for establecimiento in establecimientos:
        try:
            nombre = establecimiento.get('Nombre', 'Sin nombre')
            clase_actividad = establecimiento.get('Clase_actividad', 'Sin clasificar')
            calle = establecimiento.get('Calle', '')
            numero_ext = establecimiento.get("Num_Exterior", "")
            colonia = establecimiento.get("Colonia", "")
            telefono = establecimiento.get("Telefono", "No disponible")
            lat = establecimiento.get("Latitud")
            lon = establecimiento.get("Longitud")
            
            # Validar que las coordenadas existan y sean válidas
            if lat is None or lon is None:
                continue
                
            try:
                lat = float(lat)
                lon = float(lon)
            except (ValueError, TypeError):
                continue
            
            # Crear popup con información del establecimiento
            direccion = f"{calle} {numero_ext}, {colonia}".strip(', ')
            popup_text = f"""
            <b>{nombre}</b><br>
            <b>Actividad:</b> {clase_actividad}<br>
            <b>📍 Dirección:</b> {direccion}<br>
            <b>📞 Teléfono:</b> {telefono}
            """
            
            # Agregar marcador al mapa
            folium.Marker(
                [lat, lon],
                popup=folium.Popup(popup_text, max_width=300),
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(mapa)
            
            establecimientos_procesados += 1
            print(f"Procesado: {nombre} - {clase_actividad} - {direccion} - Tel: {telefono} - Coords: {lat},{lon}")
            
        except Exception as e:
            print(f"Error procesando establecimiento: {e}")
            continue
    
    print(f"Total de establecimientos procesados: {establecimientos_procesados}")
    
    # Guardar mapa como HTML
    mapa_html = mapa._repr_html_()
    
    return render_template('resultado.html', 
                         mapa_html=mapa_html, 
                         total_encontrados=len(data),
                         total_procesados=establecimientos_procesados,
                         condicion=condicion,
                         latitud=latitud,
                         longitud=longitud,
                         distancia=distancia)

if __name__ == '__main__':
     print("Entrando a flask ❤️")
     print("Holaaa")
     app.run(
        host='0.0.0.0',  
        port=5000,
        debug=True,      # Ver logs de depuración  
        threaded=True,   # Manejar múltiples requests
        use_reloader=False
    )