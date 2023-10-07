<h4>HOW TO RUN IT?</h4>
<ol>
    <li>
        Install package manager pipenv for Python. 'brew install pipenv'
    </li>
    <li>
        Install all packages required to run project. 'pipenv install'. Packages are defined in Pipefile
    </li>
    <li>
        In terminal run 'docker-compose up -d' to start Qdrant API instance
    </li>
    <li>
        Run 'pipenv run python init_db.py' to create and seed vector database collection
    </li>
    <li>
        Run application 'pipenv run uvicorn main:app --reload'
    </li>
    <li>
        For OpenAI specification go to http://127.0.0.1:8000/docs#/
    </li>
</ol>
<br/>