# Full Stack FastAPI Template

## Structure

```
project/
├── app/
│   ├── main.py                         # Entry point for FastAPI app
│   ├── dependencies.py                 # Dependency injection and shared utilities
│   ├── core/                           # Core business logic
│   │   ├── v1/                         # Version
│   │   │   ├── health/                 # Domain health v1
│   │   │   │   ├── usecase/            # Usecase health v1
│   │   │   │   ├── repository/         # Repository health v1
│   │   │   │   ├── entities/           # Domaini entities health v1
│   ├── infrastructure/                 # Frameworks and drivers
│   │   ├── database.py                 # Simulated or actual database logic
│   ├── handlers/                       # Request handlers (it can be HTTP Request or Event from message queue)
│   │   │   ├── http-routes/            # HTTP endpoints
│   │   │   │   ├── v1/                 # HTTP endpoints Version
│   ├── scripts/                        # Scripts related to the repo
└── tests/                              # Unit and integration tests
    ├── core/
    ├── infrastructure/
    ├── routers/
```
