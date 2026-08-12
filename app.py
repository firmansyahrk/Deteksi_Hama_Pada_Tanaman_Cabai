import streamlit as st
from streamlit_option_menu import option_menu
import hydralit_components as hc

from views import home
from views import detection
from views import about

st.set_page_config(
    page_title="Deteksi Hama Cabai",
    page_icon="🌶️",
    layout="wide"
)
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
header {visibility:hidden;}
footer {visibility:hidden;}

.stApp{
    background:#F5F9FF;
}

/* rapikan container utama */
.block-container{
    padding-top:0rem !important;
    padding-left:0rem !important;
    padding-right:0rem !important;
}

/* naikkan komponen hydralit */
iframe{
    margin-top:-33px !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.footer{
    position:fixed;
    bottom:0;
    left:0;
    width:100%;
    background:#1565C0;
    color:white;
    text-align:center;
    padding:12px 0;
    font-size:14px;
    z-index:999;
}

</style>
""", unsafe_allow_html=True)

menu_data = [
    {'id':'Home','label':'Home'},
    {'id':'Deteksi','label':'Deteksi Hama'},
    {'id':'Tentang','label':'Tentang'},
]

selected = hc.nav_bar(
    menu_definition=menu_data,
    override_theme={
        'menu_background':'#1565C0',
        'txc_inactive':'white',
        'txc_active':'white',
        'option_active':'#0D47A1'
    },
    sticky_nav=True,
    sticky_mode='pinned'
)

if selected is None:
    selected = "Home"

if selected == "Home":
    home.show()

elif selected == "Deteksi":
    detection.show()

elif selected == "Tentang":
    about.show()

st.markdown("""
<div class="footer">
    © 2026 | Developed by Firmansyah Rizki Kusuma, Dr. Suprianto, S.Si., M.Si., Hamzah Setiawan, S.Kom., M.Kom., Dr. Uce Indahyanti., S.Kom., M.Kom.
</div>
""", unsafe_allow_html=True)
