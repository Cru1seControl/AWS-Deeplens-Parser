from deeplens import deeplens
from datetime import datetime

with open("json/face_hex.json", "r") as j:
    j = j.read()

deeplens = deeplens(j)

topic = deeplens.topic
nonprecise = deeplens.face(precise=False)

print("Showing stats for Topic %s" % (topic))
for i in nonprecise:
    print("%d%%" % (i), end=" ")
print("\n")
