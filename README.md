# NeverAgainColleges

An up-to-date resource of universities that are supporting #NeverAgain demonstrators against disciplinary actions.


[Website is live here!](http://www.NeverAgainColleges.com)


## About

NeverAgainColleges.com is a resource that high school students can use to see if the universities they have applied to have made statements saying they will not rescind admittances if a student is disciplined by their high school for peacefully demonstrating. Read more on the [About](http://www.NeverAgainColleges.com/about.html) section.

## Getting Started

Want to run this site locally and start contributing? Run these commands!

```bash

git clone https://github.com/asg017/NeverAgainColleges.git
cd NeverAgainColleges/
python -m SimpleHTTPServer

```

The main page can then by found at http://localhost:8000



## Quick Overview of Tools Used

The site itself is hosted on Github Pages. Data for the list of universities 
is on [this Google Sheet](https://docs.google.com/spreadsheets/d/1J2R1ABpUoFSC3USeOOv5kpmyA7Ilw1D3aFinc1pW0yg) 
(an old Google Sheet REST API is used to access the data client-side). 
Semantic UI is used to make it pretty.

List of other Javascript libraries used:

- [Semantic UI](https://github.com/Semantic-Org/Semantic-UI) for modals, checkboxes
- [Handlebars.js](https://github.com/wycats/handlebars.js/) for templating client-side
- [mark.js](https://github.com/julmot/mark.js/) for search bar functionality
- [clipboard.js](https://github.com/zenorocha/clipboard.js/) for copy/pasting


## To-Do

- [ ] Make list sortable/add categories (UC's, Ivy's, etc.)
- [ ] Add way to add statements in question(LSU,UChicago, etc.)
- [ ] Add City/State/Size data to Spreadsheet
- [ ] Add url params to specify college,  ?college=3, ?college=UCSanDiego

## Contributors

[Alex Garcia](https://github.com/asg017) - Main Author

[Isaac Diamond](https://github.com/isaacd9) - Active contributor

[Joy Chen](https://github.com/joyhchen) - Active contributor
