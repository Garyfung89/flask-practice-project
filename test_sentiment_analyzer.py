from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest 

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):

        test_1 = sentiment_analyzer('I love working with Python')
        result_1 = 'SENT_POSITIVE'
        self.assertEqual(test_1['label'], result_1)
        
        test_2 = sentiment_analyzer('I hate working with Python')
        result_2 = 'SENT_NEGATIVE'
        self.assertEqual(test_2['label'], result_2)

        test_3 = sentiment_analyzer('I am neutral on Python')
        result_3 = 'SENT_NEUTRAL'
        self.assertEqual(test_3['label'], result_3)

unittest.main()