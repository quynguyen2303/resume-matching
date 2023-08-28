'''
Write unit tests for the functions in the resume-matching module.
'''

import unittest
import logging
import os
import sys
import json
import re

import core_matching
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'resume-matching'))

class TestCoreMatching(unittest.TestCase):
    def setUp(self):
        self.job_title = 'Software Engineer'
        self.resume_title = 'Software Engineer'
        self.must_have_skills = ['Python', 'C++', 'C', 'C#', 'JavaScript', 'SQL', 'HTML', 'CSS', 'PHP']
        self.job_skills = ['Python', 'Java', 'C++', 'C', 'C#', 'JavaScript', 'SQL', 'HTML', 'CSS', 'PHP']
        self.resume_skills = ['Python', 'Java', 'C++', 'C', 'C#', 'JavaScript', 'SQL', 'HTML', 'CSS', 'PHP']

    # def test_get_job_title_score(self):
    #     self.assertEqual(core_matching.get_job_title_score(self.job_title, self.resume_title), 1)

    # def test_get_job_title_score_bert(self):
    #     self.assertEqual(core_matching.get_job_title_score_bert(self.job_title, self.resume_title), 0)

    # def test_get_technical_skills_score(self):
    #     self.assertEqual(core_matching.get_technical_skills_score(self.must_have_skills, self.job_skills, self.resume_skills), 1)

    # # Additional test cases
    # def test_mismatched_job_title_score(self):
    #     mismatched_resume_title = 'Data Scientist'
    #     self.assertNotEqual(core_matching.get_job_title_score(self.job_title, mismatched_resume_title), 1)

    # def test_missing_must_have_skills_score(self):
    #     missing_must_have_skills = ['Java']
    #     self.assertNotEqual(core_matching.get_technical_skills_score(self.must_have_skills, self.job_skills, missing_must_have_skills), 1)

    # def test_incomplete_resume_skills_score(self):
    #     incomplete_resume_skills = ['Python', 'Java', 'C++', 'C', 'JavaScript']
    #     self.assertNotEqual(core_matching.get_technical_skills_score(self.must_have_skills, self.job_skills, incomplete_resume_skills), 1)

    # def test_additional_resume_skills_score(self):
    #     additional_resume_skills = ['Python', 'Java', 'C++', 'C', 'C#', 'JavaScript', 'SQL', 'HTML', 'CSS', 'PHP', 'R', 'Ruby']
    #     self.assertEqual(core_matching.get_technical_skills_score(self.must_have_skills, self.job_skills, additional_resume_skills), 1)

    def test_different_job_title_bert(self):
        different_resume_title = 'Backend Developer'
        # Assuming BERT score returns a float value between 0 and 1. For simplicity, I am just assuming a score greater than 0.5 as matching.
        self.assertTrue(core_matching.get_job_title_score_bert(self.job_title, different_resume_title) > 0.5)

    # def test_partial_match_resume_skills(self):
    #     partial_match_resume_skills = ['Python', 'Java', 'C++', 'C', 'JavaScript', 'SQL', 'HTML', 'CSS']
    #     score = core_matching.get_technical_skills_score(self.must_have_skills, self.job_skills, partial_match_resume_skills)
    #     self.assertTrue(0.5 <= score < 1)

def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()

