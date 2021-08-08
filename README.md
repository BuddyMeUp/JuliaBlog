# JuliaBlog

### Fixes
* budget/reporting to work on user_id
* budget/reporting db.commit currently broken
* deal with all emojis

### To dos
* add user input to the db
* add deskop file to a database do change based on user_id
    * add view for adding user input
* deal with new categories coming in
* add view to determine token and budget_id per user
* split category group reporting and category reporting into separate fields
* add 50/30/20 rule analysis of spending

Logic /budgeting: 
* when selecting budgeting: 
* if a budget_id and token is saved against the current user: 
* allow to add a budget_id but otherwise present options directly 
* otherwise ask to enter the 2 info first (until Oauth can be launched)
* pop up to list all categories, separating those that don't have user_input against them and prompt an input

Logic /budgeting/reporting:

* select which reporting to see
    * pacing
    * group analysis
    * category analysis
    * line graphs
* run py script
* **?? do py results need to be added to a db ??**
* reroute to html (incl expanded base and bootstrap)

### Future functionalities - Budgeting
* category group lab - allow for changing of category groups and adding categories to different groups and save those options
* should then allow reporting to be run on these different groups in a drop down
* 50/30/20 rule calculation
* allow for filter to include or exclude certain fields in pacing/reporting files
* show tables in a nicer format

### Future Functionalities - Website
* add disussion functionality to projects/blog