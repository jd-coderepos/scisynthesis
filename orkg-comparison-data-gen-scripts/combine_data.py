import pandas as pd
import json
import random


# Configuration
CONFIG = {
    'DATA_FILE': '', # path to existing data file
    'MISSING_DATA_OUT_FILE': '', # file name for saving samples with missing abstracts in json
    'NEW_DATA_OUT_FILE': '', # file name for saving complete dataset in .xlsx
}


def open_json(f):
    with open(f, 'r') as read_file:
        json_data = json.load(read_file)
    return json_data


def select_papers(l):
    """
    Selects and formats papers from a list of papers.

    This function performs the following steps:
    
    1. If the length of the list is a multiple of 5 (but not exactly 5):
       - Iterates over the list in chunks of 5 papers.
       - Creates dictionaries for each chunk with paper titles, abstracts, and DOIs.
       - Appends each dictionary to a list of papers.
    2. If the length of the list is not a multiple of 5:
       - Randomly selects 5 papers from the list.
       - Creates a dictionary with paper titles, abstracts, and DOIs.
    """
    if len(l) % 5 == 0 and len(l) != 5:
        papers = [ ]
        new_list = l.copy()
        for i in range(int(len(l) / 5)):
            five_papers = new_list[0:5]
            del new_list[0:5]
            papers_dict = { }
            for i in range(5):
                paper = five_papers[i]
                papers_dict[f'paper_{i+1}_title'] = paper['title']
                papers_dict[f'paper_{i+1}_abstract'] = paper['abstract'].strip()
                papers_dict[f'paper_{i+1}_doi'] = paper['doi']
            papers.append(papers_dict)
    else:    
        selected_papers = random.sample(l, k=5)
        papers = { }
        for i in range(5):
            paper = selected_papers[i]
            papers[f'paper_{i+1}_title'] = paper['title']
            papers[f'paper_{i+1}_abstract'] = paper['abstract'].strip()
            papers[f'paper_{i+1}_doi'] = paper['doi']
    return papers
            

def compile_data(d):
    """
    Compile and process data from the input dictionary.

    This function performs the following steps:
    
    1. Iterates over each key (comparison ID) in the input dictionary.
    2. Collects papers with abstracts for each comparison ID.
    3. Checks if there are at least 5 papers with abstracts:
       - If yes, it creates an info dictionary with field and problem details.
       - Selects papers using the select_papers function.
       - If select_papers returns a dictionary, merges it with the info dictionary and adds to `new_dataset`.
       - If select_papers returns a list, merges each item with the info dictionary and adds each to `new_dataset` with a unique key.
       - Uses the field ID and comparison to generate unique keys for new_dataset.
    4. If there are fewer than 5 papers with abstracts, adds the comparison ID entry to missing_dataset.
    """
    for d_id in d.keys():
        papers_with_abstracts = [ ]
        for paper in d[d_id]['papers']:
            if paper['abstract']:
                papers_with_abstracts.append(paper)
        if len(papers_with_abstracts) >= 5:
            info = {'field_id' : d[d_id]['field_id'],
            'field_label' : d[d_id]['field_label'],
            'comparison_id' : d[d_id]['comparison'],
            'problem_id' : d[d_id]['problem_id'],
            'problem_label' : d[d_id]['problem_label']}
            # check if dict or list
            papers = select_papers(papers_with_abstracts)
            if type(papers) is dict:
                field_id = d[d_id]['field_id']
                comparison = d[d_id]['comparison']
                new_dataset[f'{field_id},{comparison}'] = {**info, **papers}
            else:
                for i in range(len(papers)):
                    field_id = d[d_id]['field_id']
                    comparison = d[d_id]['comparison']
                    new_dataset[f'{field_id},{comparison}-{i}'] = {**info, **papers[i]}
        else:
            missing_dataset[d_id] = d[d_id]
        

def main():
            
    missing_dataset = { }
    new_dataset = { }
    
    data = open_json(CONFIG['DATA_FILE'])    
    compile_data(data)
    
    # format dataset into list of lists in order to convert to dataframe
    new_dataset_lst = [v for k, v in new_dataset.items()]
    df = pd.DataFrame(new_dataset_lst)
    
    # save datasets to files
    df.to_excel(CONFIG['NEW_DATA_OUT_FILE'])
    
    with open(CONFIG['MISSING_DATA_OUT_FILE'], 'w') as f:
        json.dump(missing_dataset, f)
        
main()
