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