# python-api-flask
Example of REST API being developed in python with flask

<b>Running project in your local machine</b>

To run this project on your local machine, follow the instructions below:

Download the project to your local machine with the command:

<pre>
git clone https://github.com/rafaelct/python-api-flask.git
</pre>

Enter the project folder:

<pre>
cd python-api-flask
</pre>
Go to the Python page and download version 3.x:

https://www.python.org/downloads/release/python-386/

On the python installation screen, check the option to include in PATH.
After the installation is complete, close the command prompt and open it again to consider the PATH environment variable updated.
Enter the project folder again.

Install the necessary python libraries in the project:
<pre>
pip install flask
pip install psycopg2-binary
pip install -U pytest
</pre>
Download and install the Postgresql database from the link below:

https://www.enterprisedb.com/postgresql-tutorial-resources-training?cid=48

After installed and configured, enter the Windows settings under Systems-> Edit environment variables and create a variable named DATABASE_URL, and in the content put the database connection string.

Access pgAdmin in query tools, run the contents of the scripts.sql file, to create the database structure.

I started the application with the command below:
<pre>
python web.py
</pre>
I started the application with the command below:

http://localhost:5000/<desired service request url>

<b>Running automated tests on your local machine</b>

Enter the project folder (downloaded in the previous step, see 3):

Clean the database by running the scripts.sql file in pgtools:

To test on localhost use:
<pre>
pytest teste_web_urls.py
</pre>
To test the model classes use:
<pre>
pytest teste_web.py
</pre>
