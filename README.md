# Log Analysis
The project is for Udacity's full stack developer nano degree.

This project sets up a mock PostgreSQL database for a a fictional news website.
The provided Python script uses psycopg2 library to query the database and produce
a report that answers the following three questions:

1. Find the most popular three articles of all time.
2. Find the most popular article authors of all time.
3. Find days where http requests has more than 1% error rate.

In addition to it, the provided Python script also leverages thread pool to run queries concurrently
for the performance gain.

# Note
The project has already contained an output file named `src/output.txt` which is the copy of
the query output. If you do not want to run the program to generate a new copy, you can directly check the file to see the output.

# File Structure
1. `src` - contains all source code.
2. `src/db` - contains all db related operations.
3. `src/news.py` - contains the implementation of three queries.
4. `src/app.py` - entry point of the program.
4. `src/schema/create_views.sql` - includes views need to be created before running `app.py`.

# Start the program
1. Install latest version of Vagrant and VirtualBox if you do not have one.
2. Unzip `schema/newsdata.sql.zip` into the same folder, you should get `newsdata.sql` as the output.
3. Optionally, you can overwrite `newsdata.sql` so the database will load your schema and data.
4. In the root directory, run `vagrant up`.
5. Run `vagrant ssh` to ssh into the VM.
6. In your VM, run `psql news -f /vagrant/schema/newsdata.sql` to load the data if are using your own `Vagrantfile`.
7. In your VM, run `psql news -f /vagrant/schema/create_views.sql` to load the views if you are using your own `Vagrantfile`.
8. In your VM, run `cd /vagrant/src` where you can find source code of the program.
9. Run `python3 app.py` to run the program.
10. you can then view the query output in `output.txt` located in the `src` folder.
