import numpy as np

def BiomarkerNames(PivotDF):
	
    ColNames = list(PivotDF)
    # list of column names that are not going to refer to a biomarker stain
    NotBM = ['CellID', 'slide', 'region', 'epithelial', 'qc_score', 'Perimeter', 'Eccentricity', 'MajorAxisLength', 'MinorAxisLength', 'NominalPostion_X', 'NominalPosition_Y', 'Nuc_Area', 'Cyt_Area', 'Memb_Area', 'Cell_Area']
    
    BMnames = list(np.setdiff1d(ColNames,NotBM))    
    return BMnames