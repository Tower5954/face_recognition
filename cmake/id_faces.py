import face_recognition as fr
from PIL import Image, ImageDraw

image_of_bill = fr.load_image_file("./Known/Bill Gates.jpg")
bill_face_encoding = fr.face_encodings(image_of_bill)[0]

image_of_steve = fr.load_image_file("./Known/Steve Jobs.jpg")
steve_face_encoding = fr.face_encodings(image_of_steve)[0]

image_of_Elon = fr.load_image_file("./Known/Elon Musk.jpg")
elon_face_encoding = fr.face_encodings(image_of_Elon)[0]

# -- Create array of encodings and name -- #
known_face_encodings = [
    bill_face_encoding,
    steve_face_encoding,
    elon_face_encoding
]

known_face_names = [
    "Bill Gates",
    "Steve Jobs",
    "Elon Musk"
]

# -- Load test image to find faces in -- #

test_image = fr.load_image_file("Groups/bill-steve-elon.jpg")

# -- find faces in test images -- #

face_locations = fr.face_locations(test_image)
face_encodings = fr.face_encodings(test_image, face_locations)

# -- convert to PIL format -- #

pil_image = Image.fromarray(test_image)

# -- Create a image draw instance -- #

draw = ImageDraw.Draw(pil_image)

# loop through faces in test image -- #
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = fr.compare_faces(known_face_encodings, face_encoding)

    name = 'Unknown Person'

    # If match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw Box
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

    # Draw Label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0), outline=(0, 0, 0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

del draw

#Display image
pil_image.save(f"{top}.jpg")