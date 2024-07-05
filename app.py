from io import BytesIO
import streamlit as st
import qrcode

st.title("デモアプリ")
st.write("""# QRコード生成アプリ
- ライブラリのインストール
- 入力エリアを作る
- QRコード変換プログラムを書く
- QRコードを表示する
""")

text = st.text_input("入力エリア")

if text:
    with BytesIO() as out:
        img = qrcode.make(text)
        img.save(out)
        st.image(out)
