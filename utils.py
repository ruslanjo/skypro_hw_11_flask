import json


def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as candidates_json:
        candidates_list = json.load(candidates_json)
    return candidates_list


def get_candidate_by_id(candidate_id, candidates_list):
    for candidate in candidates_list:
        if int(candidate.get('id')) == int(candidate_id):
            return candidate


def get_candidates_by_name(candidate_name, candidates_list):
    suitable_candidates = []
    for candidate in candidates_list:
        if candidate_name.lower() in candidate.get('name').lower():
            suitable_candidates.append(candidate)
    return suitable_candidates


def get_candidates_by_skill(skill_name, candidates_list):
    suitable_candidates = []
    for candidate in candidates_list:
        skills = candidate.get('skills').split(', ')
        skills = [skill.lower() for skill in skills]
        if skill_name.lower() in skills:
            suitable_candidates.append(candidate)
    return suitable_candidates
