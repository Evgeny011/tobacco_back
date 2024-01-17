FROM python:3

WORKDIR /tobacco_back

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/src

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /tobacco_back/requirements.txt

COPY . .


CMD ["uvicorn", "src.fastapi_tabak:app", "--host", "0.0.0.0", "--port", "8000"]
