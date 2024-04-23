-- Create Mentors table
CREATE TABLE IF NOT EXISTS Mentors (
    MentorID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    Description TEXT,
    Gender TEXT,
    CulturalPreference TEXT,
    FGLI BOOLEAN,
    MentorshipDuration TEXT,
    Major TEXT,
    Rural BOOLEAN
);

-- Create IdentityGroups table
CREATE TABLE IF NOT EXISTS IdentityGroups (
    GroupID INTEGER PRIMARY KEY,
    GroupName TEXT NOT NULL UNIQUE
);

-- Create MentorIdentityGroups junction table
CREATE TABLE IF NOT EXISTS MentorIdentityGroups (
    MentorID INTEGER,
    GroupID INTEGER,
    PRIMARY KEY (MentorID, GroupID),
    FOREIGN KEY (MentorID) REFERENCES Mentors(MentorID),
    FOREIGN KEY (GroupID) REFERENCES IdentityGroups(GroupID)
);