# Resume Matching

## Environment
```
source resume_matching/bin/activate
```

## Description
The algorithm for matching a resume to a job description

## Approach

### Core matching
This step match two fields:

1. Job title: match the job title in the resume to the job title in the job description using NLP techniques such as BERT. The output is a score between 0 and 1.

2. Technical skills: match the technical skills in the resume to the technical skills in the job description using rules. If the resume has a skill that is not in the job description, the score is 0. If the resume has a skill that is in the job description, the score is 1. The output is a score between 0 and 1 by dividing total skills in resumer that have in job description with total required skills in job description.

But, need to consider the weight or must-have skills in job description, if not match, should be consider to set resume to not match.

**So the score is calculated by the following formula:**

```
score = a * job_title_score + b * technical_skills_score
```

### Quantitative matching
This step match two fields:

1. Years of experience: match the years of experience in the resume to the years of experience in the job description using rules. The output is a score between 0 and 1.
3. Location: match the location in the resume to the location in the job description using rules. The output is a score between 0 and 1.
4. Salary: match the salary in the resume to the salary in the job description using rules. The output is a score between 0 and 1.


