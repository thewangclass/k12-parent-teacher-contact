# k12-parent-teacher-contact

Parent Contact is a program for automatically contacting parents of a student when they are in danger of failing for the
nine weeks.

## Installation

Make a clone of the repository.  
Place your message in the *messages* folder and modify the email_notification.py letter_path variable.  
See messages folder for example.

Place your spreadsheet data in the *data* folder and modify the main.py FILE_NAME variable.  
See data folder for example.

Create a .env file and place your email username and password there. Choose an email you want to send from - this can be
the same as your email username.

## Usage

Run the main.py script, and it will automatically email the parents.

## TO-DO

- Track emails sent (database)
- Track parents who respond to email
  - If no response, send text message in addition to email (via GVoice or Twilio)
- Grab a list of assignments students have not completed OR performed poorly on
  - Pop
- Automatically calculate grade average (allow the teacher to input grade directly into spreadsheet)
- Personalize messages depending on class student is in
