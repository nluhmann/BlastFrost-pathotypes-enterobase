#input parameter/files
#1) graph file (gfa)
#2) graph colours file (bfg_colours)
#3) EnteroBase metadata file including assembly field

#assumption: query folder in same directory, file names

#query graph
echo "Query eae"
~/my_software/BlastFrost/build/BlastFrost -g $1 -f $2 -t 8 -d 1 -q query/eae_EHEC_EPEC.fasta -o eae_d1 -s 4.5

echo "Query LT"
~/my_software/BlastFrost/build/BlastFrost -g $1 -f $2 -t 8 -d 1 -q query/LT.fasta -o LT_d1 -s 4.5

echo "Query ST"
~/my_software/BlastFrost/build/BlastFrost -g $1 -f $2 -t 8 -d 1 -q query/ST.fasta -o ST_d1 -s 4.5

echo "Query stx1 and stx2"
~/my_software/BlastFrost/build/BlastFrost -g $1 -f $2 -t 8 -d 1 -q query/stx_rep.fasta -o stx_d1 -s 4.5

echo "Query pINV invasion region"
~/my_software/BlastFrost/build/BlastFrost -g $1 -f $2 -t 8 -d 1 -q query/pINV_invasion_region.fasta -o pinv_d1 -s 4.5

echo "Query ipaH"
~/my_software/BlastFrost/build/BlastFrost -g $1 -f $2 -t 8 -d 1 -q query/ipaH_all.fasta -o ipaH_d1 -s 4.5

echo "Process results..."
cut -f 2 eae_d1_eae_EHEC_EPEC.fasta.search | sort | uniq -c |  sed 's/^ *//g' > eae_d1_genomes
python format_genome_list.py eae_d1_genomes $3

cut -f 2 LT_d1_LT.fasta.search | sort | uniq -c |  sed 's/^ *//g' > LT_d1_genomes
python format_genome_list.py LT_d1_genomes $3

cut -f 2 ST_d1_ST.fasta.search | sort | uniq -c |  sed 's/^ *//g' > ST_d1_genomes
python format_genome_list.py ST_d1_genomes $3

cut -f 2 stx_d1_stx_rep.fasta.search | sort | uniq -c |  sed 's/^ *//g' > stx_d1_genomes
python format_genome_list.py stx_d1_genomes $3

cut -f 2 pinv_d1_pINV_invasion_region.fasta.search | sort | uniq -c |  sed 's/^ *//g' > pINV_d1_genomes
python format_genome_list.py pINV_d1_genomes $3

cut -f 2 ipaH_d1_ipaH_all.fasta.search | sort | uniq -c |  sed 's/^ *//g' > ipaH_d1_genomes
python format_genome_list.py ipaH_d1_genomes $3


python combine_results.py $3 > BlastFrost_pathovars
