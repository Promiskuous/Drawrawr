import config, os, commands

def databaseSetup(db):
  # Incremental Key Setup
  art      = db.db.seq.find_one({"_id" : "art"})
  users    = db.db.seq.find_one({"_id" : "users"})
  journals = db.db.seq.find_one({"_id" : "journals"})
  comments = db.db.seq.find_one({"_id" : "comments"})
  if not art:
    db.db.seq.insert({"_id" : "art", "next" : 0})
  if not users:
    db.db.seq.insert({"_id" : "users", "next" : 0})  
  if not journals:
    db.db.seq.insert({"_id" : "journals", "next" : 0})  
  if not comments:
    db.db.seq.insert({"_id" : "comments", "next" : 0})  

def directorySetup():
  # /uploads/ setup
  if not os.path.exists("uploads"):
    os.mkdir("uploads")
    os.mkdir(os.path.join("uploads","icons") )
    os.mkdir(os.path.join("uploads","art") )
    os.mkdir(os.path.join("uploads","thumbs") )

def javascriptSetup():
  # Compile coffeescript files
  jsPath = os.path.join("static","js")
  if not os.path.exists(os.path.join(jsPath,"main.js")):
    commands.getoutput("coffee -c " + os.path.join(jsPath,"main.coffee") + " " + os.path.join(jsPath,"tabs.coffee") + " " + os.path.join(jsPath,"submit.coffee") + " " + os.path.join(jsPath,"settings.coffee") )

def main(db):
  databaseSetup(db)
  directorySetup()
  javascriptSetup()
