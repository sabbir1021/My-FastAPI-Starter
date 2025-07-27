Project Structure:

fastapi_app/
├── app/
│   ├── modules/
│   │   └── auth/
│   │       ├── controller.py
│   │       ├── router.py
│   │       ├── schemas.py
│   │       └── service.py
│   ├── core/
│    │  ├── helpers/
│   │   └── config.py
│   ├── main.py
│   ├── routers.py
│   └── worker/
├── tests/
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .github/
    └── workflows/
        └── ci.yml



<!-- Task -->
1. database connect
2. Custom response Middleware
3. redis connect
4. celery connect
5. JWT Authentication
6. Dependency 
7. unit and integration test
8. mypy setup


Project Run:
```uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload```


Build & Run with Docker 
```docker-compose up --build```

Use the -d flag to run in detached mode:
```docker compose up --build -d```

See docker live Logs for a Specific Service
fastapi here is Specific Service
```docker compose logs -f fastapi```

See Logs from All Services
```docker compose logs -f```

To Stop the Running Container
```docker compose down```
```docker compose stop ```

### To fix the distutils dependency issue in docker
```sudo apt update```
```sudo apt install python3-distutils```



### pytest for unit and integration test:

need install pytest and httpx

export pwd for pythonpath in run pytest
```export PYTHONPATH=$(pwd)```

run command:
```pytest -v tests/```

for details or log use command:
```pytest -s tests/```


