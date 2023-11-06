import cv2 as cv
img = cv.imread('photos/eagle.jpeg')
cv.imshow('normal',img)
# resized = cv.resize(img,(500,500),cv.INTER_CUBIC)
flip = cv.flip(img,-1,cv.INTER_CUBIC)

cv.imshow('resized',flip)
cv.waitKey(0)
# capture = cv.VideoCapture('/vids/y2mate.com - Dimash  SOS  2021_v720P.mp4.mp4')
# while True:
#     isTrue ,frame = capture.read()
#     cv.imshow('Video', frame)
#     if cv.waitKey(0) & 0xFF == ord('q'):
#         break
#     capture.release()
#     cv.destroyAllWindows()
# # cap = cv2.VideoCapture('fly.mp4')  # Replace 'video.mp4' with the path to your MP4 file

# # # Check if the video file was opened successfully
# # if not cap.isOpened():
# #     print("Error: Could not open video file.")
# #     exit()

# # while True:
# #     # Read a frame from the video
# #     ret, frame = cap.read()

# #     # Check if the frame was read successfully
# #     if not ret:
# #         print("End of video.")
# #         break

# #     # Display the frame
# #     cv2.imshow('Video', frame)

# #     # Exit if the 'q' key is pressed
# #     if cv2.waitKey(0) & 0xFF == ord('q'):
# #         break

# # # Release the video capture object and close OpenCV windows
# # cap.release()
# # cv2.destroyAllWindows()
# # In this example, we use cv2.VideoCapture and other OpenCV functions to work with the video file. Make sure you have OpenCV installed using pip install opencv-python before running this code.





