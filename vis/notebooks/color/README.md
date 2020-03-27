# notebooks/color
This is going to be my first project. One of the issues I run into time & time again is color settings. For the most part all of the various plotting libraries have perfect color selection in specific instances and good enough at worst. Tweaking color is a really important part of the visual story you're trying to paint and getting a handle on color is paramount. 

What kind of color scheme do you want? stark contrasts to contrast at the extreme? Subtle gradiations between near values? Is a negative number always red? Or is it good sometimes and we need to reverse the RdBu scale?

I've been working with the plotly affiliated colorlover package for a couple of weeks and have had some promising results with generating colorschemes. Matplotlib also has it's own colormapping library that we will also look at. 

We need two types of color selections beyond a simple x,y scatter plot.
* an x,y scatter plot has two colors, so min_n_colors  for f(x,y) =  1
* maybe n-1 for f(x1, x2, x3, ..., xn) = n - 1
    * I don't think this is true in total but for a 2 or 3 variables you do need an indicator to differentiate one from the other
    * 4 variables becomes difficult.
        * The immediate thought I have is to turn it into an animation, and I do plan on doing some of this but animation might be more information than required in some models
        * tangent! lol

But seriously, being able to generate color palletes either by a (min, max) range, specify a significant value, or even just generate the entire color series is a timesaver and is the first step to taking control of your visual story.
I think I want to work in rgb for the time being. Both plotly and matplotlib should accept rgb colors. I've had some issues with plotly > 4.x where sankey wasn't accepting hex colors properrly.

* interfunctionality conversion between rgb, hex, hsl, might be a useful tool
    * small support class with click args

We also need to consider what kind of color scheme do we want to genreate? Discrete steps or continuous flow? Each method has it's advantages

Discrete colors allow for a binning effect that can make distributions more clear relative to neighbors.
* a county voting choropleth map for example
   * it's discrete in the sense that it's an aggregation over that area 
   * https://brilliantmaps.com/2016-county-election-map/ is a good exapmple of this 
   * notice how it lets you get an idea at a glance geospatially where each county voted
   
Continous colors allowing for a smooth transtitions, especially amongst values of similar scale
* think a thermometer where the hotter it gets the redder it gets.
* example coming soon, I guess, lol.

let's explore
* colors-exploration.ipynb

* baseline_notebook.ipynb 

The below is a muscle memory for me. I could add this to the jupyter startup script but I like seeing the imports in the first cell, plus it's really important to rememeber what was imported and when and where within jupyter specifically but also for when our prototype gets coded up.  

```
import pandas as pd 
import numpy as np 

# matplotlib
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns
%matplotlib inline

# plotltly librariers
from plotly.offline import iplot, plot, init_notebook_mode
from plotly.subplots import make_subplots
import plotly.graph_objects as go 
init_notebook_mode(connected=True)
```


<!DOCTYPE html>
<html>
  <head>
    <title>This is a title</title>
  </head>
  <body>
    <p>Hello world!</p>
  </body>
</html>


