
**NAME  -- molecule**

===========================================

**SCHEDULE**

Done:

    Set up repository
    Set up Django project
    Set up Dgano app, link basic pages 
    Create superuser
    Get basic login set up, clean up pages


To do:

    Done! _Week 1: 
        Set up repository
        Start new Django project
        Start app, get basics set up_
       
    Week 2:
        Get basic HTML laid out
        Set up test accounts
        
        
    Break:
        Play with CSS
    
    Week 3:
        Polish, troubleshoot, etc
        

===========================================

**PROJECT OVERVIEW**

What are the major features of your web application?

    Private chat program that lets users set up groups, easily send group or duplicate or individual messages.
    Easy options to delete messages.
    Private, not searchable. You set up your own groups and cannot message outside of it.

What problem is it attempting to solve?

    Simple, streamlined private chat platform to handle groups and individuals

What libraries or frameworks will you use?

    Considering using Twilio API chat and/or SMS?  


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
