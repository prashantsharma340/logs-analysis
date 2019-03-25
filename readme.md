                                                                LOGS ANALYSIS

Our task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. 
This reporting tool is a Python program using the psycopg2 module to connect to the database.
I connected the database server with psycopg2 module like:-     
    db = psycopg2.connect("dbname=news")

TOOLS REQUIRED TO RUN THE CODE:
1. Install vagrant
2. Install virtual box
3. git bash

STEPS:
1. Open git terminal and cd to the project folder.
2. cd into vagrant directory and then run 'vagrant up' to start the virtaul machine.
3. Then run the 'vagrant ssh' command.
4. cd to vagrant.
5. To load the data, cd into the vagrant directory and use the command 'psql -d news -f newsdata.sql'
6. Now you can try out your queries in the news database in psql.
7. If you want to run now the logs_analysis file
    use command "python logs_analysis.py".


                 