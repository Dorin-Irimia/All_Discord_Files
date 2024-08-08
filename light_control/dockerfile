# Imagine de bază
FROM python3.9-slim

# Setează directorul de lucru
WORKDIR app

# Copiază fișierele necesare în container
COPY . app

# Instalează dependențele
RUN pip install --no-cache-dir -r requirements.txt

# Expune portul 8080 (folosit de Google Cloud Run)
EXPOSE 8080

# Comanda pentru a porni aplicația
CMD [gunicorn, -b, 0.0.0.08080, appapp]
