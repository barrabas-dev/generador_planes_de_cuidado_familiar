import os
import io
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as XLImage
from PIL import Image


def extraer_imagenes_excel(
    ruta_excel,
    nombre_hoja="Hoja1",
    carpeta_fam="assets/imagenes/familiogramas",
    carpeta_eco="assets/imagenes/ecomapas",
    carpeta_ana="assets/imagenes/analisis"
):
    """
    Extrae imágenes de una hoja Excel y las guarda en carpetas específicas
    según su ubicación en las columnas B, C y D.
    """
    # Crear carpetas de destino
    for carpeta in (carpeta_fam, carpeta_eco, carpeta_ana):
        os.makedirs(carpeta, exist_ok=True)

    # Cargar el archivo Excel
    wb = load_workbook(ruta_excel, data_only=True)
    hoja = wb[nombre_hoja]

    # Asociar imágenes a sus coordenadas de celda
    imagenes_por_celda = {}
    for img in hoja._images:  # openpyxl no ofrece acceso público directo
        coord = (img.anchor._from.col + 1, img.anchor._from.row + 1)  # (col, fila)
        imagenes_por_celda[coord] = img

    # Procesar cada fila (desde la fila 2, suponiendo encabezado en la 1)
    for fila in hoja.iter_rows(min_row=2):
        id_hogar = str(fila[0].value).strip()

        # Coordenadas esperadas para cada tipo de imagen
        coord_fam = (2, fila[0].row)  # columna B
        coord_eco = (3, fila[0].row)  # columna C
        coord_ana = (4, fila[0].row)  # columna D

        # Guardar cada imagen si existe en su coordenada correspondiente
        if coord_fam in imagenes_por_celda:
            guardar_imagen(imagenes_por_celda[coord_fam], os.path.join(carpeta_fam, f"{id_hogar}.jpg"))

        if coord_eco in imagenes_por_celda:
            guardar_imagen(imagenes_por_celda[coord_eco], os.path.join(carpeta_eco, f"{id_hogar}.jpg"))

        if coord_ana in imagenes_por_celda:
            guardar_imagen(imagenes_por_celda[coord_ana], os.path.join(carpeta_ana, f"{id_hogar}.jpg"))

    print("✅ Proceso completado con éxito.")


def guardar_imagen(img_obj, ruta_destino):
    """
    Guarda una imagen de Excel en formato JPG.
    """
    # Extraer datos binarios de la imagen
    if hasattr(img_obj, "_data"):
        data = img_obj._data()
    else:
        with open(img_obj.ref, "rb") as f:
            data = f.read()

    # Abrir imagen con PIL
    image = Image.open(io.BytesIO(data))

    # Convertir a RGB si es necesario (para formato JPG)
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Guardar imagen con buena calidad
    image.save(ruta_destino, "JPEG", quality=95)


if __name__ == "__main__":
    # Ejecutar función con ruta y hoja deseada
    extraer_imagenes_excel("assets/imagenes.xlsx", nombre_hoja="Hoja 1")

