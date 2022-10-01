from HackerRank.One_Week_Preparation_Kit.Day_4.mock_test import truckTour

def test_results_true():
    assert truckTour( ((1, 5), (10, 3), (3, 4)) ) == 1

def test_results_false():
    assert truckTour( ((5, 5), (10, 3), (3, 4)) ) == 0