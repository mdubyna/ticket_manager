# Ticket manager

## How to run

```
 https://github.com/mdubyna/ticket_manager.git
 cd ticket_manager
 python -m venv venv
 venv\Scripts\activate
 pip install -r requirements.txt
 flask db init
 flask db migrate
 flask db upgrade
 python -m run
```

## How to get access:

You have already created 3 users(you can create new users login -> register):

1) Admin creates new tickets and assigns a tickets to groups, creates and manages groups, manages user roles
- login: admin@admin.com
- password: password
2) Manager manages tickets in a certain group, can assign a ticket to a certain analyst or analysts
- login: manager@manager.com
- password: password
3) The analyst works with the tickets that are assigned to him
- login: analyst@analyst.com
- password: password