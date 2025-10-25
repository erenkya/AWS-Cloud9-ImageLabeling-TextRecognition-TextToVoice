import streamlit as st
import boto3
from PIL import Image
import io
import uuid

# --- AWS Clients ---
s3 = boto3.client("s3")
rekognition = boto3.client("rekognition")

# --- Streamlit UI ---
st.set_page_config(page_title="Amazon Rekognition Demo", page_icon="🤖")
st.title("🧠 Image Label Detection with Amazon Rekognition")
st.write("Upload an image and let Rekognition detect objects, scenes, or concepts.")

# --- Upload image ---
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# --- User configuration ---
bucket_name = st.text_input("Enter the name of your S3 bucket where the image will be temporarily uploaded:")

if uploaded_file and bucket_name:
    # Görseli göster
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("🔍 Analyze Image"):
        with st.spinner("Uploading image to S3 and analyzing..."):
            # Benzersiz bir dosya adı oluştur
            file_key = f"uploaded_{uuid.uuid4().hex}.jpg"

            # Görseli byte formatına çevir
            img_bytes = io.BytesIO()
            image.save(img_bytes, format="JPEG")
            img_bytes.seek(0)

            # S3'e yükle
            s3.upload_fileobj(img_bytes, bucket_name, file_key)

            # Rekognition analizi
            response = rekognition.detect_labels(
                Image={"S3Object": {"Bucket": bucket_name, "Name": file_key}},
                MaxLabels=10,
                MinConfidence=70
            )

            # Sonuçları göster
            st.success("✅ Analysis Complete!")
            st.subheader("Detected Labels:")
            for label in response["Labels"]:
                st.write(f"**{label['Name']}** – {label['Confidence']:.2f}% confidence")

            # İstersen geçici dosyayı silebilirsin
            with st.expander("🧹 Delete uploaded image from S3"):
                if st.button("Delete Now"):
                    s3.delete_object(Bucket=bucket_name, Key=file_key)
                    st.info("Image deleted from S3.")
