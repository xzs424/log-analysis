# Log Analysis
The project is for Udacity's full stack developer nano degree.

It uses Python 3 and PostgreSQL.

The project creates three queries to fetch data and print them for the following goals respectively:

1. Find the most popular three articles of all time.
2. Find the most popular article authors of all time.
3. Find days where http requests has more than 1% error rate.


# How it works
The project spins up a VM containing python3 runtime environment and hosting a PostgreSQL db, the detailed setting which is defined in `Vagrantfile`.

The program uses thread pool and db connection pool to run three queries for the performance gain.

It has already contains an output file named `src/output.txt` which is the copy of
the query output. If you do not want to run the program to generate a new copy, you can directly check the file to see the output.

When running the program, the program will automatically create a view named `request` in the database, make sure not to have any existing view named `request` if you want to replace the default data with your own.


# File Structure
1. `src` - contains all source code.
2. `src/db` - contains all db related operations.
3. `src/news.py` - contains the implementation of three queries.
4. `src/app.py` - entry point of the program.

# Start the program
1. Install latest version of Vagrant and VirtualBox if you do not have one.
2. Unzip `schema/newsdata.sql.zip` into the same folder, you should get `newsdata.sql` as the output.
3. Optionally, you can overwrite `newsdata.sql` so the database will load your schema and data.
4. In the root directory, run `vagrant up`.
5. Run `vagrant ssh` to ssh into the VM.
6. In your VM, run `cd /vagrant/src` where you can find source code of the program.
7. Run `python3 app.py` to run the program.
8. you can then view the query output in `output.txt` located in the `src` folder.
