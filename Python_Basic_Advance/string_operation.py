#string opertions,comparison and information

import numpy as np
sent1 = "This is python learning "
sent2 = "Machine learning basics"
print(np.char.add(sent1,sent2))
print(np.char.lower(sent2))
print(np.char.upper(sent2))
print(np.char.center(sent2,60,fillchar="*"))
print(np.char.split(sent2))
print(np.char.splitlines("This is \n numpy practical"))

str="mdy"
print(np.char.join([":"],[str]))

print(np.char.replace(sent2,'basics','advance'))

print(np.char.equal(sent1,sent2))