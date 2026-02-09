from flask import Flask, render_template, abort, url_for, json, jsonify, request, session, redirect, send_from_directory
from eliozoapp.eliozo_dao.indexes_repository import getWizardTopicsSPARQL

def getWorksheets():
    # Clear previous wizard data if starting fresh, or just redirect
    # session['worksheet_wizard_data'] = {} # Uncomment if we want to force reset on fresh visit
    return redirect(url_for('worksheet_wizard', step_id=1))

def _process_sparql_topics(sparql_response):
    """
    Transforms SPARQL JSON response into a nested dictionary for the template.
    Structure: { "CategoryName": [{"name": "SubtopicName", "id": "SubtopicID"}, ...], ... }
    """
    try:
        data = json.loads(sparql_response)
        bindings = data.get('results', {}).get('bindings', [])
    except Exception as e:
        print(f"Error parsing SPARQL response: {e}")
        return {}

    topics_map = {}
    
    # First pass: Identify categories (L2=0) and initialize them in order
    # Bindings are already sorted by L1, L2 from SPARQL
    
    # We need to maintain order, so we can use a list of tuples or rely on Python 3.7+ dict insertion order.
    # The existing template iterates over `topics_data.items()`.
    
    current_category = None
    
    for item in bindings:
        l2 = int(item.get('L2', {}).get('value', -1))
        name = item.get('topicName', {}).get('value', 'Unknown')
        t_id = item.get('topicIdentifier', {}).get('value', '')
        
        if l2 == 0:
            current_category = name
            if current_category not in topics_map:
                topics_map[current_category] = []
        elif l2 > 0 and current_category:
            # It's a subtopic of the current category (since query is ordered by L1, L2)
            # Check if it belongs to the current category based on L1?
            # actually SPARQL sort by L1, L2 guarantees that we see Category (L1=X, L2=0) then its children (L1=X, L2>0)
            topics_map[current_category].append({'name': name, 'id': t_id})
            
    return topics_map

def worksheet_wizard(step_id):
    if 'worksheet_wizard_data' not in session:
        session['worksheet_wizard_data'] = {}
    
    wizard_data = session['worksheet_wizard_data']

    if request.method == 'POST':
        # Update session with form data
        # Merge existing data with new form data
        for key, value in request.form.items():
            # Handle list inputs (checkboxes) correctly
            if key in ['subtopics', 'domains', 'methods', 'events', 'question_types', 'accessibility', 'include_mini_exercises', 'include_tips_box', 'allow_variants']: 
                 # Note: checkboxes with same name come as list in proper form handling, 
                 # but request.form.getlist(key) is needed for multiple values.
                 pass # We'll handle getlist below
            else:
                wizard_data[key] = value
        
        # Explicitly handle multi-value fields for the current step
        # Step 1
        if step_id == 1:
            wizard_data['subtopics'] = request.form.getlist('subtopics')
            # domains removed as per requirements
        # Step 2
        if step_id == 2:
            wizard_data['methods'] = request.form.getlist('methods')
        # Step 3
        if step_id == 3:
            wizard_data['events'] = request.form.getlist('events')
            wizard_data['question_types'] = request.form.getlist('question_types')
        # Step 4 - no multi-value fields typically, but check just in case
        
        # Advanced options handling (scattered across steps but might come here)
        wizard_data['accessibility'] = request.form.getlist('accessibility') # Advanced


        session['worksheet_wizard_data'] = wizard_data
        session.modified = True

        # Navigation
        if 'next' in request.form:
            return redirect(url_for('worksheet_wizard', step_id=step_id + 1))
        elif 'back' in request.form:
            return redirect(url_for('worksheet_wizard', step_id=step_id - 1))
        elif 'generate' in request.form:
            # Final submission
            return generate_worksheet_from_wizard(wizard_data)

    # GET request - valid step check
    if step_id < 1:
        return redirect(url_for('worksheet_wizard', step_id=1))
    if step_id > 4:
         return redirect(url_for('worksheet_wizard', step_id=4))

    # Breadcrumbs construction
    # Global template already includes "main" (Home), so we only need to append the specific page path.
    # User requested: "Sākums > Worksheets 1 (Goal)" format.
    
    current_step_name = 'Unknown'
    steps_map = {
        1: 'Goal',
        2: 'Difficulty',
        3: 'Sources',
        4: 'Output'
    }
    current_step_name = steps_map.get(step_id, '')
    
    # We pass a single navlink that represents the current state.
    # It points to the current wizard step (bolded by template because it is loop.last).
    navlinks = [
        {'url': 'worksheet_wizard', 'params': {'step_id': step_id}, 'title': f'Worksheets {step_id} ({current_step_name})'}
    ]

    # Fetch dynamic topics data
    topics_data = {}
    if step_id == 1:
        raw_sparql = getWizardTopicsSPARQL()
        topics_data = _process_sparql_topics(raw_sparql)

    template_context = {
        'title': 'Darbalapas (Wizard)',
        'step_id': step_id,
        'username': session.get('user', {}).get('name'),
        'wizard_data': wizard_data,
        'topics_data': topics_data,
        'navlinks': navlinks
    }
    
    # Render appropriate step template
    if step_id == 1:
        return render_template('wizard/step_1_goal.html', **template_context)
    elif step_id == 2:
        return render_template('wizard/step_2_difficulty.html', **template_context)
    elif step_id == 3:
        return render_template('wizard/step_3_sources.html', **template_context)
    elif step_id == 4:
        return render_template('wizard/step_4_output.html', **template_context)
    else:
        abort(404)

def generate_worksheet_from_wizard(data):
    # This would normally call the actual generation logic.
    # For now, we'll just forward to the existing API endpoint or render a success/debug page.
    # The original form posted to /api/generate-worksheet.
    # We can either redirect there with a 307 (to preserve POST) but we have data in session now, not form.
    # OR we construct a hidden form and submit it, OR we change the API to read from session/json.
    
    # Assuming the API endpoint expects form data.
    # We will simply render a temporary "generating" page that posts to the real endpoint, 
    # OR better yet, since we are in the controller, we can call the logic if it was importable.
    # But for this refactor, let's assume we want to POST to the existing endpoint.
    
    # Actually, the best way given the user request "it is meant for teachers to select parameters... please refactor it"
    # is to probably have this function act as the bridge.
    # Let's just return key attributes for now to prove it works, or render a "done" template.
    
    # Re-packing data to match original form keys where they differ? 
    # They seem to match 1:1 mostly.
    
    # Let's redirect to a "loading" page or simply pass the data to the generation function.
    # Since I don't see the generation function in this file, I'll assume we need to POST to /api/generate-worksheet
    # ONE OPTION: Render a page with hidden inputs and auto-submit JS. 
    pass
    # For now, let's just return stringified data to verify collection
    return jsonify({"status": "ready_to_generate", "data": data})