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
- [LazyLoad.js](https://github.com/verlok/lazyload) for picture lazy loading


## HELP NEEDED


Want to help out with NeverAgainColleges.com? Here's some dev work that is needed!

### Front-End

Here are some features on the site that would need some help:

- Adding [map](http://leafletjs.com/) of US, colored markers on schoools that have/haven't put statements
- Making list sortable/filterable
- Adding "Press" section
- Include a uni's statement on site

Want to start one of these things? Create an Issue above, or [DM me on twitter](https://twitter.com/asg_027)!


### Data

There is currently the `/scripts/` directory that hosts some rudimentary scripts to supplement data for NeverAgainColleges.com.


`na_colleges.py` fills a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)
of the colleges that appear on NeverAgainColleges.com. `nacac.py` fills a DataFrame of colleges that appear on 
[NACAC](https://www.nacacnet.org/news--publications/college-and-university-update-on-disciplinary-actions/)'s list.


Both Dataframe have different data and different columns names, so be sure to get affiliated with what they both return. `compare.py` contains a sample of how to retrive both DataFrames.


Some projects with this:

- Use [College ScoreCard API](https://collegescorecard.ed.gov/data/documentation/) to get city/state/size/lat/long for each college.
- Program that returns a list of colleges that appear on NACAC's list but not NeverAgainColleges.com.
- Program that finds the most popular tweets that contains their statements
- Analysis on size/influence of these admission office's twitter accounts
- 

If you want to start one of these, Create an Issue or [DM me on twitter](https://twitter.com/asg_027)!

## To-Do

- [ ] Make list sortable/add categories (UC's, Ivy's, etc.) [HIGH]
- [ ] Add City/State/Size data to Spreadsheet [MED]
- [ ] Add url params to specify college,  ?college=3, ?college=UCSanDiego [LOW]
- [ ] Add Press space, place where NeverAgainColleges.com has been cited in the press [LOW]
- [ ] Include pagination to list [LOW]
- [x] ~~Use lazy loading for photos [HIGH]~~
- [x] ~~When empty search, show message enouraging to contact me [HIGH]~~
- [x] ~~Add way to add statements in question(LSU,UChicago, etc.) [HIGH]~~


## Contributors

[Alex Garcia](https://github.com/asg017) - Main Author

[Isaac Diamond](https://github.com/isaacd9) - Active contributor

[Joy Chen](https://github.com/joyhchen) - Active contributor
