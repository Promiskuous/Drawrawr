def allowedFile(filename,extensions):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in extensions

def fileType(filename):
  return filename.rsplit('.', 1)[1]

def printList(l):
  newL = ""
  end = len(l)
  for item in range(0, end):
    if item == (end - 2):
      spaceWord = ", and "
    elif item == (end - 1):
      spaceWord = ""
    else: spaceWord = ", "
    newL += l[item] + spaceWord
  return newL

def unsplit(listOfStrings):
  if listOfStrings != []: return reduce(lambda prior, new: prior + " " + new ,listOfStrings)
  else: return ""

def dictToList(d):
  l = []
  for k in d:
    l.append(d[k])
  return l

def parseCommentMap(cMap):
  '''
  Returns a string that can be used in mongodb to find a comment reply

  Input:  "1,2,3,4,5"
  Output: "r.1.r.2.r.3.r.4.r.5.r"
  '''
  if cMap == "": return "r"
  validMap = "r."
  currentObject = ""
  for c in cMap:
    if c == ",":
      int(currentObject)
      validMap += currentObject + ".r."
      currentObject = ""
    else: currentObject += c
  int(currentObject)
  validMap += currentObject + ".r"
  return validMap  

def compareDicts(d1,d2):
  '''
  Despite the name, this just checks to make sure every key in d1 has a counterpart in d2 that's value is the same. 
  '''
  for key in d1:
    if key in d2:
      if not d1[key] == d2[key]: return False
    else: return False
  return True

def compareDictKeys(d1,d2):
  '''
  Same as above, but compares the key names rather than the key values. 
  '''
  for key in d1:
    if not key in d2: return False
  return True

def concDictValues(d1,d2):
  ''' Takes two dicts with the same keys and puts the key's values together like this: concDictValues({1:"o",2:"tw"},{1:"ne",2:"o"}) == {1:["o","ne"],2:["tw","o"]} '''
  newD = {}
  for key in d1:
    if key in d2:
      newD[key] = [d1[key], d2[key] ]
  return newD

def urlDecode(string):
  '''
  Decodes a URL string to a dict of strings
  Example: urlDecode("name=lambdanaut&age=20&") = {"name" : "lambdanaut", "age" : "20"}
  Note: Last character in string must be ampersand
  '''
  result = {}
  curVal  = ""
  curName = ""
  isName=True
  for letter in string:
    if isName:
      if letter != "=": curName += letter
      else: isName=False
    else:
      if letter != "&": curVal += letter
      else:
        result[curName] = curVal
        curVal = curName = ""
        isName=True
  return result
