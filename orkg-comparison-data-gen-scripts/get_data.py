from functions import get_problem_content
from abstracts import get_abstract
from orkg import ORKG, Hosts
from tqdm import tqdm
import json

orkg = ORKG(host=Hosts.PRODUCTION)

start_page = 0
end_page = -1

fields = orkg.classes.get_resource_by_class_unpaginated(class_id='ResearchField').content

data = { }
papers_wo_abstracts = [ ]

for field in tqdm(fields):
    field_id = field['id']
    field_label = field['label']
    problems = orkg.problems.in_research_field(field_id).content
    if problems:
        for problem in problems:
            prob_id = problem['problem']['id']
            prob_label = problem['problem']['label']
            # get comparisons about research problem
            prob_comparisons = get_problem_content(prob_id)
            if prob_comparisons:
                for comparison in prob_comparisons:
                    # get contribution ids
                    contributions = orkg.statements.get_by_subject_and_predicate_unpaginated(subject_id=comparison['id'], predicate_id='compareContribution').content
                    if len(contributions) >= 5:
                        papers = { }
                        papers_set = set()
                        for contribution in contributions:
                            # map contributions to papers
                            paper = orkg.statements.get_by_object_and_predicate(object_id=contribution['object']['id'], predicate_id='P31').content
                            if paper:
                                paper_id = paper[0]['subject']['id']
                                paper_title = paper[0]['subject']['label']
                                p = orkg.papers.by_title(paper_title).content
                                doi = None
                                if p and type(p) is list:
                                    try:
                                        doi = p[0]['identifiers']['doi']
                                    except:
                                        pass
                                papers_set.add(paper_id)
                                papers[paper_id] = {'title': paper_title, 'doi': doi}
                        # only include comparisons with at least 5 papers
                        if len(papers_set) >= 5:
                            papers_info = [ ]
                            for p_id in papers_set:
                                abstract = get_abstract(p_id)
                                if type(abstract) is not str:
                                    abstract = None
                                    papers_wo_abstracts.append(
                                        {
                                            'id': p_id,
                                            'title': papers[p_id]['title'],
                                            'doi': papers[p_id]['doi'],
                                            'comparison': comparison['id']
                                        }
                                    )
                                papers_info.append(
                                    {
                                        'id': p_id,
                                        'title': papers[p_id]['title'],
                                        'doi': papers[p_id]['doi'],
                                        'abstract': abstract
                                    }
                                )
                            data[comparison['id']] = {
                                'field_id': field_id,
                                'field_label': field_label,
                                'problem_id': prob_id,
                                'problem_label': prob_label,
                                'comparison': comparison['id'],
                                'papers': papers_info
                            }


with open(f'path_to_dataset/papers_wo_abstracts_pages{start_page}-{end_page}.json', 'w') as f:
    json.dump(papers_wo_abstracts, f)

with open(f'path_to_dataset/data_w_some_missing_abstracts_pages{start_page}-{end_page}.json', 'w') as f:
    json.dump(data, f)
