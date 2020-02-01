import cv2


def main():
    # Create a cascade classifier
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Read Image as it is.
    img = cv2.imread("photo_2019-09-17_22-09-09.jpg")

    # Convert Image to Grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Search the co-ordinates of the image.
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # img2 = cv2.imread("photo_2019-09-17_22-09-09.jpg", 0)
    # cv2.imshow("Image 1", img)
    resized_img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
    cv2.imshow("Face Detection", resized_img)

    # cv2.imshow("Image Resized", resized_img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    # print(img.shape)
    # print(img2)


if __name__ == '__main__':
    main()
