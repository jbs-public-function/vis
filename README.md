# vis
##### Who Created This Repository?

 I, James, your ```author: jbs.public.function@gmail.com```


##### To What Purpose

I keep making cool plots at work, but they tend to be one offs, and then weeks later I may want it again, and there I am, spending a good half hour rewriting completed plots.
The primary purpose of this repository is to document and develop plots of specific varieties in a variety of platforms. To make my professional life more effecient
The purpose of this repository really is a place to store my thoughts, designs, and graphs of public data.


I will likely be writing a lot of wrappers around existing plotting code. Not necessarily improving but customizing in a way 
that is meaninginful to me.


Im generally working on a conda venv on windows, currently python 3.8.
* I am curious about dipping into D3, so drop me a message if you want to evangelize.
THere's a req file in here of libraries Im using or planning on using.

##### getting started

###### I'm using a conda to manage my virtual env python=3.7
###### conda refresher

`conda create -n my_env_name python=3.7`

if you want to mess with shapefiles at all (try) and install these. I've mostly used GDAL on mac where it's a pain to install, I don't have experience with it on windows. 

```
conda install -c conda-forge gdal
conda install fiona
```

```
python -m pip install -r requirements.txt
```

###### structure

Like I said above, this repo is more about documenting my exploration of different visualization libraries than anything else.
I plan on maintaining code and notebooks in this repository I think. Im going to try and avoid and storing large sets of data in git
Hopefully I can provide links.
in the data/ directory, and a readme with instructions to myself for local postgres setup since I forget all the time.




drop a message if you have a cool dataset or vis
