import sqlite3

class Mentor:
    def __init__(self, name, email, description, gender, cultural_preference, fgli, mentorship_duration, major, rural):
        self.name = name
        self.email = email
        self.description = description
        self.gender = gender
        self.cultural_preference = cultural_preference
        self.fgli = fgli
        self.mentorship_duration = mentorship_duration
        self.major = major
        self.rural = rural

def get_database_connection():
    """Returns a connection to the database."""
    return sqlite3.connect('database.db')

def get_mentor(mentor_id):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = 'SELECT Name, Email, Description, Gender, CulturalPreference, FGLI, MentorshipDuration, Major, Rural FROM Mentors WHERE MentorID = ?'
    try:
        cursor.execute(query, (mentor_id,))
        result = cursor.fetchone()
        if result:
            mentor = Mentor(
                name=result[0], 
                email=result[1], 
                description=result[2], 
                gender=result[3], 
                cultural_preference=result[4], 
                fgli=result[5] == 1,
                mentorship_duration=result[6],
                major=result[7],
                rural=result[8] == 1
            )
            return mentor
        else:
            return None
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return None
    finally:
        connection.close()

def get_mentor_id_by_name(mentor_name):
    """Returns the unique ID of a mentor given their name."""
    connection = get_database_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT MentorID FROM Mentors WHERE Name = ?"
        cursor.execute(query, (mentor_name,))
        row = cursor.fetchone()
        if row:
            return row['MentorID']
        else:
            return None
    except sqlite3.Error as e:
        print(f"An error occurred: {e.args[0]}")
        return None
    finally:
        connection.close()

def get_mentor_by_name(mentor_name):
    """Returns a Mentor object given the mentor's name."""
    mentor_id = get_mentor_id_by_name(mentor_name)
    if mentor_id is not None:
        return get_mentor(mentor_id)
    else:
        return None


def get_mentors(mentor_ids):
    mentors = []
    for mentor_id in mentor_ids:
        mentor = get_mentor(mentor_id)
        if mentor:
            mentors.append(mentor)
    return mentors