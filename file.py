from nbformat import write
from pyflowchart import Flowchart
with open(r"F:\project inc\main project file\temp\gcd.py") as f:
    code = f.read()
 
fc = Flowchart.from_code(code)
data=fc.flowchart()

f = open(r"F:\project inc\main project file\temp\test.txt", "w")
f.write(data)
f.close()