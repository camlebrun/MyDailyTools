import qrcode
from io import BytesIO
from PIL import Image
import streamlit as st
st.set_page_config(page_title="QR Code", page_icon=":guardsman:", layout="wide")
st.title("QR Code")
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def main():
    url = st.text_input("Entrez l'URL")
    if url:
        img = generate_qr_code(url)
        img_buffer = BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        st.image(img_buffer, width=200)
        

if __name__ == '__main__':
    main()
