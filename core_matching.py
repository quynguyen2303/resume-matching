'''
This step match two fields:

1. Job title: match the job title in the resume to the job title in the job description using NLP techniques such as BERT. The output is a score between 0 and 1.

2. Technical skills: match the technical skills in the resume to the technical skills in the job description using rules. If the resume has a skill that is not in the job description, the score is 0. If the resume has a skill that is in the job description, the score is 1. The output is a score between 0 and 1 by dividing total skills in resumer that have in job description with total required skills in job description.

But, need to consider the weight or must-have skills in job description, if not match, should be consider to set resume to not match.

**So the score is calculated by the following formula:**

```
score = a * job_title_score + b * technical_skills_score
```

'''

import sys
import logging

from transformers import BertTokenizer, BertModel
import torch
from scipy.spatial.distance import cosine

def get_logger():
    logger = logging.getLogger('core_matching')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

logger = get_logger()

# Load pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
model = BertModel.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

def get_bert_embedding(sentence):
    tokens = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        embeddings = model(**tokens).last_hidden_state.mean(dim=1)[0].numpy()
    return embeddings

def compute_similarity(sentence1, sentence2):
    embed1 = get_bert_embedding(sentence1)
    embed2 = get_bert_embedding(sentence2)
    similarity = 1 - cosine(embed1, embed2)  # Using cosine similarity
    return similarity
    
def get_job_title_score_bert(job_title, resume_title):
    '''
    Calculate the score of job title matching using BERT.
    '''
    logger.info('Start to calculate job title score using BERT.')
    logger.info('Job title: %s' % job_title)
    logger.info('Resume title: %s' % resume_title)
    score = compute_similarity(job_title, resume_title)
    logger.info('Job title score: %s' % score)
    return score

def get_technical_skills_score( must_have_skills, job_skills, resume_skills):
    '''
    Calculate the score of technical skills matching.
    '''
    logger.info('Start to calculate technical skills score.')
    logger.info('Job skills: %s' % job_skills)
    logger.info('Resume skills: %s' % resume_skills)

    # job_skills = job_skills.split(',')
    # resume_skills = resume_skills.split(',')
    total_skills = len(job_skills)
    matched_skills = 0
    has_must_skills = False
    # TODO: Check if resume_skills is in must_have_skills
    for skill in resume_skills:
        if skill in must_have_skills:
            has_must_skills = True

    for skill in resume_skills:
        if skill in job_skills:
            matched_skills += 1
    logger.info('Has must have skills: %s' % has_must_skills)        
    logger.info('Technical skills score: %s/%s' % (matched_skills, total_skills))

    return matched_skills / total_skills if has_must_skills else 0

def get_matching_score(job_title, job_skills, resume_title, resume_skills, a=0.5, b=0.5):
    '''
    Calculate the matching score.
    '''
    logger.info('Start to calculate matching score.')
    job_title_score = get_job_title_score_bert(job_title, resume_title)
    technical_skills_score = get_technical_skills_score(job_skills, resume_skills)
    score = a * job_title_score + b * technical_skills_score
    logger.info('Matching score: %s' % score)
    return score

def main():
    '''
    Main function.
    '''
    logger.info('Start to match job title and technical skills.')
    job_title = sys.argv[1]
    job_skills = sys.argv[2]
    resume_title = sys.argv[3]
    resume_skills = sys.argv[4]
    score = get_matching_score(job_title, job_skills, resume_title, resume_skills)
    logger.info('Matching score: %s' % score)
    print(score)

if __name__ == '__main__':
    main()