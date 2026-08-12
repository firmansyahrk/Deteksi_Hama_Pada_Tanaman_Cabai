import streamlit as st


def show():

    # Grid untuk memberi jarak kiri-kanan
    left, content, right = st.columns([1, 8, 1])

    with content:

        st.markdown("""
        <h1 style="text-align:center;">
        Tentang Aplikasi
        </h1>
        """, unsafe_allow_html=True)


        st.markdown("""
        ## Sistem Deteksi Hama Tanaman Cabai

        Aplikasi ini merupakan **tugas akhir** yang dikembangkan
        untuk membantu proses identifikasi hama pada tanaman cabai
        menggunakan teknologi **computer vision** dengan algoritma
        **YOLOv5**.

        Sistem ini mampu melakukan deteksi hama berdasarkan gambar
        yang diunggah oleh pengguna, kemudian memberikan informasi
        mengenai jenis hama, tingkat kepercayaan (**confidence score**),
        gejala serangan, serta rekomendasi pengendalian hama.

        ---

        ## Teknologi yang Digunakan

        Aplikasi ini dibangun menggunakan beberapa teknologi berikut:

        - **Python** sebagai bahasa pemrograman utama
        - **Streamlit** sebagai framework pembuatan antarmuka aplikasi
        - **YOLOv5** sebagai model deteksi objek
        - **OpenCV** untuk pengolahan citra digital
        - **PyTorch** sebagai framework deep learning

        ---

        ## Fitur Aplikasi

        Beberapa fitur yang tersedia pada sistem ini antara lain:

        - 📷 Upload gambar tanaman cabai
        - 🔍 Deteksi hama secara otomatis
        - 📊 Menampilkan nilai confidence score hasil deteksi
        - 🐛 Memberikan informasi mengenai jenis hama
        - 🌱 Menampilkan gejala dan rekomendasi pengendalian hama

        """)
