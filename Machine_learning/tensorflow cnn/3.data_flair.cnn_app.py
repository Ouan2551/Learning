import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# โหลดโมเดล
model = tf.keras.models.load_model("dog_vs_cat_model.h5")

st.title("🐶🐱 Dog vs Cat Classifier")
st.write("อัปโหลดรูปภาพ แล้วให้ AI บอกว่าเป็น หมา หรือ แมว")

uploaded_file = st.file_uploader("เลือกรูปภาพ", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).resize((128, 128))
    st.image(image, caption="ภาพที่คุณอัปโหลด", use_column_width=True)

    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        st.success("นี่คือ 🐶 หมา!")
    else:
        st.success("นี่คือ 🐱 แมว!")