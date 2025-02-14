import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase Admin SDK with credentials and database URL
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-3c16b-default-rtdb.firebaseio.com/"
})

# Reference to the "Students" node in Firebase Realtime Database
ref=db.reference('Students')

# Student data to be uploaded to Firebase
data = {
    "21109":
        {
            "name" : "Niyati Negi",
            "major": "Btech",
            "starting year" :2021,
            "total_Attendance": 6,
            "standing":"A",
            "year":4,
            "last_attendance_time":"2025-01-24 00:54:34"
        },
"24105":
        {
            "name" : "Mudit Jain ",
            "major": "Btech",
            "starting year" :2021,
            "total_Attendance": 7,
            "standing":"A",
            "year":4,
            "last_attendance_time":"2025-01-25 00:54:34"
        },
"73200":
        {
            "name" : "Keshav Chauhan",
            "major": "Btech",
            "starting year" :2021,
            "total_Attendance": 4,
            "standing":"A",
            "year":4,
            "last_attendance_time":"2025-01-20 00:54:34"
        },
"852741":
        {
            "name" : "Emly Blunt",
            "major": "BArch",
            "starting year" :2021,
            "total_Attendance": 6,
            "standing":"B",
            "year":4,
            "last_attendance_time":"2025-01-24 00:54:34"
        },
"963852":
        {
            "name" : "Elon Musk",
            "major": "BArch",
            "starting year" :2023,
            "total_Attendance": 6,
            "standing":"C ",
            "year":4,
            "last_attendance_time":"2025-01-24 00:54:34"
        }
}


for key,value in data.items():
    ref.child(key).set(value)