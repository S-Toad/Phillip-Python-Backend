class JSONObject:
  def __init__(self, name):
    self.name = '"' + name + '"'
    self.paramDictionary = {}
    self.objectList = []
    self.text = ''
  
  def addJsonObject(self, jsonObject):
    self.objectList.append(jsonObject)
  
  def addStringParam(self, paramName, paramValue):
    param = '"' + paramName + '"'
    value = '"' + paramValue + '"'
    
    self.paramDictionary[param] = value
  
  def addParam(self, paramName, paramValue):
    param = '"' + paramName + '"'
    
    self.paramDictionary[param] = paramValue
  
  def hasChildren(self):
    return (len(self.objectList) != 0)
    
  def step(self):
    self.text += self.name + ':{'
    
    for param, value in self.paramDictionary.items():
      self.text += param + ':' + str(value) + ','
    
    if (self.hasChildren()):
      for jsonObject in self.objectList:
        jsonText = jsonObject.step()
        
        self.text += jsonText
        self.text += ','
    self.text = self.text[:-1]
    self.text += '}'
    
    return self.text
  
  def constructText(self):
      return '{' + self.step() + '}'