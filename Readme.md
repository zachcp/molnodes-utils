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


```sh

## Examples of Sending Code to the Blender Repl
# in terminal 1
pixi run launch-blender-live

# in terminal 2
pixi run send-to-blender scripts/00_script.py
pixi run send-to-blender scripts/01_script.py
pixi run send-to-blender scripts/examples/city-builder.py


# alternative using basilsp
# this will create an nrepl server to your open Blender
pixi run launch-blender-basilisp

## Build Molecular Node Nodes
# this will convert each GeometryNode class found in assets/MN_data_file_4.2.blend to a pythonclass
pixi run convert-MN
# create a python wheel of MolecularNodes nodes
pixi run build-wheel
```
