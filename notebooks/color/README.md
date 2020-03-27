# notebooks/color
This is going to be my first project. One of the issues I run into time & time again is color settings. For the most part all of the various plotting programs have good color selection in specific instances and good enough in others. Tweaking color is a really important part of the visual, you want stark contrasts to contrast but you need to see the subtlety. I've been working with the plotly affiliated colorlover for a little bit and have had some promising results with generating colorschemes. Matplotlib also has it's own colormapping library that we will also look at. 

We need two types of color selections beyond a simple x,y scatter plot.
* an x,y scatter plot has two colors, so min_n_colors  for f(x,y) =  1
* maybe n-1 for f(x1, x2, x3, ..., xn) = n - 1
    * I don't think this is true in total but for a 2 or 3 variables you do need an indicator to differentiate one from the other
    * 4 variables becomes difficult.
        * The immediate thought I have is to turn it into an animation, and I do plan on doing some of this but animation might be more information than required in some models
        * tangent! lol

But seriously, being able to generate color palletes either by a (min, max) range, specify a significant value, or even just generate the entire color series is a timesaver and is the first step to taking control of your visual story.
I think I want to work in rgb for the time being. Both plotly and matplotlib should accept rgb colors. I've had some issues with plotly > 4.x where sankey wasn't accepting hex colors propoerly.

* interfunctionality conversion between rgb, hex, hsl, might be a useful tool
    * small support class with click args


* baseline_notebook.ipynb 

is like muscle memory for me. I could add this to the jupyter startup script but I like seeint it on the first line. I'm just setting these up for future use.
Primary Goal of documenting my visualizations strategies .01% complete!

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


