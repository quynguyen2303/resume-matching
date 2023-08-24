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
        self.must_have_skills = ['Python', 'Java', 'C++', 'C', 'C#', 'JavaScript', 'SQL', 'HTML', 'CSS', 'PHP']
        self.job_skills = ['Python', 'Java', 'C++', 'C', 'C#', 'JavaScript', 'SQL', 'HTML', 'CSS', 'PHP']
        self.resume_skills = ['Python', 'Java', 'C++', 'C', 'C#', 'JavaScript', 'SQL', 'HTML', 'CSS', 'PHP']

    def test_get_job_title_score(self):
        self.assertEqual(core_matching.get_job_title_score(self.job_title, self.resume_title), 1)

    def test_get_job_title_score_bert(self):
        self.assertEqual(core_matching.get_job_title_score_bert(self.job_title, self.resume_title), 0)

    def test_get_technical_skills_score(self):
        self.assertEqual(core_matching.get_technical_skills_score(self.must_have_skills, self.job_skills, self.resume_skills), 1)

def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()

