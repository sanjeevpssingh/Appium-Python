import json
import os
from pathlib import Path
def DataJSON(filename,key):
    path = Path(__file__).parent.parent
    path = os.path.join(path,"Test_Data")
    os.chdir(path)
    print(path)
    with open("Locators.json") as file:
      data=json.load(file)
    return(data[key])



