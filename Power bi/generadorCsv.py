import pandas as pd
import random
from datetime import datetime, timedelta

# Función para generar segmentos (continente-pais-ciudad)
def generar_segmento():
    continentes = {
        "América del Sur": {
            "Chile": ["Santiago", "Valparaíso", "Concepción", "Temuco"],
            "Argentina": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza"],
            "Perú": ["Lima", "Arequipa", "Cusco", "Trujillo"],
            "Colombia": ["Bogotá", "Medellín", "Cali", "Cartagena"],
            "Brasil": ["São Paulo", "Río de Janeiro", "Brasilia", "Curitiba"]
        },
        "América Central": {
            "México": ["Ciudad de México", "Guadalajara", "Monterrey", "Cancún"]
        }
    }
    continente = random.choice(list(continentes.keys()))
    pais = random.choice(list(continentes[continente].keys()))
    ciudad = random.choice(continentes[continente][pais])
    return f"{continente}-{pais}-{ciudad}"

# Función para generar un registro de datos realista
def generar_datos_realistas():
    categorias_actualizadas = {
        "electrónico": ["celulares", "computadores", "televisores", "audífonos", "cámaras", "tablets", "drones"],
        "doméstico": ["lavadoras", "refrigeradores", "aspiradoras", "licuadoras", "ventiladores", "cafeteras"],
        "cocina": ["ollas", "sartenes", "cuchillos", "microondas", "hornos", "batidoras"],
        "baño": ["duchas", "espejos", "toallas", "calefones", "jacuzzis", "dispensadores de jabón"],
        "deporte": ["bicicletas", "trotadoras", "pesas", "pelotas", "colchonetas", "patines"],
        "moda": ["zapatillas", "chaquetas", "poleras", "pantalones", "carteras", "mochilas"],
        "jardinería": ["tijeras podadoras", "rastrillos", "mangueras", "maceteros", "fertilizantes"],
        "automotriz": ["neumáticos", "baterías", "aceites", "filtros", "herramientas de reparación"]
    }
    vendedores = [
        "Falabella", "Ripley", "Paris", "Amazon", "Mercado Libre", "Linio",
        "Walmart", "ElectroChile", "Easy", "Homecenter", "PC Factory", 
        "Hites", "Aliexpress", "eBay", "Sodimac"
    ]
    nombres = ["Juan", "Pedro", "María", "Sofía", "Carlos", "Ana", "José", "Laura", "Luis", "Camila"]
    apellidos = ["Pérez", "González", "Muñoz", "Rojas", "Díaz", "Castro", "Silva", "Fernández", "Ramírez", "Torres"]

    categoria = random.choice(list(categorias_actualizadas.keys()))
    sub_categoria = random.choice(categorias_actualizadas[categoria])
    vendedor = random.choice(vendedores)
    segmento = generar_segmento()
    fecha = datetime.strptime("2017-01-01", "%Y-%m-%d") + timedelta(days=random.randint(0, 2557))
    precio = random.randint(10000, 200000)
    stock_total = random.randint(20, 500)
    stock_vendido = random.randint(0, stock_total)
    numero_modelo = random.randint(10000, 999999)
    
    # Generar columnas adicionales
    nombre_cliente = f"{random.choice(nombres)} {random.choice(apellidos)}"
    edad_cliente = random.randint(18, 70)
    sexo_cliente = random.choice(["Masculino", "Femenino"])
    tipo_de_venta = random.choice(["Física", "E-commerce", "Tienda oficial", "Tiendas online"])

    return {
        "Fecha": fecha.strftime("%d-%m-%Y"),
        "Segmento": segmento,
        "Tienda": vendedor,
        "Categoria Producto": categoria.capitalize(),
        "Sub Categoria Producto": sub_categoria.capitalize(),
        "Nombre Producto": f"{random.choice(['Smart', 'Ecológico', 'Ergonómico', 'Premium'])} {sub_categoria.capitalize()}",
        "Modelo": numero_modelo,
        "Precio": precio,
        "Stock Vendido": stock_vendido,
        "Stock Disponible": stock_total - stock_vendido,
        "Nombre Cliente": nombre_cliente,
        "Edad Cliente": edad_cliente,
        "Sexo Cliente": sexo_cliente,
        "Tipo De Venta": tipo_de_venta,
    }

# Generar los datos
datos_base = [generar_datos_realistas() for _ in range(4000)]
df_base = pd.DataFrame(datos_base)

# Guardar los datos ordenados y sin "ventas_esperadas"
df_base.to_csv("datos_ordenados.csv", index=False)  # Guarda en el mismo directorio del script

