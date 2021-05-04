from deeplens import deeplens
from datetime import datetime

with open("json/face_dict.json", "r") as j:
    j = j.read()

deeplens = deeplens(j)
nonprecise = deeplens.face(precise=False)

print("Recorded Times %d" % (len(nonprecise)))
for stamp in deeplens.timestamps:
    print(datetime.fromtimestamp(stamp // 1000.0))

print("min: %f, max: %f" % (deeplens.min(False), deeplens.max(False)))
print("Average: %f\n" % (deeplens.avg))
print("Min/Max Average: %f" % ((deeplens.min() + deeplens.max()) / 2))
