import argparse
import json
import os
import repo_browser
import githelper
import saver


def clear_data():
    saver.clear()


def generate_data(repo_root, repo_subdir, filename):
    os.chdir(repo_root)
    component_dirs = repo_browser.find_components(repo_subdir)

    component_contributors = []
    for component_dir in component_dirs:
        contributors = githelper.find_top_contributors(component_dir)
        component_contributors.append((component_dir, contributors[0:3]))

    if filename:
        to_return = {x[0]: x[1] for x in component_contributors}
        with open(filename, "w") as fout:
            json.dump(to_return, fout)

    display = ""
    for component, contributors in component_contributors:
        contributors_str = ", ".join([str(x) for x in contributors])
        display += f"{component} {contributors_str} \n"

    print(display)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scratch script')
    parser.add_argument('--clear', action='store_true', default=False, help='Clear saved data')
    parser.add_argument('--repo_root', type=str, help='Repo to use')
    parser.add_argument('--repo_subdir', type=str, help='Subdirectory of repo to use')
    parser.add_argument('--output_file', type=str, help='Filename to store json output')
    args = parser.parse_args()
    if args.clear:
        clear_data()
    if args.repo_root:
        generate_data(args.repo_root, args.repo_subdir, args.output_file)
