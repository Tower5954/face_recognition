import face_recognition as fr
from PIL import Image

image = fr.load_image_file('Groups/team2.jpg')
face_locations = fr.face_locations(image)

for face_location in face_locations:
    top, right, bottom, left = face_location

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save(f"{top}.jpg")