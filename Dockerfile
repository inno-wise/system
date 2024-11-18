FROM python:latest

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . /app

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh

# Make the script executable
RUN chmod +x /entrypoint.sh

# Expose the port Django runs on
EXPOSE 8000

# Use the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

