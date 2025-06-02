# Use an official Python image with minimal base
FROM python:3.12-slim

# Set environment variables to avoid Python prompts
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy all files to container
COPY . .

# Install system dependencies for Pillow and TensorFlow
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxrender1 libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default Streamlit port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
