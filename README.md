# Cowin-Notifier

Use the notifier to get the notification based on district, age slot, and specfic locality. It will also create a txt file for all available slots in the desktop folder.

# Steps for using it.

1.  Install python in your system.
2.  clone the repository.
3.  open terminal in that folder and run pip install -r requirements.txt
4.  open the searchData.json and fill accordingly
5.  It's done .. just click the runner.bat to start it and it will start the program in the background. You can close the terminal that will open after clicking it.
6.  Use the stopper.bat to exit the program. So, click it to stop it.

# Input fields in searchData.json

- state - (needed) enter your state name
- district - (needed) enter your district name
- specificLocality -(optional) enter any specific locality in city
- 18plus - (optional) use "yes" or "true" for searching the data only for 18 + slots
- checksInEveryGivenSeconds - (optional) enter the time window in which data is refreshed . Default 60 seconds

Note - You can change the notification audio by replacing in public folder. Rename the new sound file like "sound.mp3" and place it inside the public folder.

# ScreenShot

![noti](https://user-images.githubusercontent.com/64629430/119117272-b6115b80-ba46-11eb-84a2-90b57baf2920.JPG)
