FROM python:3.11

WORKDIR /tobacco_back

COPY ./requirements.txt /tobacco_back/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tobacco_back/requirements.txt

COPY . ./

CMD ["uvicorn", "src.fastapi_tabak:app", "--host", "0.0.0.0", "--port", "8000"]
