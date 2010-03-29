last.fm-geo-lists
====================
A python script for creating HTML lists from last.gm geo API.

Usage
--------------
Define the constants at top of script:

    API_KEY = 'foo'
    
Then run:
    
    python generate_lists.py 'new york' 'united states' 'geo.getmetroartistchart'
   
Limitations
----------------
This simply generates flat HTML snippets and is meant to be consumed by CMS on CRON. 

Licence
-----------
Licensed with the [WTFPL](http://sam.zoy.org/wtfpl/)