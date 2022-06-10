import json
import bpy
import glob
import os


model_dir = "Z:/datasets/3D-FUTURE/"

model_info_path = model_dir + "3D-FUTURE-scene/GT/model_infos.json"
test_set_path = model_dir +"3D-FUTURE-scene/GT/test_set.json"
train_set_path = model_dir +"3D-FUTURE-scene/GT/train_set.json"
model_path = model_dir + "3D-FUTURE-model/"


# with open(model_info_path, 'r') as model_info:
#     model_data = json.load(model_info)
# print(len(model_data) )

with open(test_set_path, 'r') as test_set:
    test_data = json.load(test_set)
print(test_data.keys())

# with open(train_set_path, 'r') as train_set:
#     train_data = json.load(train_set)
# print(train_data)


image_id = int(test_data["images"][0]["id"])
scene_content = []

for item in test_data["annotations"]:
    if item["image_id"] == image_id:
        scene_content.append(item)
        pass

print(scene_content)

model_names = [content["model_id"] for content in scene_content]


print("inside image ", image_id , ": ", model_names)



for name in model_names:    
    bpy.ops.import_scene.obj(filepath=model_path + name+"/normalized_model.obj")

# print(test_data["images"][0])
# print(test_data["categories"][0])

# print(test_data["categories"])

# print(len(test_data["annotations"]))
# print(test_data["annotations"][0])

# for model in model_data:
#     print(model["model_id"])