# Sign In System

This is a face recognition sign in system that can replace written sign in sheets.

##How to use:

1. Install OpenCV and Python 2.7

2. Download this repository

3. Create a data set of a member's face. Add members one at a time by running ```python add_user.py```, entering a unique ID number (maybe student ID?), and having the member look directly into webcam. 

4. Once all of the members have been added to the data set (check the folder face_set), run ```python trainer.py``` to create recognizer

5. Now you're all set! Run ```python face_detector.py```, enter the appropriate date (in MM.DD.YY format), and have members look into webcam one by one (they can confirm that they have been logged if their name shows up in the command line)
