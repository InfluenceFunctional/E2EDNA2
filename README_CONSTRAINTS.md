# Implementing constraints
### Background

Sometimes it is necessary to implement angular constraints for a peptide, in order to conserve its geometric shape. 
This is particularly important for docking simulations, where a certain ligand will only bind to a peptide if its in a certain conformation.

OpenDNA now allows you to perform and set custom angular constraints. Here's how.

### Setting up the angular constraints

The file "backbone_dihedrals.csv" will be used as input in order to figure out which amino acids need to be constrained.
If we take a look at the file as it is currently, using our favorite text editor, we can see that the following is written in it:

```
residue_num,phi,psi
```

This is the template format that you should follow when inputting the angles into this .csv file.
Please do not remove this first line. Also, please do not change the name of this .csv file.

The strength of the angular constraint can be set with the ```params['peptide backbone constraint constant'] = YOUR_INTEGER_VALUE``` statement in ```main.py```.
It is set at ```10,000``` currently because that was determined to be the best value for constraining a peptide, when all other parameters are held constant.

### The variables
```residue_num``` is the residue number. It starts from 0, to ensure it matches with Python's (and OpenMM's) indexing style. 
In other words, if you need to put a constraint on amino acid 3 for instance (as it appears in the pdb), then you would write ```2``` for the ```residue_num```.

```phi``` is the angle value that you want to set for phi. Likewise for ```psi```. 
Support for an ```omega``` variable does not exist currently.

### An example of a valid input
The following is an example of a valid input for constraining phi and psi values for amino acids 2 and 6 in an arbitrary peptide:
```
residue_num,phi,psi
1,-90,-110
5,-85,-120
```

### Common errors that might occur
Assuming the above is followed, some common errors that might show up include:
```Particle Coordinate is nan```

This means the simulation exploded, due to the time step being too large to properly calculate trajectories using the current
```params['peptide backbone constraint constant']``` value. An easy way to rectify this is to simply make ```params['time step']``` shorter.
It is currently set at 2.0 fs because that was the best time-step for the current ```params['peptide backbone constraint constant']``` value.