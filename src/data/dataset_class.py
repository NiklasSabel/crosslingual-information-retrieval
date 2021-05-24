import numpy as np
import pandas as pd


class DataSet:
    """ Class for creating a modeling dataset based on the preprocessed europarl data.

    Attributes:
        preprocessed_dataframe (dataframe): Preprocessed dataframe from source and target
        preprocessed_source (dataframe): Preprocessed dataframe for source sentences
        preprocessed_target (dataframe): Preprocessed dataframe for target sentences
        dataset(dataframe): Preprocessed dataset with translated and random parallel sentences
    """
    def __init__(self, preprocessed_class):
        """ Initialize class by importing data from preprocessed class

        Args:
            preprocessed_class (class): Path of the europarl source dataset
        """
        self.preprocessed_dataframe = preprocessed_class.preprocessed_dataframe
        self.preprocessed_source = preprocessed_class.preprocessed_source
        self.preprocessed_target = preprocessed_class.preprocessed_target
        self.dataset = pd.DataFrame
        self.testset = pd.DataFrame()
        self.query = pd.DataFrame()
        self.documents = pd.DataFrame()
        self.feature_list = [
            'number_punctuations_total', 'number_words',
            'number_unique_words', 'number_!', 'number_"',
            'number_#', 'number_$', 'number_%',
            'number_&', "number_'", 'number_(',
            'number_)', 'number_*', 'number_+',
            'number_,', 'number_-', 'number_.',
            'number_/', 'number_:', 'number_;',
            'number_<', 'number_=', 'number_>',
            'number_?', 'number_@', 'number_[',
            "number_\\", "number_]", "number_^",
            'number__', 'number_`', 'number_{',
            'number_|', 'number_}', 'number_~',
            'number_characters', 'characters_avg',
            'number_ADJ', 'number_ADP',
            'number_ADV', 'number_AUX', 'number_CONJ',
            'number_CCONJ', 'number_DET', 'number_INTJ',
            'number_NOUN', 'number_NUM', 'number_PRT',
            'number_PRON', 'number_PROPN', 'number_SCONJ',
            'number_SYM', 'number_VERB', 'number_X',
            'number_Pres', 'number_Past', 'number_',
            'score_polarity', 'score_subjectivity',
            'number_stopwords']

    def get_sample(self, n):
        """ Method to generate a sample set of 2n with n correct examples and n wrong examples

          Args:
              n (int): Number of correct and incorrect sentence pairs
          """
        random_sample_right = self.preprocessed_dataframe.sample(n).reset_index(drop=True)
        random_sample_wrong = pd.concat([self.preprocessed_source.sample(n).reset_index(drop=True),
                                         self.preprocessed_target.sample(n).reset_index(drop=True)],
                                        axis=1)
        random_sample_wrong["Translation"] = np.zeros((int(random_sample_wrong.shape[0]), 1),
                                                      dtype=np.int8)

        self.dataset = pd.concat([random_sample_right, random_sample_wrong]).reset_index(drop=True)
