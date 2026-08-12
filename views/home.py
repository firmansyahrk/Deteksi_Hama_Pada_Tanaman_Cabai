import streamlit as st

def show():
    st.markdown("""
    <style>
    .home-container{
        padding: 40px 20px;
    }
    * Background khusus halaman Home */
    .stApp{
        background-color:#1565C0;
    }
    

    .hero-title{
        color:#0B5ED7;
        font-size:54px;
        font-weight:700;
        line-height:65px;
        margin-bottom:25px;
    }

    .hero-desc{
        font-size:19px;
        line-height:34px;
        text-align:justify;
        color:#333;
        margin-bottom:30px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="home-container">', unsafe_allow_html=True)

    margin1, col1, col2, margin2 = st.columns([0.15, 1.2, 1, 0.15])

    with col1:

        st.markdown("""
        <div style="padding-left:100px;">
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="hero-title">
        Sistem Deteksi Hama<br>
        Tanaman Cabai
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="hero-desc">
        Aplikasi ini digunakan untuk mendeteksi hama pada tanaman cabai
        menggunakan algoritma <b>YOLOv5</b>. Pengguna hanya perlu
        mengunggah gambar tanaman cabai, kemudian sistem akan
        mengidentifikasi jenis hama beserta informasi mengenai
        gejala dan cara pengendaliannya.
        </div>
        """, unsafe_allow_html=True)

        

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div style="padding-right:100px;">
        """, unsafe_allow_html=True)

        st.image(
            "assets/img/hero.jpeg",
            use_column_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)