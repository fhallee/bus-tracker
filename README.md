# MTA Bus Tracker
#### Video Demo:  <https://youtu.be/pvRycR_9utY>

## Introduction

The MTA Bus Tracker is a web application designed to streamline navigation of NYC's bus system by providing real-time bus arrival information. Developed during CS50x 2023, this project aims to empower users with accurate and timely data, enabling efficient journey planning and reducing wait times.

## Key Features:

- Live Bus Tracking: Get the lowdown on upcoming buses and their estimated arrival times in real time, powered by the MTA's Bus Time API.
- User-Friendly Search: Find your stop in a flash with a search bar that offers suggestions as you type, making navigating the city streets a breeze.
- Mobile Compatibility: Take this handy tool with you wherever you go! Its optimized design ensures seamless viewing and interaction on your smartphone.

## Technical Implementation

Programming Languages and Frameworks:

- Python: Handles the back-end logic and interacts with the API.
- JavaScript: Powers the dynamic front-end features and user interactions.
- Flask: Provides the Python web framework for routing and app structure.

## Key Files:

- app.py: The main application file, where the magic happens with routing and core logic.
- templates/index.html: This is the home page template, the first thing you see when you jump onto the app.
- templates/stopinfo.html: Dive deeper into a specific stop here, where you'll find detailed information about upcoming buses.
- templates/stopnameerror.html: Uh oh, looks like you typed in a stop that doesn't exist! This page guides you back on track.
- static/scripts.js: This script brings the front-end to life with dynamic features and interactions from Bootstrap.
- static/styles.css: Makes sure the app looks sleek and stylish wherever you access it.
- bus.db: A SQLite database holding all the stop information, including IDs, names, and even their location on a map.
- bus_backup.db: Because it's always good to have a backup plan, even for your bus app!
- import_stop_ids.py: This script grabs all the stop IDs from the MTA API and pops them into the bus.db database.
- populate_stop_names.py: Fills in the blanks by adding stop names and locations to the database, including some coordinates for future versions with even more features!

## Design Choices

- Real-Time Information First: We prioritized providing accurate, real-time bus arrival data to help you make informed decisions about your journey.
- Mobile-First Approach: Since smartphones are often the go-to for checking bus info, we made sure the app looks and works great on your mobile device.
- Intuitive Interface: We kept things simple and user-friendly, focusing on clear search functionality and easy-to-read bus arrival data.

## Future Enhancements

- Imagine this: no more frantically searching for nearby stops! We're thinking about incorporating your location to suggest them automatically.
- Feeling ambitious? We might build out features for planning your entire route and mapping your journey.
- More data, more power! We might integrate with other transit sources to give you a complete picture of your travel options.

## Conclusion

MTA Bus Tracker is a shining example of how technology can improve our urban experience. By delivering real-time information and prioritizing user needs, we aim to empower you to navigate the city's bustling bus system with confidence and ease. So, hop on board and experience the freedom of knowing exactly when your next bus arrives!
