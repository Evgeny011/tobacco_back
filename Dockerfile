FROM python:3

WORKDIR /tobacco_back

COPY ./requirements.txt /tobacco_back/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tobacco_back/requirements.txt

COPY ./src /tobacco_back/src

CMD ["uvicorn", "src.fastapi_tabak:app", "--host", "0.0.0.0", "--port", "8000"]
