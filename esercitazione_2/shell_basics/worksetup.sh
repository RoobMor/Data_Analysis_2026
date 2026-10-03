#!/usr/bin/env bash

#ATTENZIONE: Lanciare questo script con:   source worksetup.sh
#            Se usassi "./worksetup.sh", tutto il prodotto dello script verrebbe annullato.

BASE=~/Desktop/roby/physics/data_analysis/esercitazioni/Data_Analysis_2026/esercitazione_2/shell_basics

cd "$BASE" || return 1 # se per qualche motivo dovesse rompersi, return 1 non fa chiudere il terminale

mkdir -p "${USER}_workspace"
cd "${USER}_workspace" || return 1

source /home/roberto/miniconda3/envs/rootenv/bin/thisroot.sh
# ATTENZIONE: si tratta solo di un esercizio.
# il modo corretto di avviare root è attivare tutto l'environment in cui è installato (ergo: conda activate rootenv).
# altrimenti si attiverebbe root in uno stato "ibrido".
