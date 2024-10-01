# Science Synthesis

|         | Age | Subjects | Education Level | Native English |
|------------------|-----|-----------------------------------------------|-----------------|----------------|
| **Chemistry**    |     |                                               |                 |                |
| *Participant 1*  | 32  | Engineering, Science, Chemistry               | Graduate        | ✔️              |
| *Participant 2*  | 33  | Chemistry, Biochemistry (Molecular and Cellular) | Undergraduate  | ❌              |
| *Participant 3*  | 24  | Chemistry                                     | Doctorate       | ❌              |
| **Computer Science** |  |                                               |                 |                |
| *Participant 1*  | 24  | Engineering, Economics, Business, Computer Science, Marketing | Undergraduate | ✔️  |
| *Participant 2*  | 26  | Computing (IT), Engineering, Mathematics, Economics, Computer Science | Undergraduate | ❌ |
| *Participant 3*  | 33  | Computer Science, Computing (IT), Engineering, Mathematics, Physics | Undergraduate | ❌ |
| **Earth Science** |   |                                               |                 |                |
| *Participant 1*  | 30  | Earth, Environment, or Climate Sciences       | Undergraduate   | ✔️              |
| *Participant 2*  | 29  | Earth, Environment, or Climate Sciences, Geography, Science | Graduate       | ✔️ |
| *Participant 3*  | 28  | Earth, Environment, or Climate Sciences, Science | Graduate      | ✔️              |
| **Linguistics**  |     |                                               |                 |                |
| *Participant 1*  | 24  | Education, English Language, English Literature, Languages | Graduate       | ❌ |
| *Participant 2*  | 23  | Business, Languages, Management, Communication and/or Media | Graduate       | ❌ |
| *Participant 3*  | 24  | Languages                                     | Undergraduate   | ❌              |
| **Sociology**    |     |                                               |                 |                |
| *Participant 1*  | 30  | Sociology, Economics, Philosophy              | Graduate        | ❌              |
| *Participant 2*  | 24  | Art and/or design, Communication and/or Media, Computer Science, Fashion and textiles, Sociology | Undergraduate | ❌ |
| *Participant 3*  | 22  | Sociology                                     | Graduate        | ❌              |

**Table 1: Demographic information about study participants. All information is self-reported. Education level refers to the highest level of education completed.**



| Category          | Relevancy | Correctness | Completeness | Informativeness | Integration | Cohesion | Coherence | Readability | Conciseness | Avg  |
|-------------------|-----------|-------------|--------------|-----------------|-------------|----------|-----------|-------------|-------------|------|
| **Chemistry**     |           |             |              |                 |             |          |           |             |             |      |
| *GPT-4 (H/A)*     | 4.61/5.00 | 4.38/5.00   | 4.11/4.66    | 4.27/5.00       | 4.05/5.00   | 3.72/5.00| 3.88/5.00 | 4.22/5.00   | 4.22/4.00   | 4.16/4.85 |
| *Mistral (H/A)*   | 4.38/4.50 | 4.27/4.00   | 4.00/3.66    | 4.44/4.33       | 4.05/4.66   | 3.88/4.83| 3.94/4.66 | 4.27/5.00   | 3.50/4.00   | 4.08/4.40 |
| **Computer Science** |       |             |              |                 |             |          |           |             |             |      |
| *GPT-4 (H/A)*     | 4.66/5.00 | 4.50/5.00   | 4.05/4.50    | 3.88/5.00       | 4.38/5.00   | 4.27/5.00| 4.27/5.00 | 4.38/5.00   | 3.83/3.66   | 4.24/4.79 |
| *Mistral (H/A)*   | 4.38/3.16 | 4.33/3.33   | 3.22/3.16    | 3.22/3.33       | 3.44/3.16   | 3.66/3.16| 3.83/3.16 | 4.27/3.83   | 3.61/2.83   | 3.77/3.24 |
| **Earth Science** |           |             |              |                 |             |          |           |             |             |      |
| *GPT-4 (H/A)*     | 4.66/5.00 | 4.33/4.83   | 4.22/4.50    | 4.61/5.00       | 4.38/5.00   | 4.55/5.00| 4.44/5.00 | 4.55/4.83   | 4.72/3.66   | 4.49/4.75 |
| *Mistral (H/A)*   | 4.38/3.66 | 4.22/3.66   | 4.16/3.16    | 4.22/3.66       | 4.16/4.16   | 4.11/4.16| 4.22/4.00 | 4.61/4.50   | 4.44/3.50   | 4.27/3.83 |
| **Linguistics**   |           |             |              |                 |             |          |           |             |             |      |
| *GPT-4 (H/A)*     | 3.77/5.00 | 4.11/4.83   | 3.88/4.50    | 3.94/4.83       | 3.72/5.00   | 3.61/5.00| 3.61/5.00 | 3.94/5.00   | 3.88/4.00   | 3.82/4.79 |
| *Mistral (H/A)*   | 3.66/4.50 | 3.38/4.66   | 3.77/4.00    | 3.66/4.66       | 3.50/5.00   | 3.44/5.00| 3.27/4.83 | 3.72/5.00   | 3.55/4.16   | 3.55/4.64 |
| **Sociology**     |           |             |              |                 |             |          |           |             |             |      |
| *GPT-4 (H/A)*     | 4.16/5.00 | 3.83/5.00   | 3.55/4.50    | 4.16/5.00       | 3.55/5.00   | 3.72/5.00| 3.88/5.00 | 3.27/5.00   | 3.77/4.00   | 3.76/4.83 |
| *Mistral (H/A)*   | 3.50/4.66 | 3.16/3.66   | 2.33/3.66    | 3.05/4.33       | 2.83/4.66   | 3.38/4.66| 3.49/4.66 | 3.55/4.83   | 3.72/4.00   | 3.22/4.35 |
**Table 2: Average human and automatic (LLM) evaluation scores by characteristic.  For each domain/characteristic, the human scores are an average of 18 judgements (6 syntheses (2 samples x 3 synthesis types) x 3 participants) while the auto scores are an average of 6 judgements (6 syntheses (2 samples x 3 synthesis types) x 1 LLM evaluation).**