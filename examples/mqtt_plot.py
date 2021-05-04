import matplotlib.pyplot as plt
from deeplens import deeplens

with open("json/face_str.json", "r") as j:
    j = j.read()

deeplens = deeplens(j)

plt.gcf().canvas.set_window_title(deeplens.topic)
plt.title("Face percentage")

print("avg: %f" % (deeplens.avg))
for i in deeplens.face():
    plt.scatter(i, i, s=30, c=1, alpha=0.5)
plt.show()
