"""Analysis functions for the ERPscanr project."""

import numpy as np

###################################################################################################
###################################################################################################

def get_time_associations(counts):
    """Get time associations from canonically named ERP components."""

    time_associations = []

    for erp_ind, erp in enumerate(counts.terms['A'].labels):

        # List is: [word, P or N, latency]
        temp  = [None, None, None]

        # Get P/N & latency for ERPs with naming convention
        if erp[1:].isdigit():

            # Get P or N
            if erp[0] == 'P':
                temp[1] = 'P'
            elif erp[0] == 'N':
                temp[1] = 'N'

            # Get latency
            temp[2] = int(erp[1:])

            # Get association
            term_ind = np.argmax(counts.score[erp_ind, :])
            temp[0] = counts.terms['B'].terms[term_ind][0]

            # Collect ERP data
            time_associations.append(temp)

    return time_associations
