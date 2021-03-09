import sys


enterobase_file = sys.argv[2]
ass_barcode = {}

f = open(enterobase_file,"r")
for line in f:
    arr = line.rstrip("\n").split("\t")
    barcode = arr[34]
    ass = arr[43]
    ass_barcode[ass] = barcode
f.close()



f = open(sys.argv[1],"r")
o = open(sys.argv[1]+"_format","w")

o.write("Barcode\tAssembly barcode\tNUM\n")
for line in f:
    arr = line.rstrip("\n").split(" ")
    barcode = arr[1].split("/")[-1].split(".")[0]
    if "genomic" in barcode or "assembly" in barcode:
        bar = barcode.split("_")
        barcode = "_".join(bar[0:3])
    if barcode in ass_barcode:
        o.write(ass_barcode[barcode]+"\t"+barcode+"\t"+arr[0]+"\n")
    else:
        print "missing conversion: "+barcode


f.close()
o.close()
