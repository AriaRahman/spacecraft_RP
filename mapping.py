

from pathlib import Path

DATA_ROOT = Path("DATA")

CLASS_MAP = {
    'Cheops':          0,
    'LisaPathfinder':  1,
    'ObservationSat1': 2,
    'Proba2':          3,
    'Proba3':          4,
    'Proba3ocs':       5,
    'Smart1':          6,
    'Soho':            7,
    'VenusExpress':    8,
    'XMM Newton':      9
}

INV_CLASS_MAP = {v: k for k, v in CLASS_MAP.items()}
NUM_CLASSES   = len(CLASS_MAP)  

NUM_SEG_CLASSES = 6  
IMG_SIZE      = 256