import face_recognition as fr

image = fr.load_image_file('./cmake/Groups/team2.jpg')
face_locations = fr.face_locations(image)

# -- Array of coords of each face
print(face_locations)

print(f"There are {len(face_locations)} people in this frame")



