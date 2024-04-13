FROM python:3.9-alpine

# Set the working directory to /app
WORKDIR /app

# Requirements are installed here to ensure they will be cached.
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

CMD ["python", "main.py"]
