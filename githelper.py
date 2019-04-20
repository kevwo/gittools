from subprocess import check_output


def find_top_contributors(directory):
    gitcmd = f"shortlog -s -n --all --no-merges --since 1.year.ago {directory}"
    output = check_output(["git", *gitcmd.split(" ")]).decode()
    return [tuple(x.strip().split("\t")) for x in output.split("\n")]
