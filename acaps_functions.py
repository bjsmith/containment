import pandas as pd
import numpy as np

def tidy_acaps_data(source_data):
    source_data.CATEGORY = source_data.CATEGORY.str.strip()
    source_data.MEASURE = source_data.MEASURE.str.strip()
    #and because we want source_data without a sublocale to merge we're going to change NaN to a ''.
    #need to change NA to a zero-length string so that it'll list as a unique item.
    source_data.loc[:,"ADMIN_LEVEL_NAME_MERGEABLE"]=source_data.ADMIN_LEVEL_NAME
    source_data.loc[pd.isnull(source_data.ADMIN_LEVEL_NAME),"ADMIN_LEVEL_NAME_MERGEABLE"]=''

    #there's a few source data items with a date misssing - let's remove those.
    source_data = source_data.loc[source_data['DATE_IMPLEMENTED'].isnull()==False]
    
    return(source_data)


