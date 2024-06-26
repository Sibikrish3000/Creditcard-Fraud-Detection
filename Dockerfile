FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files into the container
COPY . .

# Expose the ports for both FastAPI and Gradio
EXPOSE 8000
EXPOSE 7860

# Command to run both FastAPI and Gradio servers
CMD ["python", "gradio_app.py","&&","uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]