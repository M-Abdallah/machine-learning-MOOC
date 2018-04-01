# =============================================================================
# 
# =============================================================================

import numpy as np
import matplotlib as mplot

def gradientDescent( data ):
    
    featSize = np.shape( data )[0]
    sampleSize = np.shape( data )[1]
    feature = np.zeros( ( featSize,1 ) )
    return feature;