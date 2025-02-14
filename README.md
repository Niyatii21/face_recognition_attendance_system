# face_recognition_attendance_system

Overview
    This project is a Face Recognition Attendance System implemented using Python, OpenCV, 
    Firebase, and additional libraries. It uses facial recognition to track and manage student 
    attendance in real-time, storing data in a Firebase Realtime Database and managing student 
    images in Firebase Storage.

Technologies Used
   -> Python: Main programming language.
   -> OpenCV: For image processing and face detection.
   -> face_recognition: For facial feature recognition and comparison.
   ->Firebase:
       Realtime Database: For storing and updating student attendance records.
       Storage: For managing student images.
   -> dlib: Used internally by face_recognition for face encoding.
   ->cvzone: Used for GUI enhancements.
   ->Pickle: To store pre-encoded face data for faster processing.
   ->dotenv: For secure handling of Firebase credentials.

Project Setup
    Python 3.8.7 or higher
    Required Python libraries (listed in requirements.txt)
    A Firebase project with Realtime Database and Storage enabled
    A service account JSON file for Firebase Admin SDK

Dependencies
    Ensure the dependencies are installed which are mentioned in the requiremnet.txt file in the
    same order listed.
    Install them using:
    pip install -r reqirements.txt

  
