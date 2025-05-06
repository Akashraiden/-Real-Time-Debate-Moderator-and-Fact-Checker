FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt update -y && apt install -y ffmpeg awscli

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose default Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
