-- Insert identity groups
INSERT INTO IdentityGroups (GroupName)
VALUES 
('Afro-American Cultural Center'),
('La Casa Cultural Center'),
('Asian American Cultural Center');

-- Insert mentors
INSERT INTO Mentors (Name, Email, Description, Gender, CulturalPreference, FGLI, MentorshipDuration, Major, Rural)
VALUES 
('Christina Walker', 'christinawalker@yale.edu', 'Christina is a junior at Silliman College.
Originally from Pasadena, California, Christina identifies aspires to become a Pharmacist someday.
She loves to bake, listen to afrobeats, and explore nature in her free time. She is willing to have 2-3 mentees.', 'Female', 'Black/African American', 1, 'Short term', 'Medical', 0),
('Alicia Kim', 'aliciakim@yale.edu', 'Alicia is a senior at Jonathan Edwards College.
 Originally from Boston Massachusetts, Alicia aspires to become a museum curator.
 She is on the Yale Rugby team and in her spare time loves to paint.
 She is willing to have one mentee with whom she agrees to meet at least once a month.', 'Female', 'Asian', 0, 'Long term', 'Humanities', 1),
('Malcolm Wayne', 'malcolmwayne@yale.edu', 'Malcolm is a junior at Benjamin Franklin College. Originally from Charlotte, North Carolina.
 Malcolm aspires to become a corporate lawyer someday. Malcolm is a part of the Yale Alley Cats and in his free time loves to play intramural basketball.
 He is willing to have 2-3 mentees.', 'Male', 'White', 1, 'Long term', 'Law', 1);

-- Link mentors to identity groups by their unique attributes (e.g., email and group name)

-- Christina Walker's Associations
INSERT INTO MentorIdentityGroups (MentorID, GroupID)
SELECT m.MentorID, ig.GroupID
FROM (SELECT MentorID FROM Mentors WHERE Email = 'christinawalker@yale.edu') m,
     (SELECT GroupID FROM IdentityGroups WHERE GroupName IN ('Afro-American Cultural Center', 'La Casa Cultural Center')) ig;

-- Alicia Kim's Association
INSERT INTO MentorIdentityGroups (MentorID, GroupID)
SELECT m.MentorID, ig.GroupID
FROM (SELECT MentorID FROM Mentors WHERE Email = 'aliciakim@yale.edu') m,
     (SELECT GroupID FROM IdentityGroups WHERE GroupName = 'Asian American Cultural Center') ig;

-- Malcolm Wayne has no identity group associations, so no insertion into MentorIdentityGroups for him.