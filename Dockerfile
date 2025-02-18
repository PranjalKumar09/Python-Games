FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/* .
COPY static/* static/
CMD ["python", "src/snake_game.py"]