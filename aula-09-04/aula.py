import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


st.title('Aula do dia 16/04')

image = Image.open('peppers.png')

imagem_color_arr = np.array(image)

img_gray = np.mean(imagem_color_arr, axis=2)

st.text(img_gray.shape)

# limiar = st.slider('Limiar?', 0, 255, 25)

# st.text(limiar)

img_gray = np.mean(imagem_color_arr, axis=2)

def qtdeCores(n):
    aux = 255 / n
    x = aux
    y = 0

    for i in range(n):
        if i == 0:
            img_gray[img_gray < x] = 0
            y = x
            x += aux
        elif i == (n - 1):
            img_gray[img_gray > y]  = y
        else:
            img_gray[(y < img_gray) & (img_gray < x)]  = y
            y = x
            x += aux

num_color = st.selectbox("Quantas cores?", \
    (2, 4, 8, 16, 32, 64, 128))

# st.text(num_color)
# img_gray[img_gray != limiar] = 255
if num_color == 2:
    img_gray[img_gray < 127]  = 0
    img_gray[img_gray >= 127]  = 255
elif num_color == 4:
    qtdeCores(4)
elif num_color == 8:
    qtdeCores(8)
elif num_color == 16:
    qtdeCores(16)
elif num_color == 32:
    qtdeCores(32)
elif num_color == 64:
    qtdeCores(64)
elif num_color == 128:
    qtdeCores(128)

new_image = Image.fromarray(img_gray)

# plt.axis('off')
# plt.imshow(new_image)
# plt.show()
# st.pyplot()

st.image([new_image.convert("L"), image], caption=['Cinza', 'colorida'], width=480,) 
# st.image(image, caption='Colorida', width=320,)