# ==============================================================================
# 0. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import cv2  # Importa OpenCV para procesamiento de imágenes.
import numpy as np  # Importa NumPy para manejar matrices.
import sys  # Permite detener el programa si ocurre un error.
import win32gui
import win32con
import win32api

print("-+-+-+-+- Santiago Pacheco NC 0113 -+-+-+-+")

def mostrar_ventana(titulo, imagen):
    cv2.imshow(titulo, imagen)
    cv2.setWindowProperty(titulo, cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ==============================================================================
# 1. LECTURA DE LA IMAGEN DESDE LA CARPETA
# ==============================================================================
print("\n1. LECTURA DE IMÁGENES")

nombre_ventana = "Santiago Pacheco NC 0113"
img = cv2.imread('img-0113.webp')

if img is None:
    print("Error: No se pudo leer 'img-0113.webp'. Revisa el nombre y ubicación.")
    sys.exit()
else:
    print("Imagen cargada exitosamente.")

# ==============================================================================
# 2. PROPIEDADES DE LA IMAGEN
# ==============================================================================
print("\n2. PROPIEDADES DE LA IMAGEN")

altura, anchura, canales = img.shape

print(f"Dimensiones de la imagen: {anchura}x{altura} píxeles")
print(f"Número de canales de color: {canales}")
print(f"Tipo de datos de la imagen: {img.dtype}")
print(f"Total de datos/píxeles: {img.size}")

# ==============================================================================
# 3. VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n3. MOSTRANDO IMAGEN ORIGINAL")
print("Presiona cualquier tecla sobre la ventana para continuar...")

mostrar_ventana(f'{nombre_ventana} - 1. Imagen Original', img)

# ==============================================================================
# 4. ACCESO Y MODIFICACIÓN DE PÍXELES INDIVIDUALES
# ==============================================================================
print("\n4. ACCEDIENDO Y MODIFICANDO PÍXELES")

pixel_img = img.copy()

# Ajusta coordenadas automáticamente si la imagen es pequeña
y = min(100, altura - 1)
x = min(150, anchura - 1)

pixel = pixel_img[y, x]

print(f"Valor del píxel en ({x}, {y}): {pixel} (Formato BGR)")

pixel_img[y, x] = [0, 0, 255]  # Cambia el píxel a rojo puro
cv2.circle(pixel_img, (x, y), 20, (255, 0, 0), 3)  # Dibuja un círculo azul

mostrar_ventana(f'{nombre_ventana} - 2. Pixel Modificado (Rojo)', pixel_img)

# ==============================================================================
# 5. REGIÓN DE INTERÉS (ROI)
# ==============================================================================
print("\n5. REGIÓN DE INTERÉS (ROI)")

roi_img = img.copy()

y1, y2 = min(50, altura // 4), min(200, altura)
x1, x2 = min(100, anchura // 4), min(300, anchura)

roi = roi_img[y1:y2, x1:x2]

cv2.rectangle(roi_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

mostrar_ventana(f'{nombre_ventana} - 3. Imagen con ROI marcado', roi_img)
mostrar_ventana(f'{nombre_ventana} - 4. ROI Extraida (Recorte)', roi)

# ==============================================================================
# 6. SEPARACIÓN Y FUSIÓN DE CANALES DE COLOR (BGR)
# ==============================================================================
print("\n6. SEPARANDO Y FUSIONANDO CANALES")

b, g, r = cv2.split(img)

mostrar_ventana(f'{nombre_ventana} - 5. Canal Azul (Escala de grises)', b)
mostrar_ventana(f'{nombre_ventana} - 6. Canal Verde (Escala de grises)', g)
mostrar_ventana(f'{nombre_ventana} - 7. Canal Rojo (Escala de grises)', r)

ceros = np.zeros_like(b)

blue_img = cv2.merge([b, ceros, ceros])
green_img = cv2.merge([ceros, g, ceros])
red_img = cv2.merge([ceros, ceros, r])

mostrar_ventana(f'{nombre_ventana} - 8. Canal Azul (Coloreado)', blue_img)
mostrar_ventana(f'{nombre_ventana} - 9. Canal Verde (Coloreado)', green_img)
mostrar_ventana(f'{nombre_ventana} - 10. Canal Rojo (Coloreado)', red_img)

# ==============================================================================
# 7. REDIMENSIONAMIENTO DE IMÁGENES
# ==============================================================================
print("\n7. REDIMENSIONANDO IMÁGENES")

resized_img = cv2.resize(img, (400, 300))
mostrar_ventana(f'{nombre_ventana} - 11. Redimensionada a 400x300', resized_img)

half_size = cv2.resize(img, None, fx=0.5, fy=0.5)
mostrar_ventana(f'{nombre_ventana} - 12. Mitad de tamaño (0.5x)', half_size)

double_size = cv2.resize(img, None, fx=1.5, fy=1.5)
mostrar_ventana(f'{nombre_ventana} - 13. Ampliada (1.5x)', double_size)

# ==============================================================================
# 8. ROTACIÓN DE IMÁGENES
# ==============================================================================
print("\n8. ROTANDO IMÁGENES")

altura, anchura = img.shape[:2]

matriz_de_rotacion = cv2.getRotationMatrix2D(
    (anchura / 2, altura / 2), 45, 1
)

rotated_img = cv2.warpAffine(
    img, matriz_de_rotacion, (anchura, altura)
)

mostrar_ventana(f'{nombre_ventana} - 14. Imagen Rotada (45 grados)', rotated_img)

# ==============================================================================
# 9. VOLTEO / ESPEJO DE IMÁGENES (FLIPPING)
# ==============================================================================
print("\n9. VOLTEANDO IMÁGENES")

horizontal_flip = cv2.flip(img, 1)
mostrar_ventana(f'{nombre_ventana} - 15. Volteo Horizontal (Espejo)', horizontal_flip)

vertical_flip = cv2.flip(img, 0)
mostrar_ventana(f'{nombre_ventana} - 16. Volteo Vertical (De cabeza)', vertical_flip)

ambos_flip = cv2.flip(img, -1)
mostrar_ventana(f'{nombre_ventana} - 17. Volteo en Ambos Ejes', ambos_flip)

# ==============================================================================
# 10. GUARDADO DE RESULTADOS Y LIMPIEZA
# ==============================================================================
print("\n10. GUARDANDO IMAGEN RESULTANTE")

resultado = cv2.imwrite('img-0113-rotado.webp', rotated_img)

if resultado:
    print("Imagen rotada guardada exitosamente como 'img-0113-rotado.webp'")
else:
    print("Error: No se pudo guardar la imagen rotada.")

cv2.destroyAllWindows()

print("\n¡Todas las operaciones se completaron con éxito! - Santiago Pacheco NC 0113")