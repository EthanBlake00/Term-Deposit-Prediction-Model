# Use lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Run the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]