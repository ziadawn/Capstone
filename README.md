Your proposal must be in a markdown .md file more info

Your proposal must set specific and attainable goals

Your proposal must cover all major topics we've covered

Your proposal must include the sections below

**(working) NAME  -- molecule**

===========================================

**PROJECT OVERVIEW**

What are the major features of your web application?

    Private chat program that lets users set up groups, easily send group or duplicate or individual messages.
    Easy options to delete messages.
    Private, not searchable. You set up your own groups and cannot message outside of it.

What problem is it attempting to solve?

    Simple, streamlined private chat platform to handle groups and individuals

What libraries or frameworks will you use?

===========================================

**FUNCTIONALITY**

Walk through the application from the user's perspective.

    Users create accounts
        They can set up groups
        Add friends by username, and tag to groups as they add friends (cannot search for people)
        Friends are sent notifications, to confirm before you can chat
        Log in to send messages


What will they see on each page? What can they input and click and see?

    Log in/create account page
    Landing page lists groups, messages, edit account info, add new friends
        Message page has lists of messages. Messages can be easily archived or deleted. Can delete on both ends.
        Edit account info page to change password, update contact info, profile picture, etc

How will their actions correspond to events on the back-end?

    Searching for friends checks db for existing accounts and returns matches 
    Lgoging in accesses Djano's user model
    Messages do a one-to-many or one-to-one route to get sent to users


===========================================

**DATA MODEL**

    Users
    Group tags
    Messages (read, unread)

===========================================

**SCHEDULE**

To do:

    Week 1: 
        Set up repository
        Start new Django project
        Start app, get basics set up
       
    Week 2:
        Get basic HTML laid out
        Set up test accounts
        
    Break:
        Play with CSS
    
    Week 3:
        Polish, troubleshoot, etc


Here you'll want to come up with some (very rough) estimates of the timeframe for each section.
State specifically which steps you'll take in the implementation.
This section should also include work you're planning to do after the capstone is finished.