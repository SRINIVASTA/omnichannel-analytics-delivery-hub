from collections import defaultdict

class OmnichannelMarkovAttribution:
    @staticmethod
    def calculate_paths():
        sample_journeys = [["Paid Ad", "Web Search", "In-Store Buy"], ["Web Search", "Bounce"], ["Paid Ad", "In-Store Buy"]]
        transitions = defaultdict(lambda: defaultdict(float))
        for journey in sample_journeys:
            for i in range(len(journey) - 1):
                transitions[journey[i]][journey[i+1]] += 1.0
        prob_map = {}
        for state, trans in transitions.items():
            total = sum(trans.values())
            prob_map[state] = {k: v / total for k, v in trans.items()}
        return prob_map
