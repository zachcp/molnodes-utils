# Molnodes

Explorations in Blender + Molecular Nodes.

Motivation:

  - Molecular Nodes is awesome but I'd like to do a bitmore with code.
  - I want to programatically build up more complicated VIZ on top of Molecular Nodes.
  - idea 1: script to load a PDB, split by style and apply a color scheme or maybe make the ligand glow
  - idea 2: take a PDB and an MSA and make a video/viz where conservation is moving sidechaines
  - idea 3: create an interatomic nodetype that can be used to express inter-atomic or inter-residue connections for things like NMR Noesy, evolutionary coupling relationships etc.
  - main need: be able to create Nodes programatically and connect them together with code.


Approach:

  - load all deps and the environment in code. used pixi for its awesomeness.
  - try to convert all of the MN nodes to code with the idea that that opens up CI/CD etc.
  - create some simple end-to-end viz that can be invoked as a pixi task
  - create some more complicated viz that links nodes together.


## Handy Scripts

```sh

## Runs Blender with an open basilisp repl
pixi run repl

## Build Molecular Node Nodes
# this will convert each GeometryNode class found in assets/MN_data_file_4.2.blend to a pythonclass
pixi run convert-MN
# create a python wheel of MolecularNodes nodes
pixi run build-wheel

# Example Script
pixi run python scripts/blendersynth/04_molnodes.py
```


## WIP Example

The wiggle in this gif is due to tow of Brady's Molecular Nodes - [animate value](https://bradyajohnston.github.io/MolecularNodes/nodes/animate.html#animate-value) and [res wiggle](https://bradyajohnston.github.io/MolecularNodes/nodes/animate.html#res-wiggle) - whicha re making this
protein wiggle based on B-factor. We could use the B-factor field to hold something else - e.g. sequence conservation in an MSA, etc.

Current workflow:

1. Load up the Network Editor in Molecular Nodes
2. When things look good, save the NodeGroup as a python class.
3. Put the class in its own package, `usernodes` which depends on `molnodes` and `molecularnodes`.
4. Load in my protein and swap Brady's Nodetree for me own.
5. Use any tool - I am trying [BlenderSynth](https://www.ollieboyne.com/BlenderSynth/) - to stage and capture the images.

Once this is in place, I can make a cli rendered for any protein of interest.

![wiggle](outputs/animation/prot_01.gif)
