import streamlit as st
import numpy as np
from PIL import Image

from helpers.detector import detect
from helpers.image_utils import fix_orientation
from helpers.pest_info import pest_info

def show():

    # margin kiri kanan
    left, center, right = st.columns([0.12, 0.76, 0.12])


    with center:

        st.markdown("""
        <h1 style="
        color:#0B5ED7;
        font-size:42px;
        font-weight:700;">
        Unggah Gambar
        </h1>
        """, unsafe_allow_html=True)


        uploaded_file = st.file_uploader(
            "Silakan unggah gambar tanaman cabai",
            type=["jpg","jpeg","png"]
        )


    if uploaded_file is None:
        return


    image = Image.open(uploaded_file)

    image = fix_orientation(image)

    results, pred = detect(image)



    # JANGAN taruh di dalam with center
    # buat kolom baru di luar

    left_img, img1, img2, right_img = st.columns(
        [0.12,0.38,0.38,0.12]
    )


    with img1:

        st.subheader("📷 Gambar Asli")

        st.image(
            image,
            width=350
        )


    with img2:

        st.subheader("🎯 Hasil Deteksi")

        st.image(
            np.squeeze(results.render()),
            width=350
        )


    # hasil informasi tetap pakai margin

    left_info, info, right_info = st.columns(
        [0.12,0.76,0.12]
    )


    with info:

        st.write("---")


        if len(pred)==0:

            st.error(
                "Tidak ada hama yang terdeteksi."
            )

            return


        best = pred.sort_values(
            by="confidence",
            ascending=False
        ).iloc[0]


        label = best["name"]

        confidence = best["confidence"]*100

        info_data = pest_info[label]


        st.subheader("📋 Hasil Deteksi")


        st.write(
            f"**Jenis Hama :** {label.title()}"
        )


        st.write(
            f"**Confidence :** {confidence:.2f}%"
        )


        st.subheader("Deskripsi")

        st.info(
            info_data["deskripsi"]
        )


        st.subheader("Gejala")

        for item in info_data["gejala"]:
            st.write("•", item)


        st.subheader("Pengendalian")

        for item in info_data["pengendalian"]:
            st.write("•", item)