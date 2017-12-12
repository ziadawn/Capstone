Your proposal must be in a markdown .md file more info
Your proposal must set specific and attainable goals
Your proposal must cover all major topics we've covered
Your proposal must include the sections below

NAME  -- ?

===========================================

PROJECT OVERVIEW

What are the major features of your web application?

    Users enter a few keywords, and
    A program that helps users put together an adventure itinerary, scavenger-hunt style.
    They enter a starting point (or it connects to GPS?) and they go to things, then it gives the next spot.


What problem is it attempting to solve?

    This is to help them discover new adventures in their city, plan dates, etc, from one unified platform.


What libraries or frameworks will you use?

    Investigating jQuery, React, and maybe Vue

===========================================

FUNCTIONALITY

Walk through the application from the user's perspective.

    Users go to get ideas for dates/adventures. They can search by date, by keyword, or by other parameters.
    Some possible options:
        restrictions? (no meat/gluten/whatever, under 21, no alcohol, indoors only, no money, how traveling, etc)
        length of time
        indoor/outdoor (factor in weather api?)
        cost/budget (price per person?)

What will they see on each page? What can they input and click and see?

    (Pages in no specific order)
    Page 1: Intro page, explanation, button to "plan my adventure!"
    Page 2: Enter criteria, possibly with drop down menues. Button to enter info. Pop-up or filler text of planning/searching
    Page 3: Display of events. Once selected, option to find food/treats nearby, w/search criteria
    Page 4: Option to send info to phone, to email, to save for later (sign up for account), display
    Maybe:
    Page 5: create account (name, user name, pw, email, phone, save preferences, saved dates. Connect users?)

How will their actions correspond to events on the back-end?

    Page 1: redirect
    Page 2: filters, connect to db/various db
    Page 3: compile/append stuff that can then be bundled and shared/sent/saved
    Page 4: write/save into to user db

===========================================

DATA MODEL

Users

Preferences: Dietary Preferences, Alcohol Preferences,Money Preferences, Areas of Town, Indoor/Outdoor/Weather

API: yelp, weather, other?

===========================================

SCHEDULE

Week 1:

    Research APIs, sign up for APIs
    Create repository, create Django file, set up basic Django pages
    Choose name



Here you'll want to come up with some (very rough) estimates of the timeframe for each section.
State specifically which steps you'll take in the implementation.
This section should also include work you're planning to do after the capstone is finished.