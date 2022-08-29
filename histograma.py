
# Primeiro importamos as bibliotecas e dependencias que vamos usar.

import cv2 
import pillow
import numpy as np
from matplotlib import pyplot as plt

#importa a imagem 
img = cv2.imread('teste.jpg',0)

#faz o histograma
plt.hist(img.ravel(),256,[0,256]) 


#caucula o tamanho da imagem
wid = img.shape[1] 
hgt = img.shape[0] 
print(str(wid) + "x" + str(hgt))

#cria a janela de exibição da img (imagem dimensionavel )
cv2.namedWindow("Galerya Py", cv2.WND_PROP_ASPECT_RATIO)

#cria a janela de exibição da img
cv2.imshow("Galerya Py", img)
plt.show()
   
    
    

#fecha após sair
cv2.waitKey(0)
cv2.destroyAllWindows(0)