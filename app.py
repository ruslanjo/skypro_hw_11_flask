from flask import Flask, render_template
from task_2.utils import load_candidates_from_json, get_candidate_by_id, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def index_page():
    candidates = load_candidates_from_json('candidates.json')
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<candidate_id>')
def candidate_page(candidate_id):
    candidates = load_candidates_from_json('candidates.json')
    candidate = get_candidate_by_id(candidate_id, candidates)
    return render_template('candidate_card.html', candidate=candidate)


@app.route('/candidate/<candidate_name>')
def show_candidates_with_matching_name(candidate_name):
    candidates = load_candidates_from_json('candidates.json')
    matching_candidates = get_candidates_by_name(candidate_name, candidates)
    candidates_count = len(matching_candidates)
    return render_template('search.html', candidates_count=candidates_count, candidates_found=matching_candidates)


@app.route('/skill/<skill_name>')
def show_candidates_with_matching_skill(skill_name):
    candidates = load_candidates_from_json('candidates.json')
    matching_candidates = get_candidates_by_skill(skill_name, candidates)
    candidates_count = len(matching_candidates)
    return render_template('skill.html',
                           skill=skill_name,
                           candidates_count=candidates_count,
                           candidates_found=matching_candidates)


app.run(debug=True)
