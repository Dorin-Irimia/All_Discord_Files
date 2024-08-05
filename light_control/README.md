
# Control Becurilor Inteligente cu Flask

Acest proiect exemplifică un server backend simplu folosind Flask, care permite controlul unui bec inteligent.

## Fisiere

- `app.py`: Codul principal al aplicației, include API-ul pentru obținerea și setarea stării becului.
- `requirements.txt`: Lista dependențelor necesare pentru a rula aplicația.
- `.env`: Fișier pentru variabile de mediu (dacă este necesar).

## Instalare și Utilizare

### 1. Instalare Dependențe

Asigură-te că ai instalat `pipenv` sau `virtualenv` pentru a gestiona mediul virtual. Apoi, instalează dependențele:

```bash
pip install -r requirements.txt
```

### 2. Rulare Aplicație

Pornește serverul Flask:

```bash
python app.py
```

Aplicația va porni pe adresa `http://0.0.0.0:5000`.

### 3. Utilizare API

#### Obține starea becului

```http
GET /api/light
```

Răspuns:

```json
{
  "state": false
}
```

#### Setează starea becului

```http
POST /api/light
Content-Type: application/json

{
  "state": true
}
```

Răspuns:

```json
{
  "success": true,
  "state": true
}
```

## Note

Acesta este un exemplu simplificat și trebuie extins pentru a include securitate, autentificare, și logica specifică pentru controlul hardware-ului.
