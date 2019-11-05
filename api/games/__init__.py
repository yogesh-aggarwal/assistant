"""
Game extention for Jarvis AI Project
"""

choice = {
    "trivia": [
        {
            "name": "opentdb",
            "category": "trivia",
            "api": {
                "host": "https://opentdb.com/api.php?",
                "attributes": {
                    "questionAmount": {"key": "amount", "range": "50"},
                    "questionCategory": {"key": "category", "range": "9-32"},
                    "questionDifficulty": {
                        "key": "difficulty",
                        "range": ["easy", "medium", "difficult"],
                    },
                    "questionType": {"key": "type", "range": ["multiple", "boolean"]},
                    "questionEncoding": {
                        "key": "encoding",
                        "range": ["url3986", "base64"],
                    },
                },
            },
        }
    ]
}


def init():
    pass
