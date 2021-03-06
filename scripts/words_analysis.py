"""Run analysis on collected words data."""

from lisc.data import ArticlesAll
from lisc.utils import SCDB, load_object
from lisc.utils.io import load_txt_file

from lisc.plts.words import plot_years, plot_wordcloud

###################################################################################################
###################################################################################################

# Set data words object to load
TERM_DIR = '../terms'
DB_NAME = '../data'
F_NAME = 'words_erps'

# Set the year range for plotting
YEAR_RANGE = [None, 2020]

# Set the file format for saved out plots
PLT_EXT = '.svg'   # '.svg', '.png'

###################################################################################################
###################################################################################################

def main():

    print('\n\n ANALYZING WORDS DATA \n\n')

    db = SCDB(DB_NAME)

    words = load_object(F_NAME, db)
    exclusions = load_txt_file('analysis_exclusions.txt', TERM_DIR, split_elements=False)

    for erp in words.labels:

        print('Analyzing ', erp, 'data')

        # Load data for the current term
        words[erp].load(directory=db)

        # Aggregate data together across all articles
        erp_data = ArticlesAll(words[erp], exclusions=exclusions)

        # Create and save summary
        erp_data.create_summary()
        erp_data.save_summary(directory=db)

        # Create and save wordcloud figure
        plot_wordcloud(erp_data.words, 20, transparent=True,
                       save_fig=True, f_name='wc/' + erp + PLT_EXT, directory=db, close=True)

        # Create and save years figure
        plot_years(erp_data.years, year_range=YEAR_RANGE, transparent=True,
                   save_fig=True, f_name='years/' + erp + PLT_EXT, directory=db, close=True)

        # Clear the loaded data for the current term
        words[erp].clear()

    print('\n\n FINISHED ANALYZING WORDS DATA \n\n')


if __name__ == "__main__":
    main()
