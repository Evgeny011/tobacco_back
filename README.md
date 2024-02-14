# Tobacco incentory application 📈

## Created by [Evgeny011](https://github.com/Evgeny011) - back & [shalimovSens](https://github.com/shalimovSens) - front

### Technologies I used in the project:

- Sqlalchemy
- FastApi
- SQLite
- Pydantic
- DOcker
- Uvicorn
- Python

### Frontend repository: https://github.com/shalimovSens/tobacco__front   

Frontend stack: Vue & TypeScript & TailwindCSS   

## Launching the application   

### Uvicorn   

Install virtual environment   
`python3 -m venv .venv`   

Activate the virtual environment   
`. .venv/bin/activate`   

Install dependencies into virtual environment   
`pip install -r requirements.txt`  

Start uvicorn   
`uvicorn app:app --reload`

### Docker   

`
docker build -t fastapi .

docker run -d --name mycontainer -p 8000:8000 fastapi

`








