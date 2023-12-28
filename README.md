# MTA Bus Tracker
#### Video Demo:  <https://youtu.be/pvRycR_9utY>

## Introduction

The MTA Bus Tracker is a web application designed to streamline navigation of NYC's bus system by providing real-time bus arrival information. Developed during CS50x 2023, this project aims to empower users with accurate and timely data, enabling efficient journey planning and reducing wait times.

## Key Features:

- Live Bus Tracking: Get the lowdown on upcoming buses and their estimated arrivals in real time, powered by the MTA's Bus Time API.
- User-Friendly Search: Find your stop in a flash with a search bar that offers suggestions as you type, making navigating the city streets a breeze.
- Mobile Compatibility: Take this handy tool with you wherever you go! Its optimized design ensures seamless viewing and interaction on your smartphone.

## Technical Implementation

Programming Languages and Frameworks:

- Python: Handles the back-end logic and interacts with the API.
- Flask: Provides the Python web framework for routing and app structure.
- JavaScript: Powers the dynamic front-end features and user interactions.

## Key Files:

- app.py: The main application file, where the magic happens with routing and core logic.
- templates/index.html: This is the home page template, the first thing you see when you jump onto the app.
- templates/stopinfo.html: Dive deeper into a specific stop here, where you'll find detailed information about upcoming buses.
- templates/stopnameerror.html: Looks like you typed in a stop that doesn't exist! This page guides you back on track.
- static/scripts.js: This script brings the front-end to life with dynamic features and interactions from Bootstrap.
- static/styles.css: Makes sure the app looks sleek and stylish wherever you access it.
- bus.db: A SQLite database holding all the stop information, including IDs, names, and even their location on a map.
- import_stop_ids.py: This script grabs all the stop IDs from the MTA API and pops them into the bus.db database.
- populate_stop_names.py: Fills in the blanks by adding stop names and locations to the database, including some coordinates for future versions with even more features!

## Design Choices

- Real-Time Information First: The app provides accurate, real-time bus arrival data to help you make informed decisions about your journey.
- Mobile-First Approach: Since smartphones are often the go-to for checking bus info, the app looks and works great on your mobile device.
- Intuitive Interface: The app is simple and user-friendly, focusing on clear search functionality and easy-to-read bus arrival data.

## Future Enhancements

- Auto-suggested stops: Ditch the manual search! Get nearby bus stops recommended based on your location.
- Route planning: Craft your journey with ease. Plan your entire route and map your bus trip in a future update.
- Multi-modal integration: Expand your travel options. Explore the possibility of integrating with other transit sources for a comprehensive overview of your choices.

## Conclusion

MTA Bus Tracker is an example of how technology can improve our urban experience. By delivering real-time information and prioritizing user needs, it aims to empower you to navigate the city's bustling bus system with confidence and ease. So, hop on board and experience the freedom of knowing exactly how far away your bus is!
