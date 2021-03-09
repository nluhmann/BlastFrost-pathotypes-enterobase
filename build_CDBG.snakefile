


rule all:
     input:
        "coli.gfa"


	

rule build_cDBG:
     input:
        "assemblies.txt"
     output:
        "coli.gfa"
     threads: 24
     benchmark:
         "benchmarks/Bifrost/colored.tsv"
     log:
         "logs/Bifrost/colored.log"
     message:
          "Run Bifrost with {threads} threads on all assemblies. See logfile {log}."
     shell:
         "Bifrost build -v -k 31 -c -t {threads} -o coli -r {input} > {log}"


