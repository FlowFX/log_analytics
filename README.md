# Project: Log Analytices
Source code for the Udacity nanoprogram project [Log Analytics](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/b1bc900a-44ea-43e9-a51b-d3313705277f)


## Requirements
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

### 1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

    "Princess Shellfish Marries Prince Handsome" — 1201 views
    "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
    "Political Scandal Ends In Political Scandal" — 553 views

### 2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

    Ursula La Multa — 2304 views
    Rudolf von Treppenwitz — 1985 views
    Markoff Chaney — 1723 views
    Anonymous Contributor — 1023 views

### 3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

    July 29, 2016 — 2.5% errors

## Good coding practices
### SQL style
Each one of these questions can be answered with a single database query. Your code should get the database to do the heavy lifting by using joins, aggregations, and the where clause to extract just the information you need, doing minimal "post-processing" in the Python code itself.

In building this tool, you may find it useful to add views to the database. You are allowed and encouraged to do this! However, if you create views, make sure to put the create view commands you used into your lab's README file so your reviewer will know how to recreate them.

### Python code quality
Your code should be written with good Python style. The PEP8 style guide is an excellent standard to follow. You can do a quick check using the pep8 command-line tool.

