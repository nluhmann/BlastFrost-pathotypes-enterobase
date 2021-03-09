import sys
import collections


genomes = collections.defaultdict(list)

species = {}
all_genomes = []

f = open(sys.argv[1],"r")
for line in f:
    if not line.startswith("Uberstrain"):
        arr = line.rstrip("\n").split("\t")
        barcode = arr[34]
        if not arr[22] == "":
            species[barcode] = arr[22]
        all_genomes.append(barcode)

f.close()

f = open("ipaH_d1_genomes_format","r")
for line in f:
    if not line.startswith("Barcode"):
        arr = line.rstrip("\n").split("\t")
        genomes[arr[0]].append("ipaH")
f.close()


f = open("eae_d1_genomes_format","r")
for line in f:
    if not line.startswith("Barcode"):
        arr = line.rstrip("\n").split("\t")
        barcode = arr[0]
        genomes[barcode].append("eae")
f.close()


f = open("LT_d1_genomes_format","r")
for line in f:
    if not line.startswith("Barcode"):
        arr = line.rstrip("\n").split("\t")
        genomes[arr[0]].append("LT")
f.close()



f = open("ST_d1_genomes_format","r")
for line in f:
    if not line.startswith("Barcode"):
        arr = line.rstrip("\n").split("\t")
        genomes[arr[0]].append("ST")
f.close()


f = open("pINV_d1_genomes_format","r")
for line in f:
    if not line.startswith("Barcode"):
        arr = line.rstrip("\n").split("\t")
        if int(arr[2]) >= 10:
            genomes[arr[0]].append("pINV")
f.close()

f = open("stx_d1_genomes_format","r")
for line in f:
    if not line.startswith("Barcode"):
        arr = line.rstrip("\n").split("\t")
        genomes[arr[0]].append("stx")
f.close()



for genome in all_genomes:
    if not genome in genomes:
	print genome+"\t-"
	continue
    types = genomes[genome]
    found = False
    if genome in species and "Escherichia" in species[genome]:
        if 'eae' in types:
            if 'stx' in types and len(types) == 2:
                print genome+"\t"+"E. coli - EHEC (eae,stx)"
                found = True
            elif len(types) == 1:
                print genome+"\t"+"E. coli - EPEC (eae)"
                found = True
        if not found and "ipaH" in types:
            if "pINV" in types:
                print genome+"\t"+"E. coli - EIEC (ipaH,pINV)"
                found = True
            else:
                print genome+"\t"+"E. coli - EIEC (ipaH)"
                found = True
        if not found and ("LT" in types or "ST" in types):
            print genome+"\t"+"E. coli - ETEC ("+",".join(types)+")"
            found = True
        if not found and "stx" in types:
            print genome+"\t"+"E. coli - STEC (stx)"
            found = True
        elif not found:
            print genome+"\t"+"E. coli - "+",".join(types)
    elif genome in species and "Shigella" in species[genome]:
        if "ipaH" in types:
            if "pINV" in types and len(types) == 2:
                print genome+"\t"+species[genome]+" - ipaH,pINV"
                found = True
            elif len(types) == 1:
                print genome+"\t"+species[genome]+" - ipaH"
                found = True
            else:
                print genome+"\t"+species[genome]+" - "+",".join(types)
                found = True
        elif not found:
            print genome+"\t"+species[genome]+" - "+",".join(types)+")"
            found = True
    elif genome in species:
        print genome+"\t"+species[genome]+" - "+",".join(types)
        found = True
    else:
        print genome+"\t"+" - "+",".join(types)
