import os
import cs50

db = cs50.SQL("sqlite:///database.db")

os.makedirs('metadata')
os.makedirs('metadata/problems')
problems = db.execute("SELECT * FROM problems")

for problem in problems:
	pid = problem["id"]
	description = problem["description"]
	editorial = problem["editorial"]
	hints = problem["hints"]
	if description is None:
		description = ""
	if editorial is None:
		editorial = ""
	if hints is None:
		hints = ""
	os.makedirs('metadata/problems/' + pid)
	f = open('metadata/problems/' + pid + '/description.md', 'w')
	f.write(description)
	f.close()
	f = open('metadata/problems/' + pid + '/hints.md', 'w')
	f.write(hints)
	f.close()
	f = open('metadata/problems/' + pid + '/editorial.md', 'w')
	f.write(editorial)
	f.close()

db.execute("BEGIN")
db.execute("CREATE TABLE 'problems_tmp' ('id' varchar(64) NOT NULL, 'name' varchar(256) NOT NULL, 'point_value' integer NOT NULL DEFAULT (0), 'category' varchar(64), 'flag' varchar(256) NOT NULL, 'draft' boolean NOT NULL DEFAULT(0))")

for problem in problems:
	db.execute("INSERT INTO problems_tmp VALUES(?, ?, ?, ?, ?, ?)",
			   problem["id"], problem["name"], problem["point_value"],
			   problem["category"], problem["flag"], problem["draft"])

db.execute("DROP TABLE problems")
db.execute("ALTER TABLE problems_tmp RENAME TO problems")
db.execute("COMMIT")