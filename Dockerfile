FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app

# Copy application code
COPY . .

# Fix file permissions for non-root user
RUN chown -R app:app /app

# Set Flask environment variables
ENV FLASK_APP=app
ENV FLASK_ENV=production

# Switch to non-root user
USER app

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app/app.py"]