# 🧠 Amazon Rekognition + Polly Voice Demo

<img width="1470" height="834" alt="Screenshot 2025-10-25 at 12 40 41" src="https://github.com/user-attachments/assets/3a630584-54df-4937-abbf-689a95a88ee9" />
<img width="1469" height="828" alt="Screenshot 2025-10-25 at 12 45 19" src="https://github.com/user-attachments/assets/1719f2a2-34fe-488a-9b25-87156c422b38" />
<img width="1464" height="828" alt="Screenshot 2025-10-25 at 12 45 42" src="https://github.com/user-attachments/assets/45b4dd62-d582-4cde-a15f-0d4588239523" />
<img width="1468" height="819" alt="Screenshot 2025-10-25 at 12 46 13" src="https://github.com/user-attachments/assets/5770ca3f-138c-4c0e-ad65-88b01165fd81" />



A Streamlit web application that leverages AWS services to analyze images and generate voice descriptions. This application uses Amazon Rekognition for image analysis (label and text detection) and Amazon Polly for text-to-speech conversion.

## Features

- **Image URL Input**: Load images from any publicly accessible URL
- **Label Detection**: Identifies objects, scenes, and concepts in images with confidence scores
- **Text Detection**: Extracts text content from images (OCR)
- **Voice Generation**: Creates audio descriptions of detected content using Amazon Polly
- **Temporary Storage**: Uses S3 for temporary file storage with cleanup options

## Prerequisites

- Python 3.7+
- AWS Account with appropriate credentials configured
- AWS services enabled:
  - Amazon S3
  - Amazon Rekognition
  - Amazon Polly

## Installation

1. **Clone or download the project**

2. **Install required dependencies**:
```bash
pip install streamlit boto3 pillow requests
```

3. **Configure AWS credentials**:

Set up your AWS credentials using one of these methods:

- **AWS CLI configuration**:
```bash
aws configure
```

- **Environment variables**:
```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=your_region
```

- **Cloud9**: If running in AWS Cloud9, IAM role credentials are automatically configured

## Configuration

Update the S3 bucket name in the code:

```python
bucket_name = "cloud-prooject-2"  # Change to your bucket name
```

**Important**: Ensure the S3 bucket exists and your AWS credentials have permissions for:
- `s3:PutObject`
- `s3:GetObject`
- `s3:DeleteObject`
- `rekognition:DetectLabels`
- `rekognition:DetectText`
- `polly:SynthesizeSpeech`

## Usage

1. **Start the application**:
```bash
streamlit run app.py --server.port 8080 --server.address 0.0.0.0
```

2. **Access the web interface**:
   - Local: `http://localhost:8501`
   - Cloud9: Use the preview URL provided

3. **Analyze an image**:
   - Enter a public image URL in the text input
   - Click "🔍 Analyze Image with Rekognition"
   - View detected labels and text in the results
   - Listen to the AI-generated voice description

4. **Clean up**:
   - Click "🧹 Delete temporary image and audio from S3" to remove uploaded files

## How It Works

1. **Image Loading**: Fetches image from provided URL using HTTP requests
2. **S3 Upload**: Temporarily uploads image to S3 bucket for processing
3. **Rekognition Analysis**: 
   - Detects up to 10 labels with minimum 70% confidence
   - Extracts text from the image
4. **Voice Generation**: 
   - Identifies the top label by confidence score
   - Generates speech using Amazon Polly (Joanna voice)
   - Uploads audio to S3 and provides playback link
5. **Cleanup**: Allows deletion of temporary S3 objects

## Project Structure

```
.
├── app.py              # Main Streamlit application
└── README.md           # This file
```

## Sample Workflow

```
Enter Image URL → Load Image → Click Analyze → 
View Labels & Text → Play Audio Description → Delete Temp Files
```

## Troubleshooting

**Image fails to load**:
- Ensure the URL is publicly accessible
- Check that the URL points directly to an image file

**AWS service errors**:
- Verify AWS credentials are properly configured
- Check IAM permissions for S3, Rekognition, and Polly
- Ensure the S3 bucket exists and is in the same region

**Audio not playing**:
- Check S3 bucket permissions
- Verify the presigned URL hasn't expired (1-hour expiration)

## Cost Considerations

This application uses AWS paid services:
- **S3**: Storage and requests
- **Rekognition**: Per-image analysis
- **Polly**: Per-character speech synthesis

Review [AWS Pricing](https://aws.amazon.com/pricing/) for current rates. Use the cleanup feature to minimize storage costs.

## Security Notes

- Never commit AWS credentials to version control
- Use IAM roles with least-privilege permissions
- Consider implementing authentication for production deployments
- The S3 bucket should have appropriate access controls

## License

This project is provided as-is for educational and demonstration purposes.

## Support

For AWS service issues, consult the [AWS Documentation](https://docs.aws.amazon.com/):
- [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/)
- [Amazon Polly](https://docs.aws.amazon.com/polly/)
- [Amazon S3](https://docs.aws.amazon.com/s3/)
