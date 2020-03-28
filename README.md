# vis
##### Who Created This Repository?

 I, James, your ```author: jbs.public.function@gmail.com```


##### To What Purpose

I keep making cool plots at work, but they tend to be one offs, and then weeks later I may want it again, and there I am, spending a good half hour rewriting completed plots.
The primary purpose of this repository is to document and develop plots of specific varieties in a variety of platforms. Ultimately, to make my professional life more effecient.

I will likely be writing a lot of wrappers around existing plotting code. Not necessarily improving but customizing in a way that is meaninginful to me.

#### environment
I'm using conda to manage my virtual environment with python version = 3.7.7
* After working with plotly/dash for a while I am curious about dipping my toe into D3, so drop me a message if you want to evangelize.

create conda venv
* `conda create -n my_env_name python=3.7`

add conda kernel to jupyter notebook
* `python -m ipykernel install --user --name other-env --display-name "Python (other-env)"`

if you want to mess with shapefiles at all (try) and install these. I've mostly used GDAL on mac where it's a pain to install. I didn't have much experience with it on windows until now. 

```
conda install -c conda-forge gdal
conda install fiona
```

```
python -m pip install -r requirements.txt
```

install as a package
```
python -m pip install -e .
```

###### structure

* code -> once I've prototyped something I'll start adding code into this directory.
* data -> not sure if I want to keep this around. If I maintain any static datasets in this git repository they must be small and low-impact
* notebooks -> workspace for jupyter notebooks

Like I said above, this repo is more about documenting my exploration of different visualization libraries than anything else.
I will be adding a readme and doc strings to document or otherwise leave instructions to myself.




drop a message if you have a cool dataset or vis
