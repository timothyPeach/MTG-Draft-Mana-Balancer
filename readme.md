Step 1) From terminal, execute the following command: python mtg-bal.py

Step 2) In a browser, go to the link: http://127.0.0.1:4000/page

Step 3) Enjoy the MTG Draft Deck Mana Balancer!

Notes:

-first version

-The mana balancer is a rough estimate

-this mana balancer partially accounts for a concept unfamiliar to many... Consider the following example:
    //you will be running 17 lands and 23 non-lands.  15 of your non-lands are green and 8 are blue.  It seems like
    you should probably put in a little less than 2x as much Forests as Islands... but this depends... Suppose
    your cheapest creature costs 3 mana and at most, all of your spells only require one of the symbol of their color..
    (the rest of the cost is colorless cost.)  This means that you should probably split your mana close to /evenly!/
    You only need one green and one blue to cast /all/ of your cards, so you might as well ensure that you get at least
    one of each, skewing to the side that has more of that color because you have to skew to a side.  There is a tiny bit
    of math involved in my calculation which you are more than welcome to view in the .py file, but yeah that's the
    general concept behind it.
