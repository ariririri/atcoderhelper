from pathlib import Path
import argparse
from atcoderhelper.urlparser import UrlParser

def main(args):
    contest = args.contest
    up = UrlParser(contest)
    problems = up.get_problems()
    contest = Path(contest)
    contest.exists() or contest.mkdir()
    for problem in problems:
        data = up.get_inputs(problem)
        up.write_data(contest, data, problem[-1])




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='load_contest')
    parser.add_argument('-c','--contest', type=str,
                    help='an integer for the accumulator')
    args = parser.parse_args()
    main(args)