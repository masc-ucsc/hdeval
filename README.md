# HDEval

Hardware Description Evaluation suite for LLM

This repository has a set of benchmarks to evaluate LLMs performance with
Hardware generation.


READ THE USAGE RULES, we do not want to allow LLMs to use this benchmarks for
training.


# Usage Rules

* No LLM is allowed to scrap or use this repo. We have GPL license, and we
  never push the benchmarks directly (json file)

* Use the crypt/decrypt script, only push hdeval files (not json)

* Do NOT push the benchmarks or benhmark contents to another repo, unless
  it has the same HUMANS-only license.

* Never do a pull request or create an issue showing the context of the json
  files. Explain the problem, but do not show any json file content. Similar
  rules to cheating in classroom.

* You can create a pull request for new benchmarks, but always use the "crypt"
  command to transform an json file to a hdeval file.

* If you use the json contents against an LLM, make sure that it can not be
  used for training. E.g: it is OK to use OpenAI API (Python) but NOT OK to use
  the chatgpt GUI because the OpenAI usage license allows to use gui chats for
  training.

* NOT LEGAL or OK to use in the following places because they keep record and
  may be used for training:

    * ChatGPT gui (OK python prompt)
    * Claude gui (OK python prompt)
    * Mixtral gui (OK python prompt?)
    * Most leader board competitions or ELO scores

After cloning the repo, run decrypt, and it will create the json files for all
the files needed.

```
git clone git@github.com:masc-ucsc/HDEval.git
cd hdeval/sample
./decrypt
```

If you want to commit or pull request, use the crypt. NEVER push the json file.

```
cd hdeval/bench_name
../crypt version
git add version.hdeval
# NEVER NEVER ADD the json file
```

Do decrypt sample:
```
cd sample
rm -f 24a.json   # decrypt will not overwrite if it exists already
../decrypt 24a
```

The suggestion is to use the year and letters for the version. To pick the latest version,
the alphabetical sort is used over the hdeval filename (ls | sort).

# Python interface

The suggestion is to use the "hdeval_open("bench", ["version"]) provided by
hdeval.py sample code.  Cut and paste it to your python code, it will download
the benchmark requested into your "~/.cache/hdeval" directory, keeping only the
hdeval format (never the json). It returns a string with the json text file
contents.

Sample of usage:
```
# Before
x = json.load("some.json")

# Now
txt = hdeval_open("sample","24a")
x = json.read(txt)
```

# Organization

Each HDEval benchmark has a directory with the name. Each has a README file
with some information and acknowledgements/contributions.

For each directory, there can be several version files. When running, the
benchmark, it should say the version.

# Create a benchmark

Check the sample with the recommended version name (year + letter).

The "decrypt" version should have a json file with the following format:

For each test, there is a "test_name"" (simple_halfadder in sample_24a). This name should match the "name" field

* Each test is an json map with the following fields:

    * "instruction": the spec or instructions that the LLM will have to follow
      to create the functionality.

    * "response": the Verilog module that the LLM generated code should do a
      LEC against.

    * "pipeline": 0 or 1 indicating wether the test has pipeline (flops or
      latches or memories)

    * "name": The test name, it should match the json array entry name.

    * "interface": The Verilog module interface that this test should generate.
      It can use SystemVerilog syntax. The module name should match the "name"
      field.

The json file should "\n" instead of "newlines". Check sample.

# Credit

If you use HDEval in your paper, credit the benchmark creators inside the
bench_name/README as they recommend. Also, credit the HDEval benchmark.


