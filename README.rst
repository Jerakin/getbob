getbob
######
Commandline tool to download Defold's Bob

********
Download
********
Install with ``pip install getbob``


*****
Usage
*****

.. code-block:: bash
    $ getbob --help
    usage: getbob [-h] [-o, --output OUTPUT] [-v [VERSION]] [-f] [--verbose]

    Commandline tool to download Defold's Bob

    required arguments:
      -o, --output OUTPUT   File name of the output

    optional arguments:
      -h, --help            show this help message and exit
      -v [VERSION], --version [VERSION]
                            Which version to download, if not provided the latest
                            stable will be used. Either: sha1 string, version
                            string (1.2.152) or 'beta'
      -f, --force           Overwrite already downloaded bob
      --verbose             Print verbose output


Integrates well with build systems such as Jenkins, you can set a string argument that you can use to specify which defold version to use.

Here's an example of how I use it on Jenkins
.. code-block:: bash
    export bob="$WORKSPACE/../bob/$defold.jar"

    # Get bob
    getbob --output $bob --defold $defold --no-progress


Can also be used to simply download a version of bob quickly to

`getbob --output bob.jar`
