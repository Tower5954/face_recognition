import face_recognition as fr

image_of_bill = fr.load_image_file("./Known/Bill Gates.jpg")
bill_face_encoding = fr.face_encodings(image_of_bill)[0]

unknown_image = fr.load_image_file("./Unknown/d-trump.jpg")
unknown_face_encoding = fr.face_encodings(unknown_image)[0]

# -- Compare faces

results = fr.compare_faces([bill_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Bill Gates')
else:
    print('This is not Bill Gates')

