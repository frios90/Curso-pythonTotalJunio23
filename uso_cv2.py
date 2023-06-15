import cv2

##Ver una imagen y guardarla en escala de grices
# imagen = cv2.imread('pikachu.png')
# imagen = cv2.imread('pikachu.png',0) #en escala de grices
# cv2.imwrite("pikachugris.jpg", imagen) #guardo la imagen con otro nombre y los posibles cambios que necesite
# cv2.imshow("pikachu", imagen)
# cv2.waitKey(3000)
# cv2.destroyAllWindows()

#Captura imagen desde la camara web
# captura = cv2.VideoCapture(0)
# salida = cv2.VideoWriter("videoSalida.avi", cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))

# while captura.isOpened():
#     ret, imagen = captura.read()
#     if ret:
#         cv2.imshow("video", imagen)
#         salida.write(imagen)
#         if cv2.waitKey(1) & 0xFF == ord('s'):
#             break

# captura.release()
# salida.release()
# cv2.destroyAllWindows()

##Para ver el video grabado
##el video se procesará en velocidad aumentada por defecto
captura = cv2.VideoCapture('videoSalida.avi')

while captura.isOpened():
    ret, imagen = captura.read()
    if ret:
        cv2.imshow("video", imagen)
        if cv2.waitKey(39) & 0xFF == ord('s'): ##ese 39 indica la velocidad de reproducción... mas alto/mas lento
            break

    else:
        break

captura.release()
cv2.destroyAllWindows()