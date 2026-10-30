"""Genera index.html, app.js, styles.css y robots.txt en una carpeta de salida (por defecto temporal; nunca pisa el repo sin pedirlo).
Uso: python3 berawa/build/run_stage.py [--out=DIR]"""
import sys,tempfile
from _rutas import ROOT
import albergue_san_nicolas_logrono_build as C
from content_albergue_san_nicolas_logrono import D,ALTS,IMGS
from knowledge_albergue_san_nicolas_logrono import KB
if __name__=='__main__':
    o=[x[6:] for x in sys.argv[1:] if x.startswith('--out=')]
    out=o[0] if o else tempfile.mkdtemp(prefix='demo-build-')
    C.build(D,KB,out,IMGS,ALTS,{'kb','a11y','sec','v1'}); print('built ->',out)
