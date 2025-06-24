import os
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as XLImage
from PIL import Image
import io

def extraer_imagenes_excel(ruta_excel, nombre_hoja="Hoja1", carpeta_fam="familiogramas", carpeta_eco="ecomapas"):
    # Crear carpetas si no existen
    os.makedirs(carpeta_fam, exist_ok=True)
    os.makedirs(carpeta_eco, exist_ok=True)

    # Cargar el libro
    wb = load_workbook(ruta_excel, data_only=True)
    hoja = wb[nombre_hoja]

    # Mapear imágenes por celda
    imagenes_por_celda = {}
    for img in hoja._images:  # acceso interno a las imágenes
        coord = img.anchor._from.col + 1, img.anchor._from.row + 1  # columna y fila base 1
        imagenes_por_celda[coord] = img

    # Iterar sobre filas
    for fila in hoja.iter_rows(min_row=2):  # Asumimos que hay encabezados
        id_hogar = str(fila[0].value).strip()

        # Coordenadas de cada imagen según las columnas
        coord_fam = (2, fila[0].row)  # columna B
        coord_eco = (3, fila[0].row)  # columna C

        # Guardar familiograma si existe
        if coord_fam in imagenes_por_celda:
            guardar_imagen(imagenes_por_celda[coord_fam], os.path.join(carpeta_fam, f"{id_hogar}.jpg"))

        # Guardar ecomapa si existe
        if coord_eco in imagenes_por_celda:
            guardar_imagen(imagenes_por_celda[coord_eco], os.path.join(carpeta_eco, f"{id_hogar}.jpg"))

    print("✅ Proceso completado con éxito.")

def guardar_imagen(img_obj, ruta_destino):
    """
    Convierte y guarda una imagen de openpyxl a .jpg sin perder calidad.
    """
    if hasattr(img_obj, "_data"):
        data = img_obj._data()
    else:
        with open(img_obj.ref, "rb") as f:
            data = f.read()

    image = Image.open(io.BytesIO(data))

    # Convertir a RGB si es necesario (para JPG)
    if image.mode != "RGB":
        image = image.convert("RGB")

    image.save(ruta_destino, "JPEG", quality=95)



if __name__ == "__main__":
# Código de prueba
 extraer_imagenes_excel("assets/imagenes.xlsx", nombre_hoja="Hoja 1")


