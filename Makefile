# You can set these variables from the command line, and also
# from the environment for the first two.

SPHINXOPTS    ?=
ifeq ($(GITHUB_ACTIONS), true)
	SPHINXBUILD   ?= sphinx-build
else
	SPHINXBUILD   ?= ./img-venv/bin/sphinx-build
endif
SOURCEDIR     = source
BUILDDIR      = docs

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

venv:
	$(PYTHON) -m venv img-venv
	./venv/bin/python3 -m pip install -r requirements.txt

clean:
	-rm -rf $(BUILDDIR)

html:
	mkdir -p ./docs
	touch ./docs/.nojekyll
	echo "<head>\n<meta http-equiv=\"refresh\" content=\"0; url=./html/index.html\" />\n</head>" > ./docs/index.html
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
