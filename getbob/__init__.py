import requests
import json
import sys
import os
import argparse
from html.parser import HTMLParser

stable_url = "http://d.defold.com/stable/"
__version__ = "1.0.0"

def log(string, verbose=False):
    if verbose:
        print(string)


class MyHTMLParser(HTMLParser):
    version_data = {}
    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, raw_data):
        if "var model" in raw_data[:100]:
            data = raw_data[raw_data.find("{"):]
            data = data[:data.find(r"\n")]
            json_data = json.loads(data)
            for version in json_data["releases"]:
                self.version_data[version["tag"]] = version["sha1"]


def _get_version_map(url=stable_url, verbose=False):
    response = requests.get(url)
    if response.status_code == 200:
        parser = MyHTMLParser()
        parser.feed(str(response.content))
        return parser.version_data
    else:
        log("Couldn't fetch version map HTML code: {}".format(response.status_code), verbose)
        return {}


def _get_latest_beta_sha():
    info = requests.get("http://d.defold.com/beta/info.json").json()
    return info["sha1"], info["version"]


def _get_latest_stable():
    info = requests.get("http://d.defold.com/stable/info.json").json()
    return info["sha1"], info["version"]


def download(version, output, verbose=False):
    if not output:
        print("Output file required")
    elif not version:
        sha, version = _get_latest_beta_sha()
        log("Getting latest stable version: {}".format(version), verbose)
        _download(sha, output, verbose=verbose)

    elif len(version.split(".")) == 3:
        version_map = _get_version_map()
        try:
            sha = version_map[version]
            _download(sha, output, verbose=verbose)
            return os.path.exists(output)
        except KeyError:
            print("Can't find version {} of bob, supply valid version".format(version))

    elif version == "beta":
        sha, version = _get_latest_beta_sha()
        log("Getting latest beta version: {}".format(version), verbose)
        _download(sha, output, verbose=verbose)

    else:
        _download(version, output, verbose=verbose)


def _download(sha, output, verbose=False):
    bob_url = "http://d.defold.com/archive/{}/bob/bob.jar".format(sha)
    if requests.head(bob_url).status_code > 400:
        log("Can't find version {} of bob, supply valid version".format(sha), verbose)
        sys.exit(1)

    target_folder = os.path.dirname(output)
    if os.path.exists(output):
        log("Overwriting file: {}".format(output), verbose)
        os.remove(output)

    if not os.path.exists(target_folder):
        log("Creating directories: {}".format(target_folder), verbose)
        os.makedirs(target_folder, exist_ok=True)

    r = requests.get(bob_url, stream=True)
    with open(output, "wb") as f:
        log("Downloading new bob: {}".format(sha), verbose)
        total_size = int(r.headers.get('content-length', 0))
        if total_size:
            dl = 0
            for data in r.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)

                # Progressbar
                done = int(50 * dl / total_size)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                sys.stdout.flush()
            sys.stdout.write("\n")
        else:
            f.write(r.content)
        log("Download completed", verbose)

def _cli_options():
    parser = argparse.ArgumentParser(description="Commandline tool to download Defold's Bob")
    parser.add_argument('--output', dest='output', help="File name of the output, required")
    parser.add_argument('--version', dest='version', nargs="?",
                        help="Which version to download, if not provided the latest stable will be used. "
                             "Either: sha1 string, version string (1.2.152) or 'beta'")
    parser.add_argument('--force', action='store_true', dest="force", help="Overwrite already downloaded bob")
    parser.add_argument('--verbose', action='store_true', dest='verbose', help="Print verbose output")
    input_args = parser.parse_args()

    return input_args


def _run_cli():
    options = _cli_options()
    download(options.version, options.output, options.version)


def main():
    try:
        run()
    except KeyboardInterrupt:
        sys.exit()
    except:
        raise


if __name__ == '__main__':
    main()