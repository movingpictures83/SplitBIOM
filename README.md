# SplitBIOM
# Language: Python
# Input: PY (contents of BIOM file)
# Output: PREFIX 
# Tested with: PluMA 1.1, Python 3.6


Split a BIOM file into multiple BIOM files, one for each phylogenetic tree level.

The BIOM file should be provided as a Python module, which will then be imported by the plugin.
See the example.  It should be set equal to "self.myBIOM".

The plugin will then split this data into taxonomic classifications, and output one BIOM
file per classification level with the user-specified output prefix (i.e. prefix.kingdom.biom,
prefix.phylum.biom, etc.)
