from HackerRank.Any_or_All import results

def test_results_true(monkeypatch):
    responses = iter(['5', '12 9 61 5 14'])
    monkeypatch.setattr('builtins.input', lambda: next(responses))

    assert results() == True

def test_results_false(monkeypatch):
    responses = iter(['5', '-12 9 61 5 14'])
    monkeypatch.setattr('builtins.input', lambda: next(responses))

    assert results() == False