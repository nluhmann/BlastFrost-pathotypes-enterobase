# BlastFrost-pathotypes-enterobase

Scripts to call Escherichia pathotypes by determining the presence or absence of specific marker genes using BlastFrost. These scripts have been used to determine pathotypes for the whole EnteroBase Escherichia database (Nov20) indexed as a Bifrost graph. Currently, the following pathotypes are differentiated: EHEC,EPEC,STEC,ETEC,EIEC,(Shigella).
Method details to be published.

## HowTo

### Build a Bifrost graph
Required as input: text file containing file location of genomes assemblies to be indexed, one file per line
```
Bifrost build -v -k 31 -c -t 8 -o <outprefix> -r <file list> > logfile
```
### Search the Bifrost graph

```
./determine_pathotypes.sh <Bifrost graph file> <Bifrost graph colours> <EnteroBase metadata file>
```

The script will query the Bifrost graph for all genes provided in the folder <query> and combine the search result to differentiate pathotypes. See file metadata_example.tsv for an examplary EnteroBase metadata file. The output file will list all EnteroBase barcodes in the metadata file and the determined pathotype, or "-" if not pathotype has been identified.
In order to differentiate EIECs and Shigella, EnteroBase species information is copied. We note that this can potentially contain errors.
