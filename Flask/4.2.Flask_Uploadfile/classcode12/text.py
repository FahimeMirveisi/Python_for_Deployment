from deepface import DeepFace


objs = DeepFace.analyze(
    img_path = "Flask/4.2.Flask/classcode12/uploads/sara1.jpg",
    actions = ['age'],
)

#print(objs[0]['age'])
print(objs)