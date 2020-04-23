# Market Research with Crunchbase and Automata

Market research on newly funded startups with the Crunchbase and Automata Market Intelligence APIs via RapidAPI

## Getting Started

Get access to the Crunchbase API and Automata's Market Intelligence API and your RapidAPI key at:
* https://rapidapi.com/crunchbase-team1-crunchbase/api/crunchbase
* https://rapidapi.com/andrew.fraine/api/market-intelligence-by-automata

### Prerequisites

Setup a virtual environment and install the required packages

```
cd your_project_directory
python3 -m venv ./
source ./bin/activate
pip install requirements.txt
```

### Run

Get today's seed-rounds from Crunchbase and find company lookalikes from the command line

```
python run.py -k "rapid_api_key" -max max_number
```

Example

```
python run.py -k "******************" -max 5
```

The output will be added to the current directory as a .json file

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

