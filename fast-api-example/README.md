<p>
    Fast API application that shows an example of database communication using sqlaclehmy and request object validation with pydantic.
</p> <br/>

Fast API is modern web framework for building API-s with Python. Fast API contains everything for standard web development:
<ol>
	<li> Starlette for building REST API, web sockets, etc. </li>
	<li> Pydantic for any type of data validation </li>
	<li> Global exception filters, Middlewares </li>
	<li> Dependencies </li>
	<li> Background tasks </li>
	<li> Security </li>
	<li> supports open standards for APIs right out of the box </li>
	<li> works with any database or library that “talks” to the database </li>
</ol>

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