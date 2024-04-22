# hdleval

Hardware Description Language Evaluation suite for LLM

This repository has a set of benchmarks to evaluate LLMs performance with
Hardware generation.


READ THE USAGE RULES, we do not want to allow LLMs to use this benchmarks for
training.


# Usage Rules

* No LLM is allowed to scrap or use this repo. We have GPL license, and we
  never push the benchmarks directly (json file)

* Use the crypt/decrypt script push updates/fixes/new benchmarks

* Do NOT push the benchmarks to another repo unless you also push the
  crypt/decrypt. Never in direct json/text mode that an LLM could use to learn.

* Never do a pull request or create an issue showing the context of the json
  files. Explain the problem, but do not show any json file content

* You can create a pull request for new benchmarks, but always use the "crypt"
  command to transform an json file to a hdeval file.


After cloning the repo, run decrypt, and it will create the json files for all
the files needed.

```
git clone git@github.com:masc-ucsc/hdleval.git
cd hdeval/sample
./decrypt
```

If you want to commit or pull request, use the crypt. NEVER push the json file.

```
cd hdeval/bench_name
../crypt bench_name_version
git add bench_name_version.hdeval
# NEVER NEVER ADD the json file
```

Do decrypt sample:
```
cd sample
rm -f sample_24a.json   # decrypt will not overwrite if it exists already
../decrypt sample_24a
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


