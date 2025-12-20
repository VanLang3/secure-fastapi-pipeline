# 1. Use a "Slim" version of Python to reduce the attack surface
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements first (Better for "Layer Caching")
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your application code
COPY main.py .

# 6. Create a non-root user (CYBER BEST PRACTICE)
# By default, Docker runs as 'root'. If a hacker breaks in, they have total control.
# We create a limited user called 'appuser' so the hacker is "trapped".
RUN useradd -m appuser
USER appuser

# 7. Expose the port the app runs on
EXPOSE 8000

# 8. Command to run the "Waiter" (Uvicorn)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
