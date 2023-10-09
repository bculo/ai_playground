
<h4>HOW TO RUN IT?</h4>
<ol>
    <li>
        Install package manager pipenv for Python. 'brew install pipenv'
    </li>
    <li>
        Install all packages required to run project. 'pipenv install'. Packages are defined in Pipefile
    </li>
    <li>
        Execute all available migrations and create database. 'pipenv run alembic upgrade head'
    </li>
    <li>
        Run application 'pipenv run uvicorn main:app --reload'
    </li>
    <li>
        For OpenAI specification go to http://127.0.0.1:8000/docs#/
    </li>
</ol>
<br/>


<h4>HOW TO CREATE MIGRATION?</h4>
<ol>
    <li>
        Add new entities to models.py file
    </li>
    <li>
        Generate migration file. 'pipenv run alembic revision --autogenerate -m "Migration message"'
    </li>
    <li>
        Execute migration. 'pipenv run alembic upgrade head'
    </li>
</ol>
