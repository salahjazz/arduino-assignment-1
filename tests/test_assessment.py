import unittest
from assessment import classify_score, generate_recommendations_with_feedback

class TestAssessment(unittest.TestCase):

    def test_classify_score(self):
        self.assertEqual(classify_score(5), "مبتدئ")
        self.assertEqual(classify_score(12), "متوسط")
        self.assertEqual(classify_score(18), "متقدم")

    def test_generate_recommendations(self):
        scores = {
            'درجة موضوع 1': 15,
            'درجة موضوع 2': 17,
            'درجة موضوع 3': 8,
            'درجة موضوع 4': 19,
            'درجة موضوع 5': 14
        }
        result = generate_recommendations_with_feedback(scores)
        self.assertIn('التقييم العام', result)
        self.assertIn('تفاصيل المواضيع', result)
        self.assertEqual(result['التقييم العام']['المستوى'], 'متوسط')

if __name__ == '__main__':
    unittest.main()
Add unit tests for assessment
