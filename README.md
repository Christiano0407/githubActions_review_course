# Proyect API (Python with Fast API) To GitHub Actions
Review Course GitHub Actions 

## Process To API Project | GitHub Actions 

> Review Process To Write an Pull Request & Testing | GitHub Actions | CLI

> Review all Process to my Workflows

## My Project API with FastAPI 

> This repository contains an API application developed with Fastapi, designed to manage a collection of items. Includes a robust testing configuration with Pytest and CI/CD automation with GITHUB Actions.

> Characteristics

- API Restful: built with Fastapi for rapid and easy development performance.
- Items management: endpoints to obtain individual items and items lists.
- Memory database: Use a simulated list (Fake_DB) as a database to simplify the example.
- Data validation: Use of Pydantic for the validation and serialization of data models.
- Robust testing: coverage of unit tests and integration with Pytest.
- Automated CI/CD: GITHUB ACTIONS WORKFLOWS To automatically run tests on each Push or Pull Request.

## Structure Of Project

```bash
.
├── .github/                  # Configuración de GitHub (workflows de Actions)
│   └── workflows/
│       └── pytest.yml        # Workflow para ejecutar tests con Pytest
├── backend/                  # Contiene el código fuente de la aplicación API
│   ├── api_backend/          # Módulo principal de la aplicación
│   │   ├── __init__.py
│   │   └── app.py            # Archivo principal de la aplicación FastAPI
│   └── __init__.py
├── tests/                    # Contiene los tests para la aplicación
│   └── test_api.py           # Tests para los endpoints de la API
├── .gitignore                # Archivos y directorios ignorados por Git
├── LICENSE                   # Información de la licencia del proyecto
├── README.md                 # Este archivo
└── requirements.txt          # Dependencias del proyecto

```

## Strategy To The Branch

> This project follows a branching strategy that facilitates the development and integration of new characteristics and corrections.

 Main:

- It is the main and stable branch of the project.
- It only contains proven code and ready for production.
- Main merges must come from Dev_api or Test (after passing all the tests).

 Workflows:

- Rama dedicated to configuration and experimentation with Github Actions.
- Here new workflows are developed and tested or the existing ones are adjusted before integrating them into Main or Test.

 DEV_API:

- Main development branch for new characteristics and functionalities of the API.
- All changes related to the logic of the API are made here.
- Once the characteristics are complete and tested locally, they merge in Main.

 test:

- Rama dedicated to the development and execution of tests (Pytest).
- Here the tests are written and executed to guarantee the quality of the code.
- This branch remains synchronized with Main to ensure that the tests are executed against the latest version of the API code.
- It is the branch where Github Actions's workflow is automatically triggered to validate the tests.

## Install Dependencies To The Project 

> Install requirements.txt 

```bash
 pip install -r requirements.txt
```

> Install Pytest & Httpx

```bash
 pip install pytest httpx
```

> Install Uvicorn To Server


```bash
 pip install uvicorn
```

## Execute API (Local - Server) 

> Execute Local to the API in Server (Uvicorn)


```bash
uvicorn backend.api_backend.app:app --reload
```

> Run The Tests

```bash
python -m pytest
```

## Endpoints To The API

> API CRUD | Endpoints: 

Get /

- Description: Endpoint welcome to the API.
- Answer: {"Message": "Welcome to My New Api Application with Fastapi"}

Get /Items /

- DESCRIPTION: Get a list of all the items available in the simulated database.
- Answer: List [Item] (a list of item objects).

Get /Items /{item_id}

- DESCRIPTION: Get a specific item by your ID.
- Route parameters:

Item_id (Integer): The unique ID of the item to look for.

- Answer: Item (an Item object if you are).
- Errors: 404 Not Found If the item does not exist ({"detail": "item not exist."}).

## Automated Testing (pytest)

> The project uses Pytest for the execution of tests. The tests are found in the Tests/folder.

> To execute the tests, make sure you have the installed units and the virtual environment activated, then execute:

```bash
python -m pytest
```

## Continuous Integrations & Continuous Deploy (CI/CD) | GitHub Actions

> This repository is configured with Github Actions to automate the execution of the tests.

> Note: After Push [merge] the Branch delete (dev_api | workflows | test)

Workflow location: 
```bash
  .github/workflows/pytest.
```

Triggers:

- Each push to the Main, Dev_api, Workflows and Test branches.

- Each Pull requires towards the Main, Dev_api, Workflows and Test branches.

Functionality: 

- The workflow installs the project units and then executes Python -M Pytest to validate that all the tests pass.

### License MIT 

> This Project is Under License MIT 