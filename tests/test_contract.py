from pathlib import Path
S=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text()
def test_surface():
 for n in ('gather','add_observation','diagnose','adopt','retire','get_circle'):assert 'def '+n in S
def test_complete_validator_replay():assert 'return run()==leader.calldata' in S and "len(rows)!=len(remedies)" in S
def test_observation_attribution():assert 'observation_indexes' in S and "x['origin']==origin" in S
def test_reversibility_selection_is_code():assert "safe.sort(key=lambda x:(x['irreversibility'],x['id']))" in S
def test_keeper_and_steward_are_separate():assert 'watcher==gl.message.sender_address' in S and 'gl.message.sender_address!=c.steward' in S
