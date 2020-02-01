import cv2, time

def main():
    video = cv2.VideoCapture(0)  # The object to capture video. 0 indicates ; use the built in camera

    a = 1 # Variable to count number frames it captures.
    while True:
        a += 1
        check, frame = video.read()
        print(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Capturing", gray)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
    print(a)
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()